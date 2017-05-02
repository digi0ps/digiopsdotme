from django.shortcuts import render


def home_index(request):
	return render(request, "home/index.html")


def about(request):
	return render(request, "about/index.html")


def photos(request):
	return render(request, "uc.html")


def college(request):
	return render(request, "uc.html")