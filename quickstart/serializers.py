'''Serializers allow complex data such as querysets and model instances 
to be converted to native Python datatypes that can then be easily 
rendered into JSON, XML or other content types. Serializers also provide 
deserialization, allowing parsed data to be converted back into complex 
types, after first validating the incoming data.'''

from django.contrib.auth.models import User,Group
from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    '''Serialize a field to prove our API view '''
    name = serializers.CharField(max_length=10)