# 企业网站管理系统

## 项目简介

这是一个基于Django 3.2.7开发的企业网站内容管理系统。系统提供了完整的企业网站功能，包括产品展示、新闻管理、图文管理、企业信息管理等功能。

## 技术栈

- **后端框架**: Django 3.2.7
- **数据库**: MySQL 5.7+
- **Python版本**: Python 3.8+
- **前端**: HTML5, CSS3, JavaScript, jQuery
- **其他依赖**: Pillow, PyMySQL, requests等

## 功能模块

### 核心功能
- 🏠 **首页展示**: 企业形象展示、产品轮播、新闻动态
- 📦 **产品管理**: 产品分类、产品展示、产品详情
- 📰 **新闻管理**: 新闻分类、新闻发布、新闻列表
- 🖼️ **图文管理**: 图文内容管理、图片展示
- 📄 **页面管理**: 单页面内容管理、企业信息
- 📝 **表单管理**: 留言表单、联系表单
- 🔗 **链接管理**: 友情链接管理
- 🎠 **幻灯管理**: 首页轮播图管理
- 🗺️ **站点地图**: 自动生成站点地图

### 管理功能
- 👤 **用户管理**: 管理员账号管理
- ⚙️ **系统配置**: 网站基本信息配置
- 📊 **数据统计**: 访问统计、内容统计
- 🔧 **缓存管理**: 数据库缓存管理
- 🔍 **SEO优化**: 百度推送、站点地图

## 环境要求

### 系统要求
- Python 3.8+
- MySQL 5.7+
- 推荐使用虚拟环境

### Python依赖
```
asgiref==3.4.1
backports.zoneinfo==0.2.1
certifi==2021.10.8
charset-normalizer==2.0.8
dictop==0.1.4
Django==3.2.7
django-smartfields==1.1.3
idna==3.3
magic-import==0.1.3
mysqlclient==2.1.0
Pillow==8.4.0
PyMySQL==1.0.2
pytz==2021.3
requests==2.26.0
six==1.16.0
sqlparse==0.4.2
tzdata==2021.5
urllib3==1.26.7
```

## 安装部署

### 1. 环境准备

#### 创建虚拟环境
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 数据库配置

#### 创建数据库
```sql
CREATE DATABASE lylksy_cn CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 配置数据库连接
编辑 `sx_cms/settings.py` 文件中的数据库配置：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lylksy_cn',           # 数据库名
        'USER': 'root',                # 数据库用户名
        'PASSWORD': 'your_password',   # 数据库密码
        'HOST': '127.0.0.1',          # 数据库主机
        'PORT': '3306',               # 数据库端口
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### 3. 数据库初始化

#### 导入初始数据
```bash
# 导入SQL文件（如果存在）
mysql -u root -p lylksy_cn < sql/lylksy_com.sql
```

#### 执行数据库迁移
```bash
# 创建缓存表
python manage.py createcachetable

# 执行迁移
python manage.py migrate

# 如果遇到表已存在的错误，使用fake标记
python manage.py migrate sites 0001 --fake
python manage.py migrate sites 0002 --fake
```

### 4. 创建管理员账号

```bash
python manage.py createsuperuser
```

按提示输入用户名、邮箱和密码。

### 5. 启动服务

```bash
python manage.py runserver
```

访问地址：
- 网站首页: http://localhost:8000/
- 管理后台: http://localhost:8000/sxkjcms-admin/

## 使用指南

### 管理后台使用

#### 登录管理后台
1. 访问 `http://localhost:8000/sxkjcms-admin/`
2. 使用创建的管理员账号登录
```yml
 创建管理员账号： python manage.py createsuperuser
 账号：maliang
 密码：maliang123
```

#### 主要功能模块

**网站配置 (site_set)**
- 网站基本信息设置
- 联系方式配置
- SEO设置
- 百度推送配置

**产品管理 (goods)**
- 产品分类管理
- 产品信息管理
- 产品图片上传

**新闻管理 (news)**
- 新闻分类管理
- 新闻发布管理
- 新闻图片管理

**图文管理 (tuwen)**
- 图文分类管理
- 图文内容管理

