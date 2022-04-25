from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/', include('django.contrib.auth.urls'), name='logout'),
    path('user_reg', views.user_reg, name='reg_user'),
    path('news', views.news, name='news'),
    path('create_article', views.create_new_article, name='create_article'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('update_profile/<int:user_id>', views.update_profiles, name='update_profile'),
    path('article/<int:article_id>', views.article_show, name='article'),
]