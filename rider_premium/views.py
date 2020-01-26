from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def rider_premium(request):
    if request.method == 'POST':
        data = request.data
        rate = data['RATE']
        base_premium = data['BasePremium'] * 12
        ap = round((base_premium * rate) / 100)
        staff_disc = round(ap * 0.0859 - ap * 0.0859 * 0.1)
        return Response({"AP": ap, "Rider Premium in ruppes": staff_disc}, status=status.HTTP_201_CREATED)
