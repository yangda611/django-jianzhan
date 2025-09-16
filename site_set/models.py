

from django.db import models


# CACHE_TIME = (
#     (1, '3天'),
#     (2, '7天'),
#     (3, '15天'),
# )


class Site(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name='网站名称')
    url = models.CharField(max_length=40, blank=False, unique=True, verbose_name='首页网址')
    image = models.ImageField(upload_to='ico_images', verbose_name='ico图标')
    person = models.CharField(max_length=100, blank=True, unique=True, verbose_name='联系人')
    tel = models.CharField(max_length=100, blank=True, unique=True, verbose_name='电话')
    phone = models.CharField(max_length=100, blank=True, unique=True, verbose_name='手机')
    tel_400 = models.CharField(max_length=100, blank=True, unique=True, verbose_name='400电话')
    email = models.EmailField(max_length=100, verbose_name='邮箱')
    address = models.TextField(blank=True, unique=True, verbose_name='地址')
    wechat_openid = models.CharField(max_length=120, blank=True, unique=True, verbose_name='微信openid')
    icp_url = models.CharField(max_length=255, blank=True, unique=True, verbose_name='工信部网址')
    icp_num = models.CharField(max_length=30, blank=True, unique=True, verbose_name='ICP备案号')
    ga_url = models.CharField(max_length=255, blank=True, unique=True, verbose_name='公安备案网址')
    ga_num = models.CharField(max_length=35, blank=True, unique=True, verbose_name='公安备案号')
    baidu_api = models.CharField(max_length=255, blank=True, unique=True, verbose_name='百度推送token')
    tongji = models.TextField(blank=True, verbose_name='百度统计代码')
    talk = models.TextField(blank=True, verbose_name='在线沟通代码')
    title = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo标题')
    keywords = models.CharField(max_length=255, blank=False, unique=True, verbose_name='seo关键词')
    describe = models.TextField(blank=False, default='', verbose_name='seo描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '网站配置'
        verbose_name_plural = '网站配置'


class MinGan(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True, default='', verbose_name='敏感词')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '敏感词'
        verbose_name_plural = '敏感词管理'


class BaiduFanHuiZhi(models.Model):
    content = models.CharField(max_length=30, verbose_name='百度返回数据')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.content
