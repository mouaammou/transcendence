from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view (['GET','POST'])
@permission_classes([IsAuthenticated])
def json_get(request):

	if request.method == 'GET':
		data = Product.objects.all()
		seriaze_data = ProductSerializer(data, many=True)
		return Response(seriaze_data.data, status=200)	

	seriaze_data = ProductSerializer(data=request.data)
	if (seriaze_data.is_valid(raise_exception=True)):
		seriaze_data.save()
		return Response(seriaze_data.data)
	return Response(seriaze_data.data ,status=400)

	