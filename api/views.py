from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    data = request.data.get('question')
    saida = []
    for valor, quantidade in Counter(data).most_common(len(Counter(data))):
        for _ in range(0, quantidade):
            saida.append(valor)
    return Response({'solution': saida})
