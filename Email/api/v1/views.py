from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from Email.api.v1.serializers import MailSerailizers
from Email.models import Mail


class MailView(APIView):

    def get(self, request, format=None):

        mail = Mail.objects.all()
        serializer = MailSerailizers(mail, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MailSerailizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MailDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Mail.objects.get(pk=pk)
        except Mail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MailSerailizers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MailSerailizers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DraftView(APIView):

    def get(self, request, format=None):

        mail = Mail.objects.filter(sent=False)
        serializer = MailSerailizers(mail, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MailSerailizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInboxListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        mail = Mail.objects.filter( Q(receiver__id=request.user.id))
        print(request.user.email)
        serializer = MailSerailizers(mail, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MailSerailizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserSentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        mail = Mail.objects.filter( Q(sender_user__id=request.user.id))
        print(request.user.email)
        serializer = MailSerailizers(mail, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MailSerailizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

