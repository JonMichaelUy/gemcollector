from django.db import models
from django.urls import reverse
from datetime import date


CLEANERS = (
  ('C', 'Cloth'),
  ('S', 'Silica'),
  ('A', 'Ammonia')
)
# Create your models here.


class Gem(models.Model):
  name = models.CharField(max_length=100)
  crystal_system = models.CharField(max_length=100)
  color = models.TextField(max_length=250)
  hardness = models.IntegerField()
  specific_gravity = models.CharField(max_length=100)

  def polished_for_today(self):
    return self.polishing_set.filter(date=date.today()).count() >= 1
    
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'gem_id': self.id})



class Polishing(models.Model):
  date = models.DateField('date polished')
  cleaner = models.CharField(
    max_length=1,
    choices=CLEANERS,
    default=CLEANERS[0][0]
  )
  gem = models.ForeignKey(Gem, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_cleaner_display()} on {self.date}"
  class Meta:
    ordering = ['-date']
