from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Input, Place
from .serializers import InputSerializer

class InputPostAPIView(APIView):
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            addr = serializer.validated_data['addr']
            km = serializer.validated_data['kilo']
            place_data = serializer.validated_data['place']

            place, created = Place.objects.get_or_create(place=place_data)

            
            input_obj = Input.objects.create(
                addr=addr,
                killo=kilo,
                place=place
            )

           
            return Response({'message': '정보가 성공적으로 입력되었습니다!'})
        else:
            return Response(serializer.errors, status=400)
        


        
