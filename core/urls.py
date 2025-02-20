from django.contrib import admin
from django.urls import include
from django.urls import path, include  # 🔹 Agrega "include"
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls', namespace='blog')),  # 🔹 Corregido "namespace"
]