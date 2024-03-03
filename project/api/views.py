from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Register(APIView):
  def post(self, request):
    if User.objects.filter(username=request.data['username']).count() == 0:
      if User.objects.filter(email=request.data['email']).count() == 0:
        user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
        refresh = RefreshToken.for_user(user)
        return Response(str(refresh.access_token))
      else:
        return Response({'type': 'email', 'text': 'Email address already taken'}, status=400)
    else:
      return Response({'type': 'username', 'text': 'This username is already in use, please try another one.'}, status=400)
