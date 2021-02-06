from django.http import JsonResponse

# Create your views here.

def home(request):
	return JsonResponse({
		'info':'ecommerce Project with django and react',
		'name':'Ankit'
		})