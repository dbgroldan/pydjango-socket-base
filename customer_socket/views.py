from django.http import HttpResponse
from django.shortcuts import render

def indexView(request):
    return HttpResponse('Ingresa url como: customer/room/str:user_id')

def roomView(request, room, user_id):
    return render(request,"chat_screen.html",{'room_name':room,'user_id': user_id})