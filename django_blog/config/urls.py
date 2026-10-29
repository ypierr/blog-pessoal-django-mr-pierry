from django.contrib import admin
from django.urls import path
from blog.views import inicio, post_detalhe


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('post/<int:post_id>/', post_detalhe, name='post_detalhe'),]