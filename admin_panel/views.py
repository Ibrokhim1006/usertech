from rest_framework.response import Response
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


# Menu Views
class MenuAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_all = Menu.objects.all()  
        serializer = MenuAllSerializers(objects_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        name = request.data['name']
        if name=='':
            return Response({'error':"Fill in the information"},status=status.HTTP_406_NOT_ACCEPTABLE)
        objects = Menu.objects.filter(name=name)
        if len(objects) != 0:
            return Response({'eror':"There is such a menu"},status=status.HTTP_406_NOT_ACCEPTABLE)
        objects_create = Menu(name=name)
        objects_create.save()  
        return Response({'message':"Information saved"},status=status.HTTP_201_CREATED)
class MenuChangeViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]    
    def put(self,request,pk,format=None):
        serializers = MenuChangeSerializers(instance=Menu.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':"success update"},status=status.HTTP_200_OK)
        return Response({'error':'update error data'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = Menu.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':"Delete success"},status=status.HTTP_200_OK)

class SubMenuAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_all = SubMenu.objects.all()  
        serializer = SubMenuAllSeriazlizers(objects_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = SubMenuCRUDSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':'Create Sucsess'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class SubMenuChangeViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_get = SubMenu.objects.filter(id=pk)
        serializers = SubMenuAllSeriazlizers(objects_get,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)   
    def put(self,request,pk,format=None):
        serializers = SubMenuCRUDSerializers(instance=SubMenu.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':"success update"},status=status.HTTP_200_OK)
        return Response({'error':'update error data'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = SubMenu.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':"Delete success"},status=status.HTTP_200_OK)