from django.urls import path
from admin_panel.views import *

urlpatterns = [
    path('user_sigin_in_views/',UserSiginInViews.as_view()),
    path('user_profiles_views/',UserProfilesViews.as_view()),

    # Menu urls
    path('all_menu_views/',MenuAllViews.as_view()),
    path('menu_change_views/<int:pk>/',MenuChangeViews.as_view()),
    path('sub_menu_all_views/',SubMenuAllViews.as_view()),
    path('sub_menu_change_views/<int:pk>/',SubMenuChangeViews.as_view()),
]