#
# *@author huangpngyi
# coding;utf-8


from django.shortcuts import render, HttpResponse

import json, datetime

from webqq import utils,models
# Create your views here.


#全局的queue
global_msg_dic = {}

def dashboard(request):
    return render(request, 'webqq/dashboard.html')


def send_msg(request):

    print(request.POST)

    data = request.POST.get('data')
    data = json.loads(data)
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_id = data.get('to_id')
    user_obj = models.hpy_models.UserProfilehpy.objects.get(id=to_id)
    contact_type = data.get('contact_type')
    #把消息发到对应的queue里面
    #判断queue存不存在不存在就建立一个queue
    if contact_type == 'single':
         if  not  to_id in global_msg_dic:
              global_msg_dic[to_id] = utils.Chat()
         global_msg_dic[to_id].msg_queue_hpy.put(data)
         print('\033[31;1mPush msg [%s] into user [%s] queue' % (data['msg'],user_obj.name))
    elif contact_type == 'group':
        group_obj_hpy = models.QQGrouphpy.objects.get(id=to_id)
        for member in group_obj_hpy.members.select_related():
            #群发不给自己发
           if member.id != request.user.userprofilehpy.id:
               if  not  member.id in global_msg_dic:
                  global_msg_dic[member.id] = utils.Chat()
           global_msg_dic[to_id].msg_queue_hpy.put(data)
    return HttpResponse("aaaaaaaaa")


def get_msg(request):
    uid = request.GET.get('uid')
    if uid:
        res = []
        if uid not in global_msg_dic:
            global_msg_dic[uid] = utils.Chat()
        res = global_msg_dic[uid].get_msg(request)
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided!"))
