"""UnitTestServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from autotrade import views as game_views
urlpatterns = [
    url(r'^$', game_views.index),
    url(r'^send/$', game_views.send, name='send'),
    url(r'^save/$', game_views.save, name='save'),
    url(r'^save_new_item/$', game_views.save_new_item, name='save_new_item'),
    url(r'^save_change_item/$', game_views.save_change_item, name='save_change_item'),
    url(r'^save_new_folder/$', game_views.save_new_folder, name='save_new_folder'),
    url(r'^save_change_folder/$', game_views.save_change_folder, name='save_change_folder'),
    url(r'^save_tree_state/$', game_views.save_tree_state, name='save_tree_state'),
    url(r'^save_tree_title/$', game_views.save_tree_title, name='save_tree_title'),
    url(r'^admin/', admin.site.urls),
]
