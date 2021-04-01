from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import BlogModel,AnimeModel,RamennModel
from django.urls import reverse_lazy

class BlogList(ListView):
    template_name = 'home.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogTopic(ListView):
    template_name = "topic.html"
    model = BlogModel

    def get(self, request, *args, **kwargs):
        parameter = self.kwargs.get('parameter')
        if parameter:
            request.session['parameter'] =parameter
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parameter = self.request.session.pop('parameter', None)
        if parameter:
            context['parameter'] =parameter
        return context

# def topicview(request):
#     data = {'topic' :request.GET.get('item')}
#     return render(request, 'topic.html', data)

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ( 'title', 'content', 'category')
    success_url = reverse_lazy('home')

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('home')

class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ( 'title', 'content', 'category')
    success_url = reverse_lazy('home')

def indexview(request):
    return render(request, 'index.html')

def skillview(request):
    return render(request, 'skill.html')

class BlogAnime(ListView):
    template_name = 'anime.html'
    model = AnimeModel

def sportview(request):
    return render(request, 'sport.html')

def pdfview(request):
    return render(request, 'pdf.html')

class BlogMath(ListView):
    template_name = 'math.html'
    model = BlogModel

class BlogFood(ListView):
    template_name = 'food.html'
    model = RamennModel