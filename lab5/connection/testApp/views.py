from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from testApp.models import Pictures


# Create your views here.

def function_view(request):
    return HttpResponse('response from function view')

class ListPicturesView(ListView):
    model = Pictures
    template_name = 'pictures_list.html'
    def get(self, request):
        data = {
            'pictures': [
                {'name': 'Black square', 'description':'It was painting by Malevich',
                 'place': 'Tretiakov gallery'},
                {'name': 'The starry night', 'description': 'It was painting by van Gogh',
                 'place': 'Museum of Modern Art'},
            ]
        }
        return render(request, 'pictures_list.html', data)
