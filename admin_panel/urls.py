from django.urls import path
from rest_framework import routers, serializers, viewsets
from admin_panel.views import *

urlpatterns = [
    path('user_sigin_in_views/',UserSiginInViews.as_view()),
    path('user_profiles_views/',UserProfilesViews.as_view()),
    #=========================Menu urls===============================
    path('sub_menu_all_views/',SubMenuAllViews.as_view()),
    path('sub_menu_change_views/<int:pk>/',SubMenuChangeViews.as_view()),
    #========================SubMenu Posts Urls=======================
    path('sub_menu_posts_base_views/',SubMenuPostsBaseViews.as_view()),
    path('sub_menu_posts_crud_views/<int:pk>/',SubMenuPostsCrudViews.as_view()),
    #========================Posts Urls===============================
    path('post_bae_all_views/',PostBaseAllViews.as_view()),
    path('post_base_change_views/<int:pk>/',PostBaseChangeViews.as_view()),
    #========================Vacanys Urls=============================
    path('vacanys_base_all_views/',VacansyBaseAllViews.as_view()),
    path('vacanys_base_change_views/<int:pk>/',VacanysBaseChangeViews.as_view()),
    #====================Forma Urls==================================
    path('application_base_all_views/',ApplicationBaseAllViews.as_view()),
    path('application_deteile_base_views/<int:pk>/',ApplicationDeteileBaseViews.as_view()),

    path('consultatsiya_base_all_views/',ConsultatsiyaBaseAllViews.as_view()),
    path('consultatsiya_deteile_base_views/<int:pk>/',ConsultatsiyaDeteileBaseViews.as_view()),

    path('forma_base_all_views/',FormaBaseAllViews.as_view()),
    path('forma_deteile_base_views/<int:pk>/',FormaDeteileBaseViews.as_view()),
]