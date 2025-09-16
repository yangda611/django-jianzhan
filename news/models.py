from django.db import models
from django.utils import timezone
from goods.models import GoodsCatalog
from page.models import GoodsTag, NewsTag
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor


class NewsCatalog(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name='文章分类名称')
    url = models.CharField(max_length=100, blank=False, unique=True, verbose_name='url后缀名',
                           help_text='请谨慎，URL一旦保存不能修改')
    category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                 related_name="news_c", on_delete=models.CASCADE)
    sort = models.SmallIntegerField(verbose_name='指定排序', null=True, blank=False)
    title = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='seo标题')
    keywords = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='seo关键词')
    describe = models.TextField(null=True, blank=True, verbose_name='seo描述')
    is_sitemap = models.BooleanField(default=True, verbose_name='是否加入站点地图')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news_catalog', args=[self.url])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'
        ordering = ['id']


class News(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True, verbose_name='文章标题')
    url = models.CharField(max_length=100, blank=False, unique=True, verbose_name='url后缀名',
                           help_text='请谨慎，URL一旦保存不能修改')
    c_url = models.CharField(max_length=100, unique=False, verbose_name='上级url')
    news_catalog = models.ForeignKey(NewsCatalog, null=True, on_delete=models.CASCADE, verbose_name='文章类别')
    is_topping = models.BooleanField(default=False, verbose_name='是否置顶')
    sort = models.SmallIntegerField(verbose_name='指定排序', null=True, blank=False)
    small_image = fields.ImageField(upload_to='news_images', blank=True, dependencies=[
        FileDependency(processor=ImageProcessor(format='WEBP'))], verbose_name='默认图片')
    source = models.CharField(max_length=255, blank=True, verbose_name='文章来源')
    vurl = models.TextField(blank=True, verbose_name='视频地址')
    title = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo标题')
    keywords = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo关键词')
    describe = models.TextField(null=True, blank=True, verbose_name='seo描述')
    is_sitemap = models.BooleanField(default=True, verbose_name='是否加入站点地图')
    summary = models.TextField(verbose_name='内容概要', null=True, blank=True)
    content = models.TextField(verbose_name='内容', null=True, blank=True)
    goods_tag = models.ManyToManyField(GoodsTag, blank=True, verbose_name='相关产品')
    news_tag = models.ManyToManyField(NewsTag, blank=True, verbose_name='相关文章')
    created_time = models.DateTimeField(default=timezone.now, verbose_name='发布日期')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news', args=[self.c_url, self.url])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = '文章信息'
        ordering = ['id']