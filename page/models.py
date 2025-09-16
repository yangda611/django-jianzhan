

from django.db import models


class GoodsTag(models.Model):
    name = models.CharField(max_length=30, blank=True, unique=True, verbose_name='请在此添加1个产品标签')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品标签'
        verbose_name_plural = '产品标签'


class NewsTag(models.Model):
    name = models.CharField(max_length=30, blank=True, unique=True, verbose_name='请在此添加1个文章标签')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'


class TuWenTag(models.Model):
    name = models.CharField(max_length=30, blank=True, unique=True, verbose_name='请在此添加1个图文标签')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文标签'
        verbose_name_plural = '图文标签'


class Page(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name='单页名称')
    url = models.CharField(max_length=20, blank=False, unique=True, verbose_name='url后缀名', help_text='请谨慎，URL一旦保存不能修改')
    is_bar = models.BooleanField(default=True, verbose_name='是否加入导航')
    sort = models.SmallIntegerField(verbose_name='指定排序', null=True, blank=True)
    is_sitemap = models.BooleanField(default=False, verbose_name='是否加入站点地图')
    title = models.CharField(max_length=255, blank=True, verbose_name='seo标题')
    keywords = models.CharField(max_length=255, blank=True, verbose_name='seo关键词')
    describe = models.TextField(null=True, blank=True, verbose_name='seo描述')
    content = models.TextField(verbose_name='内容', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('page', args=[self.url])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '单页'
        verbose_name_plural = '单页管理'
        ordering = ['id']


class Job(models.Model):
    sort = models.IntegerField(null=False, blank=False, verbose_name='排序')
    name = models.CharField(max_length=100, blank=False, verbose_name='岗位名称')
    age = models.CharField(max_length=100, blank=False, verbose_name='年龄要求')
    xueli = models.CharField(max_length=100, blank=False, verbose_name='学历要求')
    address = models.CharField(max_length=150, blank=False, verbose_name='工作地点')
    describe = models.TextField(verbose_name='职位描述', null=True, blank=True)
    yaoqiu = models.TextField(verbose_name='任职要求', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '招聘岗位'
        verbose_name_plural = '人才招聘'
