from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def json_get(request):

	data = Product.objects.all().order_by("?").first()

	json_data = {}
	# if data:
	# 	json_data['id'] = data.id;
	# 	json_data['title'] = data.title;
	# 	json_data['content'] = data.content;
	# if data:
	# 	json_data = model_to_dict(data, fields=['id', "title", 'price'])
	seriaze_data = ProductSerializer(data).data
	return Response(seriaze_data)