from django.shortcuts import render, redirect
from .models import Gem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Gem
from .forms import PolishingForm


from django.http import HttpResponse

def home(request):

  return render(request, 'home.html')

def about(request):

  return render(request, 'about.html')





@login_required
def gems_index(request):

  gems = Gem.objects.filter(user=request.user)
  return render(request, 'gems/index.html', { 'gems': gems})


@login_required
def gems_detail(request, gem_id):
  gem = Gem.objects.get(id=gem_id)
  polishing_form = PolishingForm()
  return render(request, 'gems/detail.html', {
    'gem': gem, 'polishing_form': polishing_form
  })

@login_required
def add_polishing(request, gem_id):
  form = PolishingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_polishing = form.save(commit=False)
    new_polishing.gem_id = gem_id
    new_polishing.save()
  return redirect('detail', gem_id=gem_id)



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  

class GemCreate(LoginRequiredMixin, CreateView):
  model = Gem
  fields = ['name', 'crystal_system', 'color', 'hardness', 'specific_gravity']
  success_url = '/gems/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GemUpdate(LoginRequiredMixin, UpdateView):
  model = Gem
  fields = ['crystal_system', 'color', 'hardness', 'specific_gravity']

class GemDelete(LoginRequiredMixin, DeleteView):
  model = Gem
  success_url = '/gems/'