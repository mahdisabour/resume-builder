from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .permissions import isAuthorize
from .models import Owner, Resume
from .serializers import resumeSerializer, resumeDetailSerializer




class resumeDetailView(APIView):

    def get(self, request, userId, resumeId):
        if (isAuthorize(request)):
            if(Owner.objects.filter(userId=userId).exists() and Resume.objects.filter(id=resumeId).exists()):
                resume = Resume.objects.get(id=resumeId)
                serializer = resumeDetailSerializer(resume)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    def patch(self, request, userId, resumeId):
        if (isAuthorize(request)):
            if(Owner.objects.filter(userId=userId).exists() and Resume.objects.filter(id=resumeId).exists()):
                resume = Resume.objects.get(id= resumeId)
                serializer = resumeDetailSerializer(resume, data= request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, userId, resumeId):
        if (isAuthorize(request)):
            if(Owner.objects.filter(userId=userId).exists() and Resume.objects.filter(id=resumeId).exists()):
                Resume.objects.get(id= resumeId).delete()
                
                return Response(status=status.HTTP_200_OK)
            else: 
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)



class resumeView(APIView):

    def get(self, request, pk, format=None):

        # correct this part
        if (not isAuthorize(request)):
            if(Owner.objects.filter(userId=pk).exists()):
                resumes = Owner.objects.get(userId=pk).resumes.all()
                serializer = resumeSerializer(resumes, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    def post(self, request, pk, format=None):

        if (isAuthorize(request)):
            if(Owner.objects.filter(userId=pk).exists()):
                owner = Owner.objects.get(userId=pk)
                data = request.data.copy()
                data["owner"] = owner.userId

                serializer = resumeSerializer(data=data)
                if serializer.is_valid():
                    _resume = serializer.save(owner=owner)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    def delete(self, request, pk, fromat=None):
        if (isAuthorize(request)):
            if(Owner.objects.filter(userId=pk).exists()):
                owner = Owner.objects.get(userId=pk)
                owner.resumes.all().delete()
                return Response(status.HTTP_200_OK)
                
            else: 
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
            





    

