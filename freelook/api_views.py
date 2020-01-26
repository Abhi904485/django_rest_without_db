from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def freelook(request):
    if request.method == 'POST':
        data = request.data
        sad = int(data['SAD'])
        emr_percent = float(data['EMRPERCENT'])
        years = float(data['YEARS'])
        days = int(data['DAYS'])
        flc_rate = float(data['FLCRATE'])
        pro_rate = round((sad * flc_rate * days) / (years * (1 + emr_percent)))
        return Response({"pro_rate": pro_rate}, status=status.HTTP_200_OK)
