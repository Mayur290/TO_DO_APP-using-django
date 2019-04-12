from django.http import  HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from app.models import TodoItem

def fire(request):
    return render(request,"first.html",{})

def jaiho(request):
    return HttpResponseRedirect('/first/')
    
def home_page(request):
    all_todo_items = TodoItem.objects.all()
    context={
        "title":"to do app",
        "content" : "TO DO APP",
        "all_items": all_todo_items,
    }
    return render(request,"home.html",context)

def add(request):
    new_item = TodoItem(content = request.POST['fullname'])
    new_item.save()
    return HttpResponseRedirect('/first/')

def delete(request ,pk=None ,  *args, **kwargs):
    item_to_delete = TodoItem.objects.get(pk=pk)
    item_to_delete.delete()
    return HttpResponseRedirect('/first/')