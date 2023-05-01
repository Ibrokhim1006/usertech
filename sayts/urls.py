from django.urls import path
from sayts.views import *

urlpatterns = [
    #=================MENU URLS===========================================
    path('menu_all_views_sayts/',MenuAllViewsSayts.as_view()),
    path('sub_menu_all_views_sayts/',SubMenuAllViewsSites.as_view()),
    path('sub_menu_deteiles_views/<int:pk>/',SubMenuDeteilesViews.as_view()),
    #=================POST URLS=============================================
    path('post_all_sites_views/',PostAllSitesViews.as_view()),
    path('post_deteile_sites_views/<int:pk>/',PostDeteileSitesViews.as_view()),
]