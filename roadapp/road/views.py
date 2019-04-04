from django.shortcuts import render
from road.models import Blackspot, Landslide

def map(request):
	loc = Blackspot.objects.all()
	n = len(loc)
	coord = []
	for i in range(n):
		coord.append(loc[i].log)
		coord.append(loc[i].lat)

	if (request.method == 'POST'):
		lat = request.POST.get('geoc1')
		lon = request.POST.get('geoc2')
		print(lat,lon)
		return render(request,"sos.html",{'lat':lat,'lon':lon})
	return render(request,"default.html",{'coord':coord})