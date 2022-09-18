from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def rec(request):
    # data = request.POST.get()
    # print(data)
    # print(111)
    # if request.POST == GET:
        return render(request, "algorithm_config.html")

    # else :
    #     return redirect('')