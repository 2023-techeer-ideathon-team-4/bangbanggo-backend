from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Input, Place
from .serializers import InputSerializer
from .gpt import get_gpt_answer

class InputPostAPIView(APIView):
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.validated_data['address']
            kilo = serializer.validated_data['kilo']
            count = serializer.validated_data['count']

            text = "현재 제 위치는 " + address + "입니다. 약 " + str(kilo) + "km 이내의 주변 관광지 중 " + str(count) + "가지를 추려서 관광지 이름만 현재 위치에서 가까운 순서대로 알려줄 수 있을까요?"

            answer = get_gpt_answer(text)
            answer = answer.split('. ')

            sight = []

            sight_data = []

            for i in range(len(answer)):
                k = answer[i].split('\n')
                for j in k:
                    sight_data.append(j)

            for i in range(len(sight_data)):
                for j in range(count+1):
                    if sight_data[i] == str(j):
                        sight.append(sight_data[i + 1])

            print(sight)

            input = Input.objects.create(address=address, kilo=kilo, count=count)

            for s in sight:
                Place.objects.create(place=s, input=input)

            return Response({'message': sight})

        else:
            return Response(serializer.errors, status=400)
        


        
