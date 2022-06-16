from bdb import effective
from distutils.log import error
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
from .models import Message
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import json


def main_view(request):
    messages = Message.objects.all()

    return render(request, "messenger_app/main_page.html", {
        "messages": messages,
        "username": request.user.username,
    })

@csrf_exempt
def send_message(request):
    request_data = json.loads(request.body)
    print(request_data)
    sent_message_text = request_data["message-text"]
    print(sent_message_text)
    if (sent_message_text):
        new_message = Message.objects.create()
        new_message.text = sent_message_text
        new_message.save()
        return HttpResponse("ok")
    return HttpResponse("no message provided (POST: message-text)")


    
def get_all_messages(request):
    messages = Message.objects.all()
    
    response = {
        "messages": [],
    }

    for message in messages:
        response["messages"].append(message.text)

    return JsonResponse(response)


def login(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    error_text = ""

    if (username != "" and password != ""):
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            error_text = "incorrect login credentials"
        else:
            auth.login(request, user)
            return HttpResponseRedirect("/")

    return render(request, "messenger_app/login_page.html", {
        "error_text": error_text,
        "username": request.user,
    })
    


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
    
