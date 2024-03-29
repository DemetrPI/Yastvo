import sys
from PIL import Image
from io import BytesIO
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext as _

 

LABEL = (
        ('',""),
        ('N', 'New'),
        ('BS', 'Best Seller')
)

CATEGORY = (
    ('B', _('Breakfast')),
    ('LC', _('Lunch')),
    ('SN', _('Snack')),
    ('D', _('Drinks')),
    ('SD', _('Salads')),
    ('DS',_('Desserts'))
)

class MenuItems (models.Model):
    item = models.CharField(_('Meal name'), max_length=50)
    category = models.CharField(_('Category'), choices=CATEGORY, max_length=2, default='B')
    label = models.CharField(_('Label'), choices=LABEL, max_length=2, blank=True, null=True)
    item_description = models.CharField(_('Meal description'), max_length=150)
    item_composition = models.CharField(_('Ingredients'), max_length=150)
    item_weight = models.FloatField(verbose_name=_('Net weight'))
    item_price = models.FloatField(verbose_name=_('Meal price'), default=100.00)
    item_discount = models.FloatField(verbose_name=_('Discounted price'), blank=True, null=True)
    item_calories = models.IntegerField(verbose_name=_('Calories'), default=100)
    item_image = models.ImageField(_('Meal image'), upload_to='goods')
    milk_added = models.BooleanField(verbose_name=_('Milk components added'), default=False)
    
    class Meta:
        verbose_name = _('Meal')
        verbose_name_plural = _('Meals')
    

    def __str__(self):
        return self.item


    def save(self, *args, **kwargs):
        item_image = self.item_image
        img = Image.open(item_image)
        new_img = img.convert('RGB')
        resized_new_img = new_img.resize((600, 600), Image.LANCZOS)
        filestream = BytesIO()
        resized_new_img.save(filestream, 'JPEG', quality=25)
        filestream.seek(0)
        name = '{}.{}'.format(*self.item_image.name.split('.'))
        self.item_image = InMemoryUploadedFile(
            filestream, 'ImageField', name, 'jpeg/image', len(filestream.getbuffer()), None
        )
        super().save(*args, **kwargs)
    

    def get_absolute_url(self):
         return reverse ('add')

    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            "pk" : self.pk  
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            "pk" : self.pk
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item}"

    def get_total_item_price(self):
        return self.quantity * self.item.item_price

    def get_discount_item_price(self):
        return self.item.item_price - self.item.item_discount

    def get_amount_saved(self):
        return self.quantity * (self.item.item_price - self.item.item_discount)

    def get_total_price_with_discount(self):
        try:
            return self.quantity*(self.item.item_price - (self.item.item_price-self.item.item_discount))
        except:
            return self.quantity*(self.item.item_price)

    def get_final_price(self):
        if self.item.item_discount:
            return self.get_total_price_with_discount()
        return self.get_total_item_price()
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    checkout_address = models.ForeignKey(
        'CheckoutAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, default=user)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, default=123)
    email = models.EmailField(max_length=25, default='email@email.com')
    
    def __str__(self):
        return self.user.username
    
           
class Payment(models.Model):
    stripe_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
