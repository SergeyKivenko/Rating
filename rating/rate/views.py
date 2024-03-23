from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import Rating
from .forms import SimpleForm



class SimpleFormView(View):
    form_class = SimpleForm
    initial = {'foo': 'initial value'}
    template_name = 'rate/form_template.html'

    def get(self, request, *args, **kwargs):
# *args - КАРТЕЖ неименновонных аргументов функции
# **kwargs - СЛОВАРЬ именнованных аргумнентов функции
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('main'))
        
        return render(request, self.template_name, {'form': form})



class RatingsListView(ListView):
    model = Rating
    template_name = "rate/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["key"] = "key"
        return context


class SimpleView(View):
    name = 'Anonymous'

    def get(self, request):
        return HttpResponse(f'Hello, {self.name}')