**页面管理 (page)**
- 单页面内容管理
- 企业信息管理
- 招聘信息管理

**表单管理 (form)**
- 留言管理
- 联系表单管理

**其他管理**
- 友情链接管理 (links)
- 幻灯管理 (slide_set)
- 站点地图管理 (sitemap_set)

### 前端页面访问

#### 主要页面
- 首页: `/`
- 产品列表: `/c/` (图文分类)
- 产品详情: `/c/{id}/`
- 新闻列表: `/a/` (新闻分类)
- 新闻详情: `/a/{id}/`
- 单页面: `/d/{slug}/`
- 联系我们: `/d/contact.html`
- 站点地图: `/sitemap.html`

#### 静态资源
- CSS文件: `/static/css/`
- JavaScript文件: `/static/js/`
- 图片文件: `/static/images/`
- 媒体文件: `/media/`

## 配置说明

### 重要配置文件

#### settings.py 主要配置
```python
# 调试模式（开发环境设为True，生产环境设为False）
DEBUG = True

# 允许的主机
ALLOWED_HOSTS = ['*']

# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# 媒体文件配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 缓存配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
        'TIMEOUT': 3,
    }
}
```

### 全局变量配置

系统通过 `sx_cms/contexts.py` 提供全局变量，包括：
- `site_mes`: 网站基本信息
- `comm_pro_c`: 产品分类
- `comm_case_c`: 图文分类
- `comm_news_c`: 新闻分类

## 维护指南

### 缓存管理

#### 清除缓存
```bash
# 方法1: 使用管理命令
python manage.py manage_cache clear

# 方法2: 使用脚本
python clear_cache.py

# 方法3: 在Django shell中
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()
```

### 数据库维护

#### 备份数据库
```bash
mysqldump -u root -p lylksy_cn > backup_$(date +%Y%m%d).sql
```

#### 恢复数据库
```bash
mysql -u root -p lylksy_cn < backup_20241217.sql
```

### 日志管理

系统日志存储在 `logs/` 目录下，定期清理旧日志文件。

### 静态文件收集

生产环境部署时需要收集静态文件：
```bash
python manage.py collectstatic
```

## 常见问题

### 1. 数据库连接错误
- 检查数据库服务是否启动
- 确认数据库配置信息正确
- 检查数据库用户权限

### 2. 静态文件无法访问
- 确认 `DEBUG = True`（开发环境）
- 检查 `urls.py` 中的静态文件配置
- 确认静态文件路径正确

### 3. 缓存表不存在
```bash
python manage.py createcachetable
```

### 4. 迁移错误
```bash
# 如果表已存在，使用fake标记
python manage.py migrate app_name migration_name --fake
```

### 5. 权限问题
- 检查文件权限
- 确认数据库用户有足够权限

## 开发指南

### 项目结构
```
项目根目录/
├── manage.py                 # Django管理脚本
├── requirements.txt          # Python依赖
├── clear_cache.py           # 缓存清理脚本
├── manage_cache.py          # 缓存管理命令
├── sx_cms/                  # 主项目配置
│   ├── settings.py          # 项目设置
│   ├── urls.py              # URL配置
│   ├── contexts.py          # 全局变量
│   └── ...
├── goods/                   # 产品管理应用
├── news/                    # 新闻管理应用
├── page/                    # 页面管理应用
├── form/                    # 表单管理应用
├── tuwen/                   # 图文管理应用
├── links/                   # 链接管理应用
├── slide_set/               # 幻灯管理应用
├── site_set/                # 网站配置应用
├── sitemap_set/             # 站点地图应用
├── sxkj_admin/              # 自定义管理后台
├── templates/               # 模板文件
├── static/                  # 静态文件
├── media/                   # 媒体文件
└── sql/                     # 数据库文件
```

### 添加新功能

1. 创建新的Django应用
2. 在 `settings.py` 中注册应用
3. 创建模型、视图、URL配置
4. 创建管理界面
5. 添加模板文件

### 自定义管理后台

系统使用自定义的管理后台 `sxkj_admin`，可以：
- 自定义管理界面样式
- 添加自定义功能
- 集成第三方组件

