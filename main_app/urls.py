# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>', views.cats_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name='cats.create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('user/<username>', views.profile, name='profile'),
]