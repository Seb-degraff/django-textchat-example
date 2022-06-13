from bdb import effective
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
from .models import Message

def main_view(request):
    sent_message_text = request.POST.get("message-text", "")
    if (sent_message_text != ""):
        new_message = Message.objects.create()
        new_message.text = sent_message_text
        new_message.save()

    messages = Message.objects.all()

    return render(request, "messenger_app/main_page.html", { "send_message": sent_message_text, "messages": messages })

def get_all_messages(request):
    messages = Message.objects.all()
    
    response = {
        "messages": [],
    }

    for message in messages:
        response["messages"].append(message.text)



    return JsonResponse(response)
