import datetime
import os
from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'
    path = settings.FILES_PATH
    file_list = os.listdir(path)
    content = []
    #mtime = path.stat().st_mtime
    #timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

    for i in file_list:
        file = os.path.join(path, i)
        get_file_ctime = os.stat(file).st_ctime
        get_file_mtime = os.stat(file).st_mtime
        date_create_file = datetime.datetime.fromtimestamp(get_file_ctime)
        date_modify_file = datetime.datetime.fromtimestamp(get_file_mtime)
        content.append({'name': i, 'ctime': date_create_file, 'mtime': date_modify_file})

    context = {
        'files': content,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = settings.FILES_PATH
    file = os.path.join(path, name)
    content = ''

    with open(file, 'r') as file:
        content = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

