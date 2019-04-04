from django.shortcuts import render
from road.models import Blackspot, Landslide,Update
from django.urls import reverse
from django.http import HttpResponseRedirect
from road.forms import Updateform
lat=0
lon=0
def map(request):
	loc = Blackspot.objects.all()
	loc1=Update.objects.all()
	n1=len(loc1)
	n = len(loc)
	coord1=[]
	coord = []
	for i in range(n):
		coord.append(loc[i].log)
		coord.append(loc[i].lat)
	for j in range(n1):
		coord1.append(loc1[j].longitude)
		coord1.append(loc1[j].latitude)
	print(coord1)
	print(loc1[1].longitude)

	if (request.method == 'POST'):
		lat = request.POST.get('geoc1')
		request.session['d1']=lat
		lon = request.POST.get('geoc2')
		request.session['d2']=lon
		print(lat,lon)
		flag=int(request.POST.get('geoc3'))
		if(flag==1):
			url = reverse('feedback',kwargs={})
			return HttpResponseRedirect(url)
		elif(flag==0):
			return render(request,"sos.html",{'lat':lat,'lon':lon})
	print(coord1)
	return render(request,"default.html",{'coord':coord,'c':coord1})


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
