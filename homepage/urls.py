from django.urls import path
from homepage import views
from design.views import portfolio
from blog.views import blog, blog_single

app_name='homepage'

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio', portfolio, name='portfolio'),
    path('blog', blog, name='blog'),
    path('blog-single/<int:id>/',blog_single,name='blog-single'),
]