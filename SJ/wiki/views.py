from django.shortcuts import render, redirect
from wiki.forms import CategoryForm, PageForm
from django.core.urlresolvers import reverse
from wiki.models import Category, Page

def wiki(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'wiki/wiki.html', context)
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
def LeeTeuk(request):
    return render(request, 'wiki/LeeTeuk.html')
def HeeChul(request):
    return render(request, 'wiki/HeeChul.html')
def YeSung(request):
    return render(request, 'wiki/YeSung.html')
def KangIn(request):
    return render(request, 'wiki/KangIn.html')
def ShinDong(request):
    return render(request, 'wiki/ShinDong.html')
def SungMin(request):
    return render(request, 'wiki/SungMin.html')
def EunHyuk(request):
    return render(request, 'wiki/EunHyuk.html')
def SiWon(request):
    return render(request, 'wiki/SiWon.html')
def DongHae(request):
    return render(request, 'wiki/DongHae.html')
def RyeoWook(request):
    return render(request, 'wiki/RyeoWook.html')
def KyuHyun(request):
    return render(request, 'wiki/KyuHyun.html')

def about(request):
    context = {}
    return render(request, 'wiki/about.html', context)

def category(request, categoryID):
    context = {}
    try:
        category = Category.objects.get(id=categoryID)
        context['category'] = category
        context['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
            pass
    return render(request, 'wiki/category.html', context)

def addCategory(request):
    template = 'wiki/addCategory.html'
    if request.method=='GET':
        return render(request, template, {'form':CategoryForm()})
    # request.method=='POST'
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    return redirect(reverse('wiki:wiki'))
    # Or try this: return wiki(request) 

def addPage(request, categoryID):
    template = 'wiki/addPage.html'
    try:
        pageCategory = Category.objects.get(name=categoryID)
    except Category.DoesNotExist:
        return category(request, categoryID)
    context = {'category':pageCategory}
    if request.method=='GET':
        context['form'] = PageForm()
        return render(request, template, context)
    # request.method=='POST'
    form = PageForm(request.POST)
    context['form'] = form
    if not form.is_valid():
        return render(request, template, context)
    page = form.save(commit=False)
    page.category = pageCategory
    page.save()
    return redirect(reverse('wiki:category', args=(categoryID, )))

    
def deleteCategory(request, categoryID):
    if request.method!='POST':
        return wiki(request)
    # request.method=='POST':
    categoryToDelete = Category.objects.get(id=categoryID)
    if categoryToDelete:
        categoryToDelete.delete()
        return redirect(reverse('wiki:wiki'))

    
def deletePage(request, pageID):
    if request.method!='POST':
        return wiki(request)
# request.method=='POST':
    pageToDelete = Page.objects.get(id=pageID)
    if pageToDelete:
        categoryID = pageToDelete.category.id
        pageToDelete.delete()
    else:
        categoryID = ''
    return redirect(reverse('wiki:category', args=(categoryID, )))
    
    
def updateCategory(request, categoryID):
    template = 'wiki/updateCategory.html'
    try:
        category = Category.objects.get(id=categoryID)
    except Category.DoesNotExist:
            return wiki(request)
    if request.method=='GET':
        form = CategoryForm(instance=category)
        return render(request, template, {'form':form, 'category':category})
    # request.method=='POST'
    form = CategoryForm(request.POST, instance=category)
    if not form.is_valid():
        return render(request, template, {'form':form, 'category':category})
    category.save()
    return redirect(reverse('wiki:wiki'))
    
def updatePage(request, pageID):
    template = 'wiki/updatePage.html'
    try:
        page = Page.objects.get(id=pageID)
    except Page.DoesNotExist:
            return category(request, '')
    if request.method=='GET':
        form = PageForm(instance=page)
        return render(request, template, {'form':form, 'page':page})
        # request.method=='POST'
    form = PageForm(request.POST, instance=page)
    if not form.is_valid():
        return render(request, template, {'form':form, 'page':page})
    page.save()
    return redirect(reverse('wiki:category', args=(page.category.id,)))