from django.shortcuts import render, redirect
from .models import Students
def index(request):
    user_name=request.GET.get('name')
    user_class=request.GET.get('Class')
    user_roll_no=request.GET.get('roll_no')
    if user_name and user_class and user_roll_no:
        status="admission done"
        Students.objects.create(name=user_name, Class=user_class, roll_no=user_roll_no, status=status)
    obj=Students.objects.all()
    return render(request, 'index.html',{'objs':obj})

# Created your views here.
def delete(request, id):
    Students.objects.get(id=id).delete()
    return redirect('/')

def update(request, id):
    if request.GET.get('id'):
        user_name=request.GET.get('name')
        user_class=request.GET.get('Class')
        user_roll_no=request.GET.get('roll_no')
        if user_name and user_class and user_roll_no:
            obj=Students.objects.get(id=request.GET.get('id'))
            obj.name=user_name
            obj.Class=user_class
            obj.roll_no=user_roll_no
            obj.save()
    scl=Students.objects.get(id=id)
    return render(request, 'update.html', {'scl':scl})
