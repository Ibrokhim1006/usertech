from django.urls import path
from rest_framework import routers, serializers, viewsets
from admin_panel.views import *

urlpatterns = [
    path('user_sigin_in_views/',UserSiginInViews.as_view()),
    path('user_profiles_views/',UserProfilesViews.as_view()),
    #=========================Menu urls===============================
    path('all_menu_views/',MenuAllViews.as_view()),
    path('menu_change_views/<int:pk>/',MenuChangeViews.as_view()),
    path('sub_menu_all_views/',SubMenuAllViews.as_view()),
    path('sub_menu_change_views/<int:pk>/',SubMenuChangeViews.as_view()),
    #========================SubMenu Posts Urls=======================
    path('sub_menu_posts_base_views/',SubMenuPostsBaseViews.as_view()),
    #========================Posts Urls===============================
    path('post_bae_all_views/',PostBaseAllViews.as_view()),
    path('post_base_change_views/<int:pk>/',PostBaseChangeViews.as_view()),
    #========================Vacanys Urls=============================
    path('vacanys_base_all_views/',VacansyBaseAllViews.as_view()),
    path('vacanys_base_change_views/',VacanysBaseChangeViews.as_view()),
]