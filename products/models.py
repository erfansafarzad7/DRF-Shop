from django.db import models
from django.utils.translation import gettext as _


class Base(models.Model):
    title = models.CharField(_('Title'), max_length=20, unique=True)
    image = models.ImageField(_('Image'), upload_to='other_images/', null=True, blank=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField(_('Image'), upload_to='images/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.image.name


class Category(Base):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(Base):
    pass


class Product(models.Model):
    name = models.CharField(_('Product Name'), max_length=100)
    complete_descriptions = models.TextField(_('Product Descriptions'), max_length=256)
    category = models.ManyToManyField(Category, verbose_name='Product Category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Product Brand')
    image = models.ForeignKey(Images, on_delete=models.CASCADE, verbose_name='Product Image')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    def __str__(self):
        return self.name


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super(AvailableManager, self).get_queryset().filter(product__is_available=True, quantity__gte=1)


class ProductFeature(models.Model):
    key = models.CharField(_('Subject'), max_length=30, default='Color')
    value = models.CharField(_('Subject Value'), max_length=30, default='Black')

    def __str__(self):
        return f'{self.key} - {self.value}'


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_model = models.CharField(_('Product Model'), max_length=30, null=True, blank=True)
    short_description = models.CharField(_('Short Description (50 word)'), max_length=50)
    features = models.ManyToManyField(ProductFeature, verbose_name="Features")
    images = models.ManyToManyField(Images, verbose_name='Product Images')
    price = models.PositiveSmallIntegerField(_('Product Price'), )
    discount = models.PositiveSmallIntegerField(_('Product Discount'), default=0)
    quantity = models.PositiveSmallIntegerField(_('Product Quantity'), default=1)
    available = AvailableManager()
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} {self.product_model}'

    def product_name(self):
        return f'{self.product.name} {self.product_model}'

    def is_available(self):
        return True if self.quantity >= 1 else False

    def calc_discount(self):
        return self.price * (1 - self.discount / 100)
