from django.shortcuts import render

def wiki(request):
    return render(request, 'wiki/wiki.html')
def 歷年專輯介紹(request):        
    return render(request, 'wiki/歷年專輯介紹.html')
def 成員(request):
    return render(request, 'wiki/成員.html')
def 首張同名專輯(request):
    return render(request, 'wiki/首張同名專輯.html')
def U台灣限定普通版(request):
    return render(request, 'wiki/U台灣限定普通版.html')
def sorrysorry(request):
    return render(request, 'wiki/sorrysorry.html')
def Bonamana(request):
    return render(request, 'wiki/Bonamana.html')
def MAMACITA(request):
    return render(request, 'wiki/MAMACITA.html')