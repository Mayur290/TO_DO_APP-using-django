
from django.conf.urls import url
from django.contrib import admin
from .views import home_page, add , delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^first/$',home_page),
    url(r'^toadd/$',add),
    url(r'^deleteTodo/(?P<pk>\d+)/$',delete),
]
