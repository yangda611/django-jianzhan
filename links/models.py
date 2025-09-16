
from django.db import models

from goods.models import Goods
from news.models import News
from tuwen.models import TuWen


class Links(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True, default='', verbose_name='链接词')
    links_url = models.CharField(max_length=200, blank=False, unique=True, default='', verbose_name='URL')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'

class Mode(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='页面标题')
    url = models.CharField(max_length=50, default='', verbose_name='页面URL')
    number = models.CharField(max_length=30, verbose_name='输出投票数量『个数』')
    content = models.TextField(verbose_name='输出投票清单', null=True, blank=True)
    vote_number = models.SmallIntegerField(null=True, default=0, verbose_name='被投票数量『页数』')
    goods = models.ForeignKey(Goods, null=True, blank=True, on_delete=models.CASCADE, verbose_name='产品内链列表')
    news = models.ForeignKey(News, null=True, blank=True, on_delete=models.CASCADE, verbose_name='文章内链列表')
    tuwen = models.ForeignKey(TuWen, null=True, blank=True, on_delete=models.CASCADE, verbose_name='图文内链列表')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '内链统计'
        verbose_name_plural = '内链统计'

class LinkInner(models.Model):
    mode = models.ForeignKey(Mode, null=True, blank=True, on_delete=models.CASCADE, verbose_name='内链详情')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='投票页面标题')
    vote_url = models.CharField(max_length=50, default='', verbose_name='投票页面url')
    vote_keyword = models.CharField(max_length=100, default='', verbose_name='投票链接词')

    def __str__(self):
        return self.vote_keyword

