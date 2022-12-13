from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class CategoryModel(MPTTModel):
    name = models.CharField(max_length=100,unique=True)
    parent = TreeForeignKey('self',on_delete=models.CASCADE, null=True, blank=True,related_name='children')

    class MPTTMeta:
        level_attr = 'parent_attr'
        order_insertion_by = ['name']


    def __str__(self):
        return self.name


class ProductsModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.name