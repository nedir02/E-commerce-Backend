from django.db import models
from django.urls import reverse


class AllProducts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    main_img = models.ImageField(upload_to='uploads/', blank=True, null=True)
    img_1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    img_2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    img_3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    img_4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    img_5 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='category')
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'AllProduct'
        verbose_name_plural = 'AllProduct'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


