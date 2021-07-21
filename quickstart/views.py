from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
''' code HTTP status as responses'''
from rest_framework import status
from . import serializers
'''To run pending to execute the virtual env'''

# Create your views here.
class HelloApiView(APIView):
    '''Class of API view'''

    '''This set our API view to have the serializer class'''
    serializer_class = serializers.HelloSerializers

    #Each function must return a response object
    def get(self, request, format=None):
        '''Return list of features of the API view'''
        an_apiview = [
            'We use HTTP methods as functions(get, post, patch, put, delete)',
            'Its similiar to a traditional view of django',
            'This gives us more control about the logic of our application',
            'Maps manually the URLs'
        ]

        #Response transform the information to JSON, this information
        #must be an array or a dict
        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        })
        '''Now we can create a URL to view this api view through URL'''

    def post(self, request):
        '''Create a message with our name'''
        #Self.serializer is a class that set out class with the API view, standart method
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            '''This datas must be validated'''
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'message': message
            })
        #Not valid information
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Manage the object update'''

        return Response({
            'method': 'PUT'
        })

    def patch(self, request, pk=None):
        '''Manage partial update of an object'''
        return Response({
            'method': 'PATCH'
        })

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({
            'method': 'DELETE'
        })

    
