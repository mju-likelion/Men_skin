from django.shortcuts import render

# Create your views here.

def home(requset):
    return render(requset, 'home.html')
    # render는 3개의 인자를 받을 수 있음, 3번째는 사전형 객체
def find_foundation(requset):
    return render(requset, 'find_foundation.html')
def foundation_result(requset):
    return render(requset, 'foundation_result.html')
def mens_ranking(request):
    return render(request,'mens_ranking.html')
def mens_rankingdetail1(request):
    return render(request,'mens_rankingdetail1.html')
def mens_rankingdetail2(request):
    return render(request,'mens_rankingdetail2.html')
def search_result(request):
    return render(request,'search_result.html')
    #게시판
def board(request):
    return render(request, 'board.html')
def boardji(request):
    return render(request, 'boardji.html')
def board_view(request):
    return render(request, 'board_view.html')
def board_views(request):
    return render(request, 'board_views.html')
def board_write(request):
    return render(request, 'board_write.html')
def board_writes(request):
    return render(request, 'board_writes.html')