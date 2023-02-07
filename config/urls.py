from django.contrib import admin
from django.urls import path, include
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('project.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
