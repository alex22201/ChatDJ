from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Modelmassege


def index(request):
    chat = Modelmassege.objects.all()
    return render(request, 'chat/massandger.html', {'chat': chat})


def send_message(request):
    print(request.POST.get)

    if request.method == 'POST':
        if request.POST.get('delete'):
            Modelmassege.objects.all().delete()
            return HttpResponseRedirect("/")
        if request.POST['message'] == '':
            return HttpResponseRedirect("/")

        if request.POST.get('message'):
            text = request.POST['message']

            # TODO

            if "@" in text:
                chat = Modelmassege.objects.all()
                res = "Передача почты запрещена!"
                return render(request, 'chat/massandger.html', {'res': res,'chat': chat})
            # phone
            Modelmassege(text=text).save()
            return HttpResponseRedirect("/")
