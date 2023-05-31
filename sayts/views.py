from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate,logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from admin_panel.serizalizers import *
from admin_panel.models import *
from sayts.serializers import *



class SubMenuAllViewsSites(APIView):
    def get(self,request,format=None):
        objects_list = Menu.objects.all()
        serializers = SubMenuAllSeriazlizers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class SubMenuDeteilesViews(APIView):
    def get(self,request,pk,format=None):
        objects_filter = SubmenuPost.objects.filter(id_menu__id=pk)
        serializers = PostMenuSerizalizers(objects_filter,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class MenuPostDeteile(APIView):
    def get(self,request,pk,format=None):
        objects = SubmenuPost.objects.filter(id=pk)
        serializers = PostMenuSerizalizers(objects,many=True)
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

class VacansyAllSiteViews(APIView):
    def get(self,request,format=None):
        objects_list = Vacansy.objects.all().order_by('-pk')
        serializers = VacansySiteAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = VakansiyaPostSerizalizers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(files = request.data.get('files'))
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class VakansiyaDeteileViews(APIView):
    def get(self,request,pk,format=None):
        objects = Vacansy.objects.filter(id=pk)
        serializers = VacansySiteAllSerializers(objects,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)