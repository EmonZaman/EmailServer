from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.v1.serializers import UserSerailizers
from accounts.models import User



class UserView(APIView):

    def get(self, request, format=None):

        user = User.objects.all()
        serializer = UserSerailizers(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):


        serializer = UserSerailizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

