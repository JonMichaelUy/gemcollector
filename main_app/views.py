from django.shortcuts import render, redirect
from .models import Gem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Gem
from .forms import PolishingForm

# Create your views here.
from django.http import HttpResponse

def home(request):
  # return HttpResponse('<h1>Homepage</h1>')
  return render(request, 'home.html')

def about(request):
  # return HttpResponse('<h1>About the gem collector</h1>')
  return render(request, 'about.html')



# class Gem: 
#   def __init__(self, name, crystal_system, color, hardness, specific_gravity):
#     self.name = name
#     self.crystal_system = crystal_system
#     self.color = color
#     self.hardness = hardness
#     self.specific_gravity = specific_gravity

# gems = [
#   Gem('Diamond', 'Cubic', 'white to black, colorless, yellow, pink, red, blue, brown', 10, '3.4-3.5'),
#   Gem('Ruby', 'Hexagonal-trigonal', 'red', 9, '4.0-4.1'),
#   Gem('Sapphire', 'Hexagonal-trigonal', 'occurs in most colors', 9, '4.0-4.1'),
#   Gem('Zircon', 'Tetragonal', 'colorless, brown, red, yellow, orange, blue, green', 7.5, '4.6-4.7')
# ]

def gems_index(request):
  # return HttpResponse('<h1>About the gem collector</h1>')
  gems = Gem.objects.all()
  return render(request, 'gems/index.html', { 'gems': gems})



def gems_detail(request, gem_id):
  gem = Gem.objects.get(id=gem_id)
  polishing_form = PolishingForm()
  return render(request, 'gems/detail.html', {
    'gem': gem, 'polishing_form': polishing_form
  })


def add_polishing(request, gem_id):
  form = PolishingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_polishing = form.save(commit=False)
    new_polishing.gem_id = gem_id
    new_polishing.save()
  return redirect('detail', gem_id=gem_id)

class GemCreate(CreateView):
  model = Gem
  fields = '__all__'
  success_url = '/gems/'


class GemUpdate(UpdateView):
  model = Gem
  fields = ['crystal_system', 'color', 'hardness', 'specific_gravity']

class GemDelete(DeleteView):
  model = Gem
  success_url = '/gems/'