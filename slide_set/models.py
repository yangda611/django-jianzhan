

from django.db import models


class PCSlide(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name='PC幻灯标题')
    linkurl = models.CharField(max_length=255, blank=False, unique=True, verbose_name='链接地址')
    pc_image = models.ImageField(verbose_name='幻灯图片', default=None, upload_to='news_images')
    sort = models.SmallIntegerField(verbose_name='指定排序', null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PC站幻灯'
        verbose_name_plural = 'PC站幻灯'


class MSlide(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name='移动站幻灯标题')
    linkurl = models.CharField(max_length=255, blank=False, unique=True, verbose_name='链接地址')
    m_image = models.ImageField(verbose_name='幻灯图片', default=None, upload_to='news_images')
    sort = models.SmallIntegerField(verbose_name='指定排序', null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '移动站幻灯'
        verbose_name_plural = '移动站幻灯'
