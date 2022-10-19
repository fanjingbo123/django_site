from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

from Rec.models import User

from Rec import log
import logging


# data = User.objects.all().first()
# print(data.id)


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


def result(request):

    logger = logging.getLogger()
    logs = log.CommonLog(logger, "Rec/reclog/log.log")

    if request.is_ajax():
        itemid = request.POST.get('loadNewTable')
        uid = request.POST.get('uid')
        print("ID:", itemid, "uid:", uid)
        logs.info('id为'+uid+'的用户点击了'+'信息'+itemid)
        Data = {}
        return JsonResponse(Data)

    elif request.method == "GET":

        logs.info('进入推荐结果页面')
        return render(request, "rec_result.html")

    elif request.method == "POST":
        uid = request.POST.get('uid')
        # data = ItemList.objects.all()
        print(uid, data)
        logs.info('id为'+uid+'的用户登陆账号')

        List = [{'item_id': '1', 'item_name': 'zhongguo918'}, {'item_id': '2', 'item_name': 'zhongguo918'},
                {'item_id': '3', 'item_name': 'zhongguo918'}, {'item_id': '4', 'item_name': 'zhongguo918'}, {'item_id': '5', 'item_name': 'zhongguo918'}, {'item_id': '6', 'item_name': 'zhongguo918'}, {'item_id': '7', 'item_name': 'zhongguo918'}, {'item_id': '8', 'item_name': 'zhongguo918'}, {'item_id': '9', 'item_name': 'zhongguo918'}, {'item_id': '10', 'item_name': 'zhongguo918'}, {'item_id': '11', 'item_name': 'zhongguo918'}, {'item_id': '12', 'item_name': 'zhongguo918'}, {'item_id': '13', 'item_name': 'zhongguo918'}, {'item_id': '14', 'item_name': 'zhongguo918'}, {'item_id': '15', 'item_name': 'zhongguo918'}, {'item_id': '16', 'item_name': 'zhongguo918'}, {'item_id': '17', 'item_name': 'zhongguo918'}, {'item_id': '18', 'item_name': 'zhongguo918'}]

        return render(request, "rec_result.html", {'List': List, 'uid': uid})


# def addToBehaviour(request):
#     if request.method == "POST":
#         itemid = request.POST['itemid']
#         # 在这里将itemid加到那个behaviour表里
#         print(itemid)
#
#         return redirect('../recResult')
