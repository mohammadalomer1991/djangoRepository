
from django.shortcuts import render

# Create your views here.
from core_student_affairs import models, forms


def Index(request):


    context={'name':'hussein',
             'age':26,
             'jobs':['eng', 'dev', 'lecture'],

             }
    return render(request,'index.html',context)

  #return HttpResponse('welcome to index page')

def Register(request):
    form_data = forms.UserRegistrar(request.POST or None)
    msg = ''
    if form_data.is_valid():
        student = models.Student()
        student.first_name = form_data.cleaned_data['first_name']
        student.last_name = form_data.cleaned_data['last_name']
        student.age = form_data.cleaned_data['age']
        student.date_birth = form_data.cleaned_data['date_birth']
        student.save()
        msg = 'data is saved'

    context = {
        'formregister': form_data,
        'msg': msg
    }
    return render(request, 'regiester.html', context)
