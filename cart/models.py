from django.db import models
from django.utils.translation import gettext as _
from products.models import ProductVariation
from accounts.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveSmallIntegerField(_('Quantity'), default=0)

    def __str__(self):
        return f'{self.user.phone_number} : {self.product.product.name}'
