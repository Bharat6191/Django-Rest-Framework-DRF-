from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PersonSerializer,LoginSerializer,RegisterSerializer
from .models import Person
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
class RegisterAPI(APIView):
  def post(self,request):
    data=request.data
    serializer=RegisterSerializer(data=data)
    if not serializer.is_valid():
      return Response({
        'status':False,
        'message': serializer.error}
      , status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response({'status':True,'message':'user created'},status.HTTP_201_CREATED)

class LoginAPI(APIView):
  def post(self,request):
    data=request.data
    serializer=LoginSerializer(data=data)
    if not serializer.is_valid():
      return Response({
        'status':False,
        'message': serializer.error}
      , status.HTTP_400_BAD_REQUEST)
    user=authenticate(username=serializer.data['username'],password=serializer.data['password'])
    if not user:
      return Response({
        'status':False,
        'message': 'invalid cred'}
      , status.HTTP_400_BAD_REQUEST)
    token , _= Token.objects.get_or_create(user=user)
    
    return Response({'status':True,'message':'user loggedin','token':token.key},status.HTTP_202_ACCEPTED)
  
    
  


def hello_word(request):
    return HttpResponse('<h1>Hello world!</h1><br><hr><br><p><b>To view api use PORT/api/PATH </p></b>')

@api_view(['GET','POST'])
def index(request):
  if request.method=='GET':
    courses={
      'name':'DRF'
    }
    Method={
       'HIT':'HIT GET METHOD'
    }
    return Response(courses,Method)
  elif request.method=='POST':
    data=request.data
    Method={
       'HIT':'HIT POST METHOD',
       'Data':f'{data}'
    }

    return Response(Method)
  elif request.method=='PUT':
    Method={
       'HIT':'HIT POST METHOD'
    }
    return Response(Method)
  else:
    Method={
       'HIT':'HIT Different METHOD'
    }
    return Response(Method)
 
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
  if request.method=='GET':
    obj=Person.objects.all()
    serializer=PersonSerializer(obj,many=True)
    return Response(serializer.data)
  elif request.method=='POST':
    data=request.data
    serializer=PersonSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  elif request.method=='PUT':
    data=request.data
    obj=Person.objects.get(id=data['id'])
    serializer=PersonSerializer(obj,data=data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
    else:
      return Response(serializer.errors)
  elif request.method=='PATCH':
    data=request.data
    obj=Person.objects.get(id=data['id'])
    serializer=PersonSerializer(obj,data=data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  else:
    data=request.data
    obj=Person.objects.get(id=data['id'])
    obj.delete()
    return Response({'message':'Person is deleted'})    

@api_view(['POST'])
def login(request):
  if request.method=='POST':
    data=request.data
    serializer=LoginSerializer(data=data)
    if serializer.is_valid():
      data=serializer.validated_data
      print(data)
      return Response({'message':'Success'})
    return Response(serializer.errors)

class PersonAPI(APIView):
  permission_classes = [IsAuthenticated]
  authentication_classes = [TokenAuthentication]
  

  def get(self,request):
    obj=Person.objects.all()
    serializer=PersonSerializer(obj,many=True)
    return Response(serializer.data)
  def post(self,request):
    data=request.data
    serializer=PersonSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  def put(self,request):
    data=request.data
    obj=Person.objects.get(id=data['id'])
    serializer=PersonSerializer(obj,data=data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
    else:
      return Response(serializer.errors)
  def patch(self,request):
    data=request.data
    obj=Person.objects.get(id=data['id'])
    serializer=PersonSerializer(obj,data=data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  def delete(self,request):
    data=request.data
    obj=Person.objects.get(id=data['id'])
    obj.delete()
    return Response({'message':'Person is deleted'})    
  
class PeopleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    def list(self,request):
      search=request.GET.get('search')
      queryset=self.queryset
      if search:
        queryset=queryset.filter(name__startswith=search)
      serializer=PersonSerializer(queryset,many=True)
      return Response({'status':200,'data':serializer.data})



