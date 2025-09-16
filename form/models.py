
from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=20, blank=False, verbose_name='姓名')
    tel = models.CharField(max_length=20, blank=False, verbose_name='电话')
    email = models.EmailField(max_length=40)
    content = models.TextField(blank=False, verbose_name='留言内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')
    ipaddress = models.CharField(max_length=20, verbose_name='IP地址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言列表'
