from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Django")


def rec(request):
    # data = request.POST.get()
    # print(data)
    # print(111)
    return render(request, "algorithm_config.html")