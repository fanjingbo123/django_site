from django.shortcuts import render, HttpResponse, redirect


from Rec.models import User
data = User.objects.all().first()
print(data.id)
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
        data = dict(data)
        print(data)
        # for item in meta['evaluation']:
        #     print(item)

        return HttpResponse("配置成功")
        # return redirect('http://127.0.0.1:8000/recResult/rec_result.html')
# else :
#     return redirect('')


def result(request):
    # global uid
    # global List
    if request.method == "GET":
        return render(request, "rec_result.html")
    else:
        uid = request.POST.get('uid')
        # data = ItemList.objects.all()
        print(uid, data)

        #
        List = [{'item_id': '123', 'item_name': 'zhongguo918'},{'item_id': '1234', 'item_name': 'zhongguo918'},{'item_id': '12345', 'item_name': 'zhongguo918'},{'item_id': '123456', 'item_name': 'zhongguo918'}]

        return render(request, "rec_result.html", {'List':List, 'uid':uid})

def addToBehaviour(request):
    # global uid
    # global List
    if request.method == "POST":
        itemid = request.POST['itemid']
        # 在这里将itemid加到那个behaviour表里
        print(itemid)

        return redirect('../recResult')



