from rest_framework.views import APIView
from rest_framework.response import Response
from .models import information
from .serializers import InformationSerializer

class InformationPostAPIView(APIView):
    def post(self, request):
        serializer = InformationSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.validated_data['address']
            km = serializer.validated_data['km']
            num_places = serializer.validated_data['num_places']

            
            info = information.objects.create(
                address=address,
                km=km,
                num_places=num_places
            )

           
            return Response({'message': '정보가 성공적으로 입력되었습니다!'})
        else:
            return Response(serializer.errors, status=400)
