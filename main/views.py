from django.shortcuts import render,redirect
from .models import ToDoList,Item
from .forms import createListForm

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request,"main/home.html",{})
    else:
        return redirect('login')


def lists(request,id):
    if request.user.is_authenticated:
        ls = ToDoList.objects.get(id=id)
        if request.method == "POST":
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    if request.POST.get("c{}".format(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
                return redirect("/lists/{}".format(id))
            
            elif request.POST.get("newItem"):
                text = request.POST.get("new")
                ls.item_set.create(text = text,complete =False)
                return redirect("/lists/{}".format(id))
                
        elif request.method == "GET":
            title = ToDoList.objects.get(id=id)
            if title in request.user.todolist.all():
                print(type(title))
                item = title.item_set.all()
                return render(request,"main/lists.html",{"name" : title,"content" : item})
            else:
                return redirect('/lists-view')
            
    else:
        return redirect('login')
    
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = createListForm(request.POST)
            if form.is_valid():
                listTitle = form.cleaned_data["title"]
                listId = form.cleaned_data["id"]
                newList = ToDoList(title=listTitle,id=listId)
                newList.save()
                request.user.todolist.add(newList)
                return redirect("/")
        elif request.method == "GET":
            form = createListForm()
            return render(request,"main/create-list.html",{"form":form})
    else:
        return redirect('login')       

def viewUserLists(request):
    if request.user.is_authenticated:
        return render(request,"main/lists-view.html",{})
    else:
        return redirect('login')
