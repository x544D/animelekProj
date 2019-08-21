from django.shortcuts import render
from users.models import Members
from django.http import HttpResponse

# Create your views here.
# users view 
def members_view(request, *args, **kwargs):
  
	u =[]
	for m in Members.objects.all():
		u.append("<div style ='color:red; border:2px black solid;' > ")
		u.append("<center>Name : %s <br>" % m.username)
		u.append("<center>Pass : %s <br>" % m.password)

	return HttpResponse(u)
	
  #return render(request, "members.html", dico)


