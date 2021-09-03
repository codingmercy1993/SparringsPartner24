import django_filters
from .models import FighterProfile

class AgeFilter(django_filters.FilterSet):
  weight = django_filters.AllValuesFilter()

  class Meta:
      model = FighterProfile
      fields = ['weight']