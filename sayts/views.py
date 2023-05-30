from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate,logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from admin_panel.serizalizers import *
from admin_panel.models import *



class SubMenuAllViewsSites(APIView):
    def get(self,request,format=None):
        objects_list = Menu.objects.all()
        serializers = SubMenuAllSeriazlizers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class SubMenuDeteilesViews(APIView):
    def get(self,request,pk,format=None):
        objects_filter = Menu.objects.filter(id=pk)
        serializers = SubMenuAllSeriazlizers(objects_filter,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
#=================SubMenu POSTS Views================================


#==================POST Views=========================================
class PostAllSitesViews(APIView):
    def get(self,request,format=None):
        objects_list = Post.objects.all().order_by('-id')
        serializers = PostBaseAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class PostDeteileSitesViews(APIView):
    def get(self,request,pk,format=None):
        objects_list = Post.objects.filter(id=pk)
        serializers = PostBaseAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)