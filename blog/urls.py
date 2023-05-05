from django.urls import path
from . import views
urlpatterns = [
    path('', views.forum,name='forum'),
    path('post/<int:id>', views.post_item, name='post-item'),
    path('author/<slug:name>/', views.home, name='post-by-author'),
    path('post/create/', views.create_post, name='post-create'),
    path('post/update/<int:id>/', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'),
    path('post/category/<int:id>', views.post_category, name='post-by-category'),

]
