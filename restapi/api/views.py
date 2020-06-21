from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def lambda_function(request):
    data = request.data.get('question')
    print(data)
    return Response({'1': '2'})

