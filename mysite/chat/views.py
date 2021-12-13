from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Modelmassege
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


def index(request):
    chat = Modelmassege.objects.all()
    return render(request, 'chat/massandger.html', {'chat': chat})


def send_message(request):
    print(request.POST.get)

    if request.method == 'POST':
        # print(request.user)
        print(request.user.is_authenticated)
        if request.user.is_authenticated is True:
            autor = request.user
        else:
            chat = Modelmassege.objects.all()
            res = "Авторизийруйтесь для отправки сообщений!"
            return render(request, 'chat/massandger.html', {'res': res, 'chat': chat})

        if request.POST.get('delete'):
            Modelmassege.objects.all().delete()
            return HttpResponseRedirect("/")
        if request.POST['message'] == '':
            return HttpResponseRedirect("/")
        if request.POST.get('message'):
            text = request.POST['message']

            if any(map(str.isdigit, text)) is True:
                if request.user.is_superuser:
                    Modelmassege(text=text, author=autor).save()
                    return HttpResponseRedirect("/")
                else:
                    chat = Modelmassege.objects.all()
                    res = "Права ограничены!"
                    return render(request, 'chat/massandger.html', {'res': res, 'chat': chat})

            if "@" in text:
                chat = Modelmassege.objects.all()
                res = "Передача почты запрещена!"
                return render(request, 'chat/massandger.html', {'res': res, 'chat': chat})

            Modelmassege(text=text, author=autor).save()

            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")



def indexs(request):
    return render(request, 'chat/my.html')
