from rest_framework.response import Response
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate,logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from admin_panel.pagination import *
from admin_panel.renderers import *
from admin_panel.models import *
from admin_panel.serizalizers import *

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'accsess':str(refresh.access_token)
    }

class UserSiginInViews(APIView):
    render_classes = [UserRenderers]
    def post(self,request,format=None):
        serializers = UserSiginInSerizalizers(data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                tokens = get_token_for_user(user)
                return Response({'token':tokens,'message':'Welcome to the system'},status=status.HTTP_200_OK)
            else:
                return Response({'error':{'none_filed_error':['This user is not available to the system']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class UserProfilesViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):  
        serializer = UserPorfilesSerializers(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)


#=======================================Menu Views===================================
class SubMenuAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_all = Menu.objects.all().order_by('pk')  
        serializer = SubMenuAllSeriazlizers(objects_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = SubMenuCRUDSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img = request.data.get('img'))
            return Response({'message':_('Create Sucsess')},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class SubMenuChangeViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_get = Menu.objects.filter(id=pk)
        serializers = SubMenuAllSeriazlizers(objects_get,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)   
    def put(self,request,pk,format=None):
        serializers = SubMenuCRUDSerializers(instance=Menu.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img = request.data.get('img'))
            return Response({'message':_("success update")},status=status.HTTP_200_OK)
        return Response({'error':_('update error data')},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = Menu.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':_("Delete success")},status=status.HTTP_200_OK)

#===========================================SubMenu POSTS Views========================
class SubMenuPostsBaseViews(APIView):
    pagination_class = LargeResultsSetPagination
    serializer_class = SubMenuPostSeriazlizers
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
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
        instance = SubmenuPost.objects.all()  
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = SubMenuPostCRUDSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img = request.data.get('img'))
            return Response({'message':_('Create Sucsess')},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class SubMenuPostsCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_all = SubmenuPost.objects.filter(id=pk)  
        serializer = SubMenuPostSeriazlizers(objects_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk,format=None):
        serializers = SubMenuPostCRUDSerializers(instance=SubmenuPost.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img = request.data.get('img'))
            return Response({'message':_("success update")},status=status.HTTP_200_OK)
        return Response({'error':_('update error data')},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = SubmenuPost.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':_("Delete success")},status=status.HTTP_200_OK)

#==============================================Posts Views============================
class PostBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
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
    def post(self,request,format=None):
        serializers = PostBaseCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class PostBaseChangeViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_get = Post.objects.filter(id=pk)
        serializers = PostBaseAllSerializers(objects_get,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)   
    def put(self,request,pk,format=None):
        serializers = PostBaseCrudSerializers(instance=Post.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img = request.data.get('img'))
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response({'error':_('update error data')},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = Post.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':_("Delete success")},status=status.HTTP_200_OK)
    

#==============================================Vacansy Views============================
class VacansyBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = VacansyBaseAllSerializers
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
        instance = Vacansy.objects.all()  
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = VacanysBaseCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class VacanysBaseChangeViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_get = Vacansy.objects.filter(id=pk)
        serializers = VacanysBaseCrudSerializers(objects_get,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)   
    def put(self,request,pk,format=None):
        serializers = VacanysBaseCrudSerializers(instance=Vacansy.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img = request.data.get('img'))
            return Response({'message':_("success update")},status=status.HTTP_200_OK)
        return Response({'error':_('update error data')},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = Vacansy.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':_("Delete success")},status=status.HTTP_200_OK)

#=======================Forma Views===========================================
class ApplicationBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = ApplicationSerizliers
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
        instance = Application.objects.all() 
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class ApplicationDeteileBaseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_get = Application.objects.filter(id=pk)
        serializers = ApplicationSerizliers(objects_get,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)   
    def delete(self,request,pk,format=None):
        objects_get = Application.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':_("Delete success")},status=status.HTTP_200_OK)

class ConsultatsiyaBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = ConsultatsiyaSerizliers
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
        instance = Consultatsiya.objects.all() 
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class ConsultatsiyaDeteileBaseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_get = Consultatsiya.objects.filter(id=pk)
        serializers = ConsultatsiyaSerizliers(objects_get,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)   
    def delete(self,request,pk,format=None):
        objects_get = Consultatsiya.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':_("Delete success")},status=status.HTTP_200_OK)

class FormaBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = FormaSerizliers
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
        instance = Forma.objects.all() 
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class FormaDeteileBaseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_get = Forma.objects.filter(id=pk)
        serializers = FormaSerizliers(objects_get,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)   
    def delete(self,request,pk,format=None):
        objects_get = Forma.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':_("Delete success")},status=status.HTTP_200_OK)