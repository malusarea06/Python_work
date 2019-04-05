from demo.models import NewUser
from django.http import HttpResponse

def addUser(request):

	newu = NewUser(
		username = 'malusarea111', city = 'pune')
	newu.save()

	


	allusers = NewUser.objects.all()

	res =''
	for elt in objects:
		res += elt.username


	return HttpResponse(res)






# Create your views here.
