from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.files.storage import FileSystemStorage


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
    return render(request, 'request_app/user-form.html')

def upload_file(request):
    too_much = False
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        if fs.size <= 1048576:
            filename = fs.save(myfile.name, myfile)
            print('сохранили файл:', filename)
        else:
            too_much = True
    context = {
        'too_much': too_much
    }
    return render(request, 'request_app/file_upload.html', context=context)
