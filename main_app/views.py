from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  # return HttpResponse('<h1>Homepage</h1>')
  return render(request, 'home.html')

def about(request):
  # return HttpResponse('<h1>About the gem collector</h1>')
  return render(request, 'about.html')



class Gem: 
  def __init__(self, name, crystal_system, color, hardness, specific_gravity):
    self.name = name
    self.crystal_system = crystal_system
    self.color = color
    self.hardness = hardness
    self.specific_gravity = specific_gravity

gems = [
  Gem('Diamond', 'Cubic', 'white to black, colorless, yellow, pink, red, blue, brown', 10, '3.4-3.5'),
  Gem('Ruby', 'Hexagonal-trigonal', 'red', 9, '4.0-4.1'),
  Gem('Sapphire', 'Hexagonal-trigonal', 'occurs in most colors', 9, '4.0-4.1'),
  Gem('Zircon', 'Tetragonal', 'colorless, brown, red, yellow, orange, blue, green', 7.5, '4.6-4.7')
]
def gems_index(request):
  # return HttpResponse('<h1>About the gem collector</h1>')
  return render(request, 'gems/index.html', { 'gems': gems})