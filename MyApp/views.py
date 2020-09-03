from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from MyApp.models import *


# @login_required
# def welcome(request):
#     print('###')
#     # HttpResponse 返回一个字符串
#     # HttpResponseRedirect 重定向到其他url上
#     # render 返回html页面和页面初始数据
#     return render(request, 'welcome.html')


def child(request, eid, oid):
    """
    render welcome.html页面的时候会调用该接口，目的是将welcome.html和子页面一同返回到前端
    :param request:
    :param eid:
    :param oid:
    :return:
    """
    res = child_json(eid, oid)
    return render(request, eid, res)


def child_json(eid, oid=''):
    """
    根据传入页面的不同，向child接口返回数据库数据，再有child返回给前端
    :param eid:
    :return:
    """
    res = {}
    if eid == 'home.html':
        data = DB_home_href.objects.all()
        res = {'hrefs': data}
    if eid == 'project_list.html':
        data = DB_project.objects.all()
        res = {'projects': data}
    if eid == 'P_apis.html':
        project = DB_project.objects.filter(id=oid)[0]
        apis = DB_apis.objects.filter(project_id=oid)
        res = {'project': project, 'apis': apis}
    if eid == 'P_cases.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {'project': project}
    if eid == 'P_project_set.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {'project': project}
    return res


@login_required
def home(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})


@login_required
def case_list(request):
    return render(request, 'welcome.html', {"whichHTML": "case_list.html", "oid": ""})


def login(request):
    """
    登陆页面
    :param request:
    :return:
    """
    return render(request, 'login.html')


def login_action(request):
    """
    登陆动作（数据库校验，返回）
    :param request:
    :return:
    """
    u_name = request.GET['username']
    p_word = request.GET['password']
    print(u_name, p_word)

    user = auth.authenticate(username=u_name, password=p_word)
    if user:
        auth.login(request, user)
        request.session['user'] = u_name
        return HttpResponse('成功')
    else:
        return HttpResponse('')


def register_action(request):
    """
    注册动作
    :param request:
    :return:
    """
    u_name = request.GET['username']
    p_word = request.GET['password']
    print(u_name, p_word)

    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=u_name, password=p_word)
        user.save()
        return HttpResponse('注册成功')
    except:
        return HttpResponse('注册失败，用户名已存在')


def login_out(request):
    """
    退出登录
    :param request:
    :return:
    """
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def pei(request):
    """
    吐槽功能
    :param request:
    :return:
    """
    tucao_text = request.GET['tucao_text']
    DB_tucao.objects.create(user=request.user.username, text=tucao_text)
    return HttpResponse('写入成功')


def api_help(request):
    """
    帮助页面
    :param request:
    :return:
    """
    return render(request, 'welcome.html', {'whichHTML': 'help.html', 'oid': ''})


def project_list(request):
    """
    项目列表
    :param request:
    :return:
    """
    return render(request, 'welcome.html', {'whichHTML': 'project_list.html', 'oid': ''})


def delete_project(request):
    """
    删除项目
    :param request:
    :return:
    """
    id = request.GET['id']
    DB_project.objects.filter(id=id).delete()
    return HttpResponse('删除成功')


def add_project(request):
    """
    新增项目
    :param request:
    :return:
    """
    project_name = request.GET['project_name']
    project_remark = request.GET['project_remark']
    DB_project.objects.create(name=project_name, remark=project_remark, user=request.user.username, other_user='')
    return HttpResponse('创建成功')


def open_apis(request, id):
    """
    进入接口库
    :param request:
    :return:
    """
    project_id = id
    return render(request, 'welcome.html', {'whichHTML': 'P_apis.html', 'oid': project_id})


def cases(request, id):
    """
    进入用例库
    :param request:
    :param id:
    :return:
    """
    project_id = id
    return render(request, 'welcome.html', {'whichHTML': 'P_cases.html', 'oid': project_id})


def project_set(request, id):
    """
    进入项目设置
    :param request:
    :param id:
    :return:
    """
    project_id = id
    return render(request, 'welcome.html', {'whichHTML': 'P_project_set.html', 'oid': project_id})


def save_project_set(request, id):
    """
    保存项目设置
    :param request:
    :return:
    """
    project_id = id
    name = request.GET['name']
    remark = request.GET['remark']
    other_user = request.GET['other_user']
    DB_project.objects.filter(id=project_id).update(name=name, remark=remark, other_user=other_user)
    return HttpResponse('')


def project_api_add(request, Pid):
    """
    新增接口
    :param request:
    :param Pid:
    :return:
    """
    project_id = Pid
    DB_apis.objects.create(project_id=project_id)
    return HttpResponseRedirect('/apis/{}/'.format(project_id))


def project_api_del(request, id):
    """
    删除接口
    :param request:
    :return:
    """
    project_id = DB_apis.objects.filter(id=id)[0].project_id
    DB_apis.objects.filter(id=id).delete()
    return HttpResponseRedirect('/apis/{}/'.format(project_id))


def save_bz(request):
    """
    添加备注
    :param request:
    :return:
    """
    api_id = request.GET['api_id']
    bz_value = request.GET['bz_value']
    DB_apis.objects.filter(id=api_id).update(des=bz_value)
    return HttpResponse('')


def get_bz(request):
    """
    获取备注
    :param request:
    :return:
    """
    api_id = request.GET['api_id']
    bz_value = DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(bz_value)