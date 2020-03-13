from rest_framework import serializers
from rest_framework.serializers import(ValidationError)
from rest_framework.validators import UniqueValidator
from django.forms import widgets
from django.db.models import Q
from secret.models import Friends

class adding_friends(serializers.ModelSerializer):
   class Meta: 
      model=Friends
      fields=('name','age','department')  
   
   def __init__(self, *args, **kwargs):
      super(adding_friends, self).__init__(*args, **kwargs)
      for fieldname in ['name','age','department']:
         self.fields[fieldname].required = True
   
   def create(self, validated_data):
      friends = Friends.objects.create(**validated_data)
      return friends 
   def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      instance.name=instance.name.strip().capitalize()
      instance.age = validated_data.get('age', instance.age)
      instance.department = validated_data.get('department', instance.department)
      instance.save()
      return instance
   




