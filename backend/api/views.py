from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def json_get(request):

	if request.method == 'GET':
		data = Product.objects.all()
		seriaze_data = ProductSerializer(data, many=True)
		return Response(seriaze_data.data, status=200)

	# json_data = {}
	# if data:
	# 	json_data['id'] = data.id;
	# 	json_data['title'] = data.title;
	# 	json_data['content'] = data.content;
	# if data:
	# 	json_data = model_to_dict(data, fields=['id', "title", 'price'])
	seriaze_data = ProductSerializer(data=request.data)
	if (seriaze_data.is_valid(raise_exception=True)):
		seriaze_data.save()
		return Response(seriaze_data.data)
	return Response(seriaze_data.data ,status=400)

	