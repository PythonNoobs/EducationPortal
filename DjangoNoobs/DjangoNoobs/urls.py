from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('authorization.urls'), name='accounts'),
    path('testsystem/', include('testsystem.urls'), name='testsystem')
]
