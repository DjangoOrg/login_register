from django.db import models

# Create your models here.

class User(models.Model):
    gender = (
        ('male',"男"),
        ('female',"女"),
    )
    name = models.CharField(max_length=255,unique=True,verbose_name="用户名")
    password = models.CharField(max_length=255,verbose_name="密码")
    email = models.EmailField(blank=True,null=True,verbose_name="邮箱")
    sex = models.CharField(max_length=32,choices=gender,default='男',verbose_name="性别")
    c_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    mobile_phone = models.CharField(max_length=11,verbose_name="手机号")
    def __str__(self):
        return self.name
    class Meta:
        ordering=["-c_time"]
        verbose_name="用户"
        verbose_name_plural="用户"

