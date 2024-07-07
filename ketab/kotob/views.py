from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member
from .serializers import MemberSerializer


# @api_view(['GET'])
# def getdata(request):
#     return Response({'name': 'amir'})

class Home(APIView):
    def get(self, request):
        members = Member.objects.all()
        ser_data = MemberSerializer(instance=members, many=True)
        return Response(data=ser_data.data)


    def post(self, request):
        name = request.data['name']
        return Response({'name': name})