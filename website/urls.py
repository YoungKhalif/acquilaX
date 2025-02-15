from django.urls import path
from .views import home, blog_list, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog_list, name='blog_list'),
    path('contact/', contact_view, name='contact'),
]
