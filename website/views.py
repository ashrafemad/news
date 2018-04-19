from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from website.models import New, Category


class Home(ListView):
    template_name = 'index.html'
    model = New

    def get_queryset(self):
        queryset = queryset = New.objects.filter(published=True).order_by('-priority', '-date')
        if self.request.GET.get('category'):
            try:
                category = Category.objects.get(title=self.request.GET.get('category'))
                queryset = New.objects.filter(category=category.pk).order_by('-priority', '-date')
            except:
                queryset = queryset = New.objects.filter(published=True).order_by('-priority', '-date')
        elif self.request.GET.get('search'):
            queryset = New.objects.filter(content__icontains=self.request.GET.get('search')).order_by('-priority', '-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ViewNew(DetailView):
    template_name = 'single.html'
    model = New


    def get_context_data(self, **kwargs):
        context = super(ViewNew, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        try:
            context['next'] = New.objects.filter(id__gt=self.object.id).order_by('id')[0]
        except:
            context['next'] = New.objects.last()
        try:
            context['prev'] = New.objects.filter(id__lt=self.object.id).order_by('-id')[0]
        except:
            context['prev'] = New.objects.first()
        return context


def switch_language(request, lang):
    request.session['lang'] = lang
    return redirect('/')

