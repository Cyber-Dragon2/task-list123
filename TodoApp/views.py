from django.shortcuts import render
from .models import TodoItems
from time import strftime
# Create your views here.
def home(request):
    if request.method == 'POST':
        if 'TodoTitle' in request.POST:
            title = request.POST['TodoTitle']
            date = strftime('%d/%m/%y')
            if title != '':
                print(f"Title: {title}\nDate: {date}")
                storage = TodoItems(TodoTitle = title, TodoDate = date )
                storage.save()
            else:
                print("Data was empty")
        
        else:
            ID = request.POST['del']
            
            storage = TodoItems.objects.filter(id=ID)
            print(f"Id = {ID}\n Data = {str(storage.first())}")
            storage.delete()
    items = TodoItems.objects.all()
    content = {'list_items' : items}

    return render(request,'home.html',content)