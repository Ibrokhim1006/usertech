from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate,logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from admin_panel.serizalizers import *
from admin_panel.models import *
from sayts.serializers import *
from sayts.pagination import *



class SubMenuAllViewsSites(APIView):
    def get(self,request,format=None):
        objects_list = Menu.objects.all()
        serializers = SubMenuAllSeriazlizers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class SubMenuDeteilesViews(APIView):
    pagination_class = LargeResultsSetPagination
    serializer_class = PostMenuSerizalizers
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator
    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,self.request, view=self)
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    def get(self,request,pk,format=None):
        instance = SubmenuPost.objects.filter(id_menu__id=pk) 
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class MenuPostDeteile(APIView):
    def get(self,request,pk,format=None):
        objects = SubmenuPost.objects.filter(id=pk)
        serializers = PostMenuSerizalizers(objects,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
#=================SubMenu POSTS Views================================


#==================POST Views=========================================
class PostAllSitesViews(APIView):
    pagination_class = LargeResultsSetPagination
    serializer_class = PostBaseAllSerializers
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator
    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,self.request, view=self)
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    def get(self,request,format=None):
        instance = Post.objects.all() 
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
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



class VakansiyaGet(APIView):
    def get(self,request,format=None):
        objects = VacansiyaPost.objects.all()
        serializers = Vakan(objects,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)