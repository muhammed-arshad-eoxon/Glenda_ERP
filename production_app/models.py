from django.db import models

# Create your models here.
class water_Finished_goods_category(models.Model):
    category_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.category_name


class water_Finished_Goods(models.Model):
    category = models.ForeignKey(water_Finished_goods_category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=True,unique=True)
    size = models.CharField(max_length=150, null=True,unique=True)
    image = models.ImageField(upload_to='images/',null=True)
    date = models.DateField(auto_now=True)
    total_stock = models.IntegerField(default=0)  # Field to track total stock


class damaged_Goods(models.Model):
    name = models.CharField(max_length=150, null=True,unique=True)
    image = models.ImageField(upload_to='images/',null=True)
    description =  models.CharField(max_length=200,null=True)