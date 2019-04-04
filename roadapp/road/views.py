from django.shortcuts import render
from road.models import Blackspot, Landslide
from django.urls import reverse
from django.http import HttpResponseRedirect
from road.forms import Updateform
lat=0
lon=0
def map(request):
	loc = Blackspot.objects.all()
	n = len(loc)
	coord = []
	for i in range(n):
		coord.append(loc[i].log)
		coord.append(loc[i].lat)

	if (request.method == 'POST'):
		lat = request.POST.get('geoc1')
		request.session['d1']=lat
		lon = request.POST.get('geoc2')
		request.session['d2']=lon
		print(lat,lon)
		flag=int(request.POST.get('geoc3'))
		print("flag"+str(flag))
		if(flag==1):
			url = reverse('feedback',kwargs={})
			return HttpResponseRedirect(url)
		elif(flag==0):
			return render(request,"sos.html",{'lat':lat,'lon':lon})
	return render(request,"default.html",{'coord':coord})


def feed(request):
	lat=request.session['d1']
	lon=request.session['d2']
	print(lat,lon)
	print(request.method)
	if request.method == 'POST':
		form = Updateform(request.POST or None)
		if form.is_valid():
			form.save()
			return render(request,"success.html",{})
	return render(request,"feedback.html",{'lat':lat,'lon':lon})
