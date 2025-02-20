from django.urls import path
from .views import BlogListView, BlogCreateView, blogDetailView

app_name = "blog"  # 🔹 Asegura que app_name esté definido correctamente

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),  #   🔹 "name" en lugar de "namespace"
    path('create/', BlogCreateView.as_view(), name='create'),
    #path('<int:pk>/', blogDetailView.as_view(), name='detail'),
    path('<int:id>/', blogDetailView.as_view(), name='detail'),


]
