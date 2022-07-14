from nturl2path import url2pathname
from django.urls import path
from .views import *


urlpatterns = [
    path('login/',Login.as_view(), name="login_api"),
    path('proudcto_create/',producto_create.as_view(), name="producto_create_api"),
    path('producto_update/',producto_update.as_view(), name="producto_update_api"),
    path('producto_read/<id>/',producto_read, name="producto_read"),
    path('producto_delete/<id>/',producto_delete, name="producto_delete"),
    path('producto_read_all/',producto_read_all, name="producto_read_all"),
   

]
