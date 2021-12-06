# **从零开始Django玩python**

一.**搭建环境**

**官方文档**[https://docs.djangoproject.com/zh-hans/3.2/]

本章教程https://www.bilibili.com/video/BV1iU4y1A7MH

1.下载：用pip安装器下载安装

```python
pip install Django==3.2
```

2.新建工程：

```python
cd d:\PythonDev\Django_WEB_DEV\BlogDev

django-admin startproject blog
```

3.结构分析

```python
+--Django_WEB_DEV\BlogDev\blog\
 --blog
​	--__init__.py
​	--blog/settings.py
​	--blog/urls.py
​	--blog/asgi.py
​	--blog/wsgi.py
```

- `manage.py`: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 [django-admin 和 manage.py](https://docs.djangoproject.com/zh-hans/3.2/ref/django-admin/) 获取所有 `manage.py` 的细节。

- 里面一层的 `blog/`目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 `blog.urls`).
- `blog/__init__.py`：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
- `blog/settings.py`：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](https://docs.djangoproject.com/zh-hans/3.2/topics/settings/) 了解细节。
- `blog/urls.py`：Django 项目的 URL 声明，就像你网站的“目录”。阅读 [URL调度器](https://docs.djangoproject.com/zh-hans/3.2/topics/http/urls/) 文档来获取更多关于 URL 的内容。
- ``blog/asgi.py`：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 [如何使用 ASGI 来部署](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/asgi/) 了解更多细节。
- `blog/wsgi.py`：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 [如何使用 WSGI 进行部署](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/wsgi/) 了解更多细节。

4.启动项目

```python
python manage.py runserver
```

看到默认网页就成功

二.**开始项目**

1.`blog/settings.py`配置一下语言等

```python
LANGUAGE_CODE = 'zh-hans' 

TIME_ZONE = 'Asia/Shanghai'
```

2.创建页面，此处页面取名为blogtest

```python
python manage.py startapp blogtest
```

会生成模块，以该模块为例

```python
blogtest/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

3.打开 `blogtest/views.py`输入，后面通过URL映射后显示效果

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
```

4.在 blogtest目录里新建一个 `urls.py` 文件输入下列代码使当前`blogtest/views.py`设置成index首页

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

5.在项目主文件`blog/urls.py`添加映射代码

```
from django.urls import include, path

urlpatterns = [
    path('blogtest/', include('blogtest.urls')),
    path('admin/', admin.site.urls),
]
```