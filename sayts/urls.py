from django.urls import path
from sayts.views import *

urlpatterns = [
    path('menu_all_views_sayts/',MenuAllViewsSayts.as_view()),
    path('sub_menu_all_views_sayts/',SubMenuAllViewsSites.as_view()),
    path('sub_menu_deteiles_views/<int:pk>/',SubMenuDeteilesViews.as_view()),
]