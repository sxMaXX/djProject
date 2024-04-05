import os
import random

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app.models import ModelMaXX
from app.form import ImageForm
from django.http import HttpResponseRedirect



image_dir = 'app/static/'
user_info = {'': False}


# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def maxx(request):
    if request.method == 'POST':
        users = list(ModelMaXX.objects.all().values())
        login = request.POST['login']
        pas = request.POST['pass']
        for u in users:
            if login == u['login']:
                if u['password'] == pas:
                    users_login = request.POST['login']
                    user_info[users_login] = True
                    html = redirect('/ziv', {'user': users_login})
                    html.set_cookie('user_session', users_login)
                    return html
                else:
                    return HttpResponse('Неверный логин или пароль')
        return HttpResponse('Неверный логин или пароль')
    return render(request, 'maxx.html')


def rename_image(fname, user_id: int):
    new_fname = 'IMG-' + str(user_id) + '-'
    for i in range(5):
        new_fname += chr(random.randint(65, 90))
    new_fname += '.' + fname.split('.')[-1]
    return new_fname


@csrf_exempt
def ziv(request):
    user_login = request.COOKIES.get('user_login')
    if user_login:
        print('Есть куки: ' + user_login)
        users = ModelMaXX.objects.all()
        for u in users:
            if u.user_login == user_login:
                profile_img = 'base_profile.jpg'
                if u.user_image:
                    profile_img = u.user_image
                    print("Загружено изображение пользователя из базы: " + profile_img)
            if request.method == "POST":
                if 'load' in request.POST:
                    form = ImageForm(request.POST, request.FILES)
                    if form.is_valid():
                        fname = request.FILES['user_image'].name
                        if u.user_image:
                            os.remove(image_dir + u.user_image)
                        form.save()
                        # добавляем новое
                        new_fname = rename_image(fname, u.id)
                        os.rename(image_dir + fname, image_dir + new_fname)
                        u.user_image = new_fname
                        u.save(force_update=True)
                        profile_img = new_fname
                form = ImageForm()
                print(profile_img)
                return render(request, 'ziv.html', {'user': u, 'profile_image': profile_img, 'form': form})
            html = render(request, 'index.html')
            html.delete_cookie('user_session')
            return html
        print('Куки отсутствуют')
    return render(request, 'ziv.html', {'users': request.COOKIES['user_session']})




@csrf_exempt
def out(request):
    return render(request, 'out.html')


@csrf_exempt
def res(request):
    if request.method == 'POST':
        users = list(ModelMaXX.objects.all().values())
        login = request.POST['login']
        pas = request.POST['pas']
        ph = request.POST['ph']
        for i in users:
            if login == i['login']: return HttpResponse('Такой пользователь уже существует')
        user = ModelMaXX()
        user.login = login
        user.password = pas
        user.email = ph
        user.save()
        return HttpResponse('Регистрация прошла успешно')
    else: HttpResponse('Произошла ошибка')
    return render(request, 'res.html')


@csrf_exempt
def profile(request):
    return render(request, 'profile.html')


def some_url(request, s):
    if s == '55555':
        return render(request, 'index.html')
    return render(request, 'error.html', {'url': s})
# Create your views here.
