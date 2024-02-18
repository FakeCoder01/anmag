from django.shortcuts import render, redirect
from .models import AnonUser, Message
# Create your views here.


def create_new_user(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        
        if name != None:
            user = AnonUser.objects.create(name=name)
            return render(request, 'share.html', {'context' : user})
        return render(request, 'create.html', {'error' : True})
    return render(request, 'create.html')


def send_new_message(request, id):
    if not AnonUser.objects.filter(id=id).exists():
        return redirect('/')
    
    user = AnonUser.objects.get(id=id)

    if request.method == "POST":
        msg = request.POST.get('msg', None)
        extra = request.POST.get('extra', 'normal')

        if msg != None:
            msg = Message.objects.create(user=user, msg=msg, extra=extra)
            return render(request, 'success.html', {'context' : user})
        return render(request, 'send.html', {'error' : True, 'context' : user})
    return render(request, 'send.html', {'context' : user})


def view_messages(request, id, pin):
    if not AnonUser.objects.filter(id=id, pin=pin).exists():
        return redirect('/')
    user = AnonUser.objects.get(id=id, pin=pin)

    messages = Message.objects.filter(user=user).order_by('-sent_at')

    context = {
        "user" : user,
        "messages" : messages,
        "total_messages" : len(messages)
    }

    return render(request, 'messages.html', context)


