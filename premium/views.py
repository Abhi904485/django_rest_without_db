from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def premium(request):
    if request.method == 'POST':
        data = request.data
        result = (data['RATE'] * data['SA']) // 1000
        return Response({"result": result}, status=status.HTTP_201_CREATED)
