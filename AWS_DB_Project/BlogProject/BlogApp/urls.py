from django.urls import path
from . import views


urlpatterns = [
    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
    path('get_all_blog/', views.show_blogs, name='get_all_blog'),
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('show_blog/<int:blog_id>', views.show_blog, name='show_blog')
]
