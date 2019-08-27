from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view()),
    path('admin/', admin.site.urls),
    path('testsystem/', include('testsystem.urls'))
]
