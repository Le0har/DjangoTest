from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm, UserForm


def process_get(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
        'a': a,
        'b': b,
        'result': result
    }
    return render(request, 'request_app/request_query_params.html', context=context)

def user_form(request):
    context = {
        'form': UserForm(),
    }
    return render(request, 'request_app/user-form.html', context=context)

def upload_file(request):
    too_much = False
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # myfile = request.FILES['myfile']
            myfile = form.cleaned_data['file']
            fs = FileSystemStorage()
            if fs.size < 1048576:
                filename = fs.save(myfile.name, myfile)
                print('сохранили файл:', filename)
            else:
                too_much = True
    else:
        form = UploadFileForm()
    context = {
        'too_much': too_much,
        'form': form
    }
    return render(request, 'request_app/file_upload.html', context=context)
