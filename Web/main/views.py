from django.shortcuts import render, redirect
from .models import vote
from .forms import voteForms
from django.views.generic import DetailView


def index(request):
    data= {
        'title': 'Главная страница',
}
    return render(request,'main/main.html',data)


def about(request):
    return render(request,'main/about.html')

def contacts(request):
    return render(request,'main/contacts.html')

def polls(request):
    polls = vote.objects.order_by('name')
    return render(request,'main/polls.html',{'polls': polls})

def create(request):
    return render(request, 'main/create.html')

def create(request):
    error =''
    if request.method == 'POST':
        form = voteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls')
        else:
            error= 'Ошибка ввода'

    form = voteForms()

    data ={
        'form': form,
        'error': error
    }

    return render(request, 'main/create.html', data)

def details_view(request):
    return render(request,'main/details_view.html')

class VoteDetailView(DetailView):
    model = vote
    template_name = 'main/details_view.html'
    context_object_name = 'vote'