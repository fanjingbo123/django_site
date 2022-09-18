from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def rec(request):
    # data = request.POST.get()
    # print(data)
    # print(111)
    if request.method == "GET":
        return render(request, "config.html")
    else:
        print(request.POST)
        return HttpResponse("配置成功")
        # return redirect('http://127.0.0.1:8000/recResult/rec_result.html')
# else :
#     return redirect('')

def result(request):
    return render(request, "rec_result.html")
