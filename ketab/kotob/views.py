from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member, Question
from .serializers import MemberSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class Home(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        members = Member.objects.all()
        ser_data = MemberSerializer(instance=members, many=True)
        return Response(data=ser_data.data)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass


