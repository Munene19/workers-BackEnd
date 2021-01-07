from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import status, viewsets, permissions, generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from .models import User, Profile, Jobpost, Reviews
from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer, ProfileSerializer, JobpostSerializer, ReviewsSerializer, RoleSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.data.get('username') != '':
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            profile = Profile.objects.get(pk=request.data.get('id'))
            if profile:
                serializer = ProfileSerializer(profile, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({
            'success':True,
            'message':'APIView: put request fulfilled',
            'data': ''

        })

    def delete(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            profile = Profile.objects.get(pk=request.data.get('id'))
            if profile:
                profile.delete()

        return Response({
            'success':True,
            'message':'APIView: delete request fulfilled',
            'data': ''

        })

@api_view(['GET'])
def singleprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


class JobpostAPIView(APIView):
    permission_classes = (AllowAny,)
     

    def get(self, request):
        jobpost = Jobpost.objects.all()
        serializer = JobpostSerializer(jobpost, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.data.get('id') != '':
            serializer = JobpostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            jobpost = Jobpost.objects.get(pk=request.data.get('id'))
            if jobpost:
                serializer = JobpostSerializer(jobpost, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({
            'success':True,
            'message':'APIView: put request fulfilled',
            'data': ''

        })

    def delete(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            jobpost = Jobpost.objects.get(pk=request.data.get('id'))
            if jobpost:
                jobpost.delete()

        return Response({
            'success':True,
            'message':'APIView: delete request fulfilled',
            'data': ''

        })

class ReviewsAPIView(APIView):
    permission_classes = (AllowAny,)
  

    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.data.get('id') != '':
            serializer = ReviewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            reviews = Reviews.objects.get(pk=request.data.get('id'))
            if reviews:
                serializer = ReviewsSerializer(reviews, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({
            'success':True,
            'message':'APIView: put request fulfilled',
            'data': ''

        })

    def delete(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            reviews = Reviews.objects.get(pk=request.data.get('id'))
            if reviews:
                reviews.delete()

        return Response({
            'success':True,
            'message':'APIView: delete request fulfilled',
            'data': ''

        })

class RoleAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.data.get('id') != '':
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)


