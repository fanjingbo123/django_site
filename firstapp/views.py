from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def rec(request):
    # data = request.POST.get()
    # print(data)
    # print(111)
    if request.method == "GET":
        return render(request, "config.html")
    else:
        """获取推荐配置表单数据"""
        data = request.POST
        print(data)
        meta = dict(data)
        print(meta)
        # for item in meta['evaluation']:
        #     print(item)

        return HttpResponse("配置成功")
        # return redirect('http://127.0.0.1:8000/recResult/rec_result.html')
# else :
#     return redirect('')

def result(request):
    return render(request, "rec_result.html")
