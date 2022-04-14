from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# ? https://www.remoteinning.com/blog/how-to-use-jwt-authentication-with-django-rest-framework
# ? https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8
# ? https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



class BlacklistRefreshView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")