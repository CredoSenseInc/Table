from django.shortcuts import render,redirect
from .models import Table
from .forms import TableForm

# Create your views here.


def tableList(request):
    tables = Table.objects.all()
    return render(request, 'table-list.html', {'tables':tables})


def tableCreate(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('table-list')
            except:
                pass

    else:
        form = TableForm()
    return render(request, 'table-create.html', {'form':form})


def tableUpdate(request, id):
    table = Table.objects.get(id=id)
    form = TableForm(initial={'s_1' : table.s_1, 's_2' : table.s_2, 's_3' : table.s_3, 'time_date' : table.time_date})
    if request.method  == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/table-list')
            except Exception as e:
                pass
    return render(request, 'table-update.html', {'form':form})
def tableDelete(request, id):
    table = Table.objects.get(id=id)
    try:
        table.delete()
    except:
        pass
    return redirect('table-list')
