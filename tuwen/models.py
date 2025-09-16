from django.db import models
from page.models import GoodsTag, TuWenTag
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor


class TuWenCatalog(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name='图文分类名称')
    url = models.CharField(max_length=50, blank=False, unique=True, verbose_name='url后缀名', help_text='请谨慎，URL一旦保存不能修改')
    category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                 related_name="tuwen_c", on_delete=models.CASCADE)
    sort = models.SmallIntegerField(blank=False, null=True, verbose_name='指定排序')
    image = fields.ImageField(upload_to='tuwen_c_images', blank=True, dependencies=[
        FileDependency(processor=ImageProcessor(format='WEBP'))], verbose_name='默认图片')
    title = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo标题')
    keywords = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo关键词')
    describe = models.TextField(null=True, blank=True, verbose_name='seo描述')
    jianjie = models.TextField(null=True, blank=True, verbose_name='简介')
    is_sitemap = models.BooleanField(default=True, verbose_name='是否加入站点地图')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('tuwen_catalog', args=[self.url])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文分类'
        verbose_name_plural = '图文分类'
        ordering = ['id']


class TuWen(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name='图文名称')
    url = models.CharField(max_length=50, blank=False, unique=True, verbose_name='url后缀名', help_text='请谨慎，URL一旦保存不能修改')
    c_url = models.CharField(max_length=50, unique=False, verbose_name='上级url')
    tuwen_catalog = models.ForeignKey(TuWenCatalog, on_delete=models.CASCADE, verbose_name='图文类别')
    is_topping = models.BooleanField(default=True, verbose_name='是否置顶')
    sort = models.SmallIntegerField(verbose_name='指定排序', null=True, blank=False)
    file_upload = models.FileField(upload_to='files', blank=True, verbose_name='文件上传', default='')
    title = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo标题')
    keywords = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo关键词')
    describe = models.TextField(null=True, blank=True, verbose_name='seo描述')
    splj = models.CharField(max_length=150, blank=False, verbose_name='视频地址')
    is_sitemap = models.BooleanField(default=False, verbose_name='是否加入站点地图')
    summary = models.TextField(null=True, blank=True, verbose_name='内容摘要(选填)')
    content = models.TextField(verbose_name='内容', null=True, blank=True)
    goods_tag = models.ManyToManyField(GoodsTag, blank=True, verbose_name='相关产品')
    tuwen_tag = models.ManyToManyField(TuWenTag, blank=True, verbose_name='相关图文')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('tuwen', args=[self.c_url, self.url])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文信息'
        verbose_name_plural = '图文信息'
        ordering = ['id']


class TuWenImage(models.Model):
    # images = models.ImageField(verbose_name='请上传图片', default=None, upload_to='goods_images')
    images = fields.ImageField(upload_to='goods_images', dependencies=[
        FileDependency(processor=ImageProcessor(format='WEBP'))], verbose_name='请上传图片')
    alt = models.CharField(max_length=255, null=True, blank=True, verbose_name='图片标签')
    goods = models.ForeignKey(TuWen, null=True, blank=True, on_delete=models.CASCADE, verbose_name='项目图片')

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name_plural = '上传项目预览图片'
