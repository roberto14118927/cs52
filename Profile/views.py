from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from Profile.models import Profile
from Profile.serializers import ProfileSerializer

class ProfileList(APIView):
    def get (self, request, format=None):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class ProfileDetail(APIView):
    def get_objetc(self, id):
        try:
            return Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        profile = self.get_objetc(id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    
