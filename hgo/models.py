from django.db import models

# Create your models here.
class Stu(models.Model):
    name= models.CharField('姓名', max_length=50)
    gender= models.CharField('性别', max_length=2)
    age= models.IntegerField('年龄')
    address= models.CharField('地址', max_length=50)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
