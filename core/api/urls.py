from home.views import index,person,login,PersonAPI,PeopleViewSet,RegisterAPI,LoginAPI
from django.urls import path,include

# from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')
urlpatterns = router.urls


urlpatterns = [
  path('', include(router.urls)),
  path('index/',index),
  path('person/',person),
  path('login/',login),
  path('personclass/',PersonAPI.as_view()),
  path('register/',RegisterAPI.as_view()),
  path('loginapi/',LoginAPI.as_view()),

]
