from django.urls import path
from admin_panel.views import *

urlpatterns = [
    path('user_sigin_in_views/',UserSiginInViews.as_view()),
    path('user_profiles_views/',UserProfilesViews.as_view()),
]