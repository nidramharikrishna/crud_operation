from django.shortcuts import render,redirect,get_object_or_404
from appz.models import student
from appz.forms import stu_forms

def stu_read(request):
    stu=student.objects.all()
    return render(request,'stu_list.html',{'stu':stu})

def stu_create(request):
    
    if request.method == 'POST':
        form = stu_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stu_list')
    else:
        form=stu_forms()
    
    return render(request, 'stu_form.html', {'form': form})  


def stu_update(request,id):
    stu=get_object_or_404(student, id=id)
    form = stu_forms(request.POST or None, instance=stu)
    if form.is_valid():
        form.save()
        return redirect('stu_list')
    return render(request,'stu_form.html',{'form':form})

def stu_delete(request,id):
    stu=get_object_or_404(student, id=id)
    stu.delete()
    return redirect('stu_list')
