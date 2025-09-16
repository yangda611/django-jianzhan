
from django.db import models

W_CHOICES = (
    (1, '0.1'),
    (2, '0.2'),
    (3, '0.3'),
    (4, '0.4'),
    (5, '0.5'),
    (6, '0.6'),
    (7, '0.7'),
    (8, '0.8'),
    (9, '0.9'),
    (10, '1.0'),
)

F_CHOICES = (
    (1, 'always'),
    (2, 'hourly'),
    (3, 'weekly'),
    (4, 'monthly'),
    (5, 'yearly'),
    (6, 'never'),
)


class Sitemap(models.Model):
    name = models.CharField(max_length=30, help_text='示例：码良科技的站点地图')
    newscatalog = models.BooleanField(default=True, verbose_name='文章分类',
                                      help_text='文章分类已默认添加至sitemap，并继承已有自定义设置，如需修改请前往管理页面')
    goodscatalog = models.BooleanField(default=True, verbose_name='产品分类',
                                       help_text='产品分类已默认添加至sitemap，并继承已有自定义设置，如需修改请前往管理页面')
    tuwencatalog = models.BooleanField(default=True, verbose_name='图文分类',
                                       help_text='图文分类已默认添加至sitemap，并继承已有自定义设置，如需修改请前往管理页面')
    page = models.BooleanField(default=False, verbose_name='单页面', help_text='单页默认不添加sitemap，已继承已有自定义设置，如需修改请前往管理页面')
    index_w = models.SmallIntegerField(verbose_name='首页权重', choices=W_CHOICES)
    catalog_w = models.SmallIntegerField(verbose_name='分类页权重', choices=W_CHOICES)
    inner_w = models.SmallIntegerField(verbose_name='落地页权重', choices=W_CHOICES)
    page_w = models.SmallIntegerField(verbose_name='单页权重', choices=W_CHOICES)

    index_f = models.SmallIntegerField(verbose_name='首页更新频率', choices=F_CHOICES)
    catalog_f = models.SmallIntegerField(verbose_name='分类页更新频率', choices=F_CHOICES)
    inner_f = models.SmallIntegerField(verbose_name='落地页更新频率', choices=F_CHOICES)
    page_f = models.SmallIntegerField(verbose_name='单页更新频率', choices=F_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '站点地图'
