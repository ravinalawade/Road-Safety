from django.shortcuts import render
from road.models import Blackspot, Sharpturn

def map(request):
	loc = Blackspot.objects.all()
	n = len(loc)
	coord = []
	for i in range(n):
		coord.append(loc[i].log)
		coord.append(loc[i].lat)
	return render(request,"default.html",{'coord':coord})