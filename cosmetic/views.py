from django.shortcuts import render

# Create your views here.

def home(requset):
    return render(requset, 'home.html')
    # render는 3개의 인자를 받을 수 있음, 3번째는 사전형 객체