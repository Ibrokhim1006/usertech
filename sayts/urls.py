from django.urls import path
from sayts.views import *

urlpatterns = [
    #=================MENU URLS===========================================
    path('sub_menu_all_views_sayts/',SubMenuAllViewsSites.as_view()),
    path('sub_menu_deteiles_views/<int:pk>/',SubMenuDeteilesViews.as_view()),
    path('menu_post_deteile/<int:pk>/',MenuPostDeteile.as_view()),
    #=================POST URLS=============================================
    path('post_all_sites_views/',PostAllSitesViews.as_view()),
    path('post_deteile_sites_views/<int:pk>/',PostDeteileSitesViews.as_view()),

    path('vacansy_all_site_views/',VacansyAllSiteViews.as_view()),
    path('vakansiya_deteile_views/<int:pk>/',VakansiyaDeteileViews.as_view()),
    path('VakansiyaGet/',VakansiyaGet.as_view()),
    
]