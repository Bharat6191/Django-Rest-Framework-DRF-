# Django REST Framework (DRF)

This repository is a comprehensive guide for learning and implementing a Django REST Framework (DRF) project. It covers essential concepts and step-by-step processes for building APIs using DRF, including explanations of key components and code examples.

## Table of Contents 
1. [What is an API?](#what-is-an-api) 
2. [What is Django REST Framework?](#what-is-django-rest-framework) 
3. [What is Django REST API?](#what-is-django-rest-api) 
4. [Setting Up Django REST Framework](#setting-up-django-rest-framework) 
5. [Using `@api_view()` Decorator](#using-api_view-decorator) 
6. [HTTP Methods in DRF](#http-methods-in-drf) 
7. [Creating Models](#creating-models) 
8. [Understanding Serializers](#understanding-serializers) 
9. [Creating a Serializer](#creating-a-serializer) 
10. [Validation with Serializers](#validation-with-serializers) 
11. [Serializing Foreign Keys](#serializing-foreign-keys) 
12. [Class-based Views (APIView)](#class-based-views-apiview) 
13. [ModelViewSet](#modelviewset) 
14. [Token Authentication](#token-authentication) 
15. [Permissions in DRF](#permissions-in-drf) 16. [Pagination in DRF](#pagination-in-drf)

## 1. What is an API? An API (Application Programming Interface) allows communication between different software applications. It defines a set of rules that allow two applications to interact with each other.

## 2. What is Django REST Framework? Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs. It is built on Django and provides a simple yet robust way to build APIs with minimal effort.

## 3. What is Django REST API? Django REST API refers to web APIs created using Django REST Framework, allowing clients to interact with the backend through HTTP requests such as GET, POST, PUT, PATCH, and DELETE.

## 4. Setting Up Django REST Framework To set up DRF, follow these steps: 1. **Install DRF**: ```bash pip install djangorestframework ``` 2. **Add `rest_framework` to `INSTALLED_APPS` in `settings.py`**: ```python INSTALLED_APPS = [ ..., 'rest_framework', 'rest_framework.authtoken', ] ``` 3. **Configure DRF settings**: ```python REST_FRAMEWORK = { 'DEFAULT_AUTHENTICATION_CLASSES': [ 'rest_framework.authentication.BasicAuthentication', 'rest_framework.authentication.SessionAuthentication', ], 'DEFAULT_PERMISSION_CLASSES': [ 'rest_framework.permissions.IsAuthenticated', ], } ```

## 5. Using `@api_view()` Decorator The `@api_view()` decorator is used for function-based views to handle specific HTTP methods like GET, POST, etc.


### Example:
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def example_view(request):
    if request.method == 'GET':
        return Response({"message": "GET request"})
    elif request.method == 'POST':
        data = request.data
        return Response({"message": "POST request", "data": data})

## 6. HTTP Methods in DRF - GET: Retrieve data - POST: Create new data - PUT: Update existing data - PATCH: Partially update data - DELETE: Remove data

## 7. Creating Models Models in Django define the structure of your database tables.

### Example:
```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.ForeignKey('Color', on_delete=models.CASCADE, related_name="color", null=True)

    def __str__(self):
        return f"{self.name}-{self.age}-{self.color}"
      
## 8. Understanding Serializers Serializers in DRF help convert complex data types like querysets and model instances into native Python data types. They also handle data validation.

### 9. Creating a Serializer

### Example:
```python
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

## 10. Validation with Serializers Custom validation logic can be added to ensure data integrity.

### Example:
```python
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return value
## 11. Serializing Foreign Keys When dealing with models that have foreign key relationships, you can serialize related data.

### Example:
```python
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']
## 12. Class-based Views (APIView) APIView is a class-based view in DRF that offers more flexibility than function-based views.

### Example:
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleAPIView(APIView):
    def get(self, request):
        return Response({"message": "GET request"})
    
    def post(self, request):
        data = request.data
        return Response({"message": "POST request", "data": data})

## 13. ModelViewSet ModelViewSet allows CRUD operations with minimal code by combining view and serializer logic.

### Example:
```python
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


## 14. Token Authentication DRF supports token-based authentication for securing API endpoints.

Steps:
Add rest_framework.authtoken to INSTALLED_APPS.
Run migrations:
python manage.py migrate

## 15. Permissions in DRF Permissions control access to views based on the authentication status and user roles.

### Example:
```python

from rest_framework.permissions import IsAuthenticated

class SecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Secure content"})
## 16. Pagination in DRF DRF provides built-in pagination classes to handle large datasets.

### Example:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


## Project Structure - settings.py: Configuration for DRF and project setup. - views.py: Contains class-based and function-based views. - serializers.py: Defines serializers for data conversion and validation. - models.py: Contains Django models. - urls.py: Maps endpoints to view functions.
## cConclusion This guide provides an overview of the Django REST Framework essentials. With these concepts, you can create, manage, and secure robust APIs in Django. Explore the project and start building your own API-driven applications with DRF!