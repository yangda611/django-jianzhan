
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-^1ff%yl9p^fo5a6zi3j+yemntz1=h34dqk60uv&dvg7)31b+3#'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django_admin_global_sidebar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'sx_cms',
    'goods',
    'news',
    'page',
    'form',
    'tuwen',
    'links',
    'slide_set',
    'site_set',
    'sitemap_set',
    'sxkj_admin',
    'requests',
    'django.contrib.sites',
    'smartfields',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sxkj_admin.middleware.InvalidQueryStringMiddleware'
]
SITE_ID = 1
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
ROOT_URLCONF = 'sx_cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sx_cms.contexts.global_variable',
            ],
        },
    },
]

WSGI_APPLICATION = 'sx_cms.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lylksy',
        'USER': 'root',
        'PASSWORD': 'chenyang123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
        'TIMEOUT': 3,
        'OPTIONS': {
            'MAX_ENTRIES': 300,
            'CULL_FREQUENCY': 2,
         }
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
X_FRAME_OPTIONS = 'SAMEORIGIN'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'sxkj_service@163.com'
EMAIL_HOST_PASSWORD = 'UVBLHPFTVPXERVCG'

admin_address = "sxkjcms-admin/"


DJANGO_ADMIN_GLOBAL_SIDEBAR_MENUS = [
    {
        "title": "首页",
        "icon": "fa fa-home",
        "url": '/' + admin_address,
    }, {
        "title": "网站配置",
        "icon": "fa fa-cogs",
        "children": [
            {
                "title": "网站配置",
                "icon": "fas fa-list",
                "model": "site_set.site",
                "permissions": ["site_set.view_site"],
            }, {
                "title": "批量推送百度",
                "icon": "fas fa-list",
                "url": '/' + admin_address + "site_set/baidufanhuizhi/all_tui_view",
                "permissions": ["site_set.view_baidufanhuizhi"],
            }, {
                "title": "浏览推送数据",
                "icon": "fas fa-list",
                "url": '/' + admin_address + "site_set/baidufanhuizhi/view",
                "permissions": ["site_set.view_baidufanhuizhi"],
            }, {
                "title": "敏感词管理",
                "icon": "fas fa-list",
                "model": "site_set.mingan",
                "permissions": ["site_set.view_mingan"],
            }, {
                "title": "敏感词收集",
                "icon": "fas fa-list",
                "url": '/' + admin_address + "site_set/mingan/get_mgc",
                "permissions": ["site_set.view_mingan"],
            }, {
                "title": "缓存管理",
                "icon": "fas fa-list",
                "url": '/' + admin_address + "site_set/site/cache_view_page",
                "permissions": ["site_set.view_site"],
            }
        ]
    }, {
        "title": "产品管理",
        "icon": "fa fa-th-list",
        "children": [
            {
                "title": "产品分类",
                "icon": "fas fa-list",
                "model": "goods.goodscatalog",
                "permissions": ["goods.view_goodscatalog"],
            }, {
                "title": "产品信息",
                "icon": "fas fa-list",
                "model": "goods.goods",
                "permissions": ["goods.view_goods"],
            }
        ]
    }, {
        "title": "文章管理",
        "icon": "fa fa-book-reader",
        "children": [
            {
                "title": "文章分类",
                "icon": "fas fa-list",
                "model": "news.newscatalog",
                "permissions": ["news.view_newscatalog"],
            }, {
                "title": "文章信息",
                "icon": "fas fa-list",
                "model": "news.news",
                "permissions": ["news.view_news"],
            }
        ]
    }, {
        "title": "图文管理",
        "icon": "fa fa-qrcode",
        "children": [
            {
                "title": "图文分类",
                "icon": "fas fa-list",
                "model": "tuwen.tuwencatalog",
                "permissions": ["tuwen.view_tuwencatalog"],
            }, {
                "title": "图文信息",
                "icon": "fas fa-list",
                "model": "tuwen.tuwen",
                "permissions": ["tuwen.view_tuwen"],
            }
        ]
    }, {
        "title": "企业信息",
        "icon": "fa fa-list",
        "children": [
            {
                "title": "单页管理",
                "icon": "fas fa-list",
                "model": "page.page",
                "permissions": ["page.view_page"],
            }, {
                "title": "人才招聘",
                "icon": "fas fa-list",
                "model": "page.job",
                "permissions": ["page.view_job"],
            }, {
                "title": "产品标签",
                "icon": "fas fa-list",
                "model": "page.goodstag",
                "permissions": ["page.view_goodstag"],
            }, {
                "title": "文章标签",
                "icon": "fas fa-list",
                "model": "page.newstag",
                "permissions": ["page.view_newstag"],
            }, {
                "title": "图文标签",
                "icon": "fas fa-list",
                "model": "page.tuwentag",
                "permissions": ["page.view_tuwentag"],
            }
        ]
    }, {
        "title": "链接管理",
        "icon": "fa fa-link",
        "children": [
            {
                "title": "友情链接",
                "icon": "fas fa-list",
                "model": "links.links",
                "permissions": ["links.view_links"],
            }, {
                "title": "内部链接",
                "icon": "fas fa-list",
                "model": "links.mode",
                "permissions": ["link.inner"],
            }, {
                "title": "启动统计",
                "icon": "fas fa-list",
                "url": '/' + admin_address + "links/mode/links",
                "permissions": ["link.view_inner"],
            }
        ]
    }, {
        "title": "留言管理",
        "icon": "fa fa-swatchbook",
        "children": [
            {
                "title": "留言列表",
                "icon": "fas fa-list",
                "model": "form.message",
                "permissions": ["form.view_message"],
            }
        ]
    }, {
        "title": "幻灯管理",
        "icon": "fa fa-image",
        "children": [
            {
                "title": "PC站幻灯",
                "icon": "fas fa-list",
                "model": "slide_set.pcslide",
                "permissions": ["slide_set.view_pclide"],
            }, {
                "title": "移动站幻灯",
                "icon": "fas fa-list",
                "model": "slide_set.mslide",
                "permissions": ["slide_set.view_mslide"],
            },
        ]
    }, {
        "title": "站点地图",
        "icon": "fa fa-sitemap",
        "children": [
            {
                "title": "sitemap管理",
                "icon": "fas fa-list",
                "model": "sitemap_set.sitemap",
                "permissions": ["sitemap_set.view_sitemap"],
            }
        ]
    }, {
        "title": "用户管理",
        "icon": "fa fa-cogs",
        "children": [
            {
                "title": "用户管理",
                "icon": "fas fa-user-edit",
                "model": "auth.user",
                "permissions": ["auth.view_user", ],
            },
            {
                "title": "用户组管理",
                "icon": "fas fa-users",
                "model": "auth.group",
                "permissions": ["auth.view_group", ],
            },
            {
                "title": "日志管理",
                "icon": "fas fa-book-open",
                "url": '/' + admin_address + "admin/logentry/",
                "permissions": ["auth.view_user", ],
            }
        ]
    },
]
