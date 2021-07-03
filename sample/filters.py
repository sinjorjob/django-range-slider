import django_filters
from .models import Member
from django_filters import FilterSet
from django_filters.filters import RangeFilter
from .models import Member
from .forms import MemberFilterFormHelper
from .widgets import CustomRangeWidget

class AllRangeFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [p.age for p in Member.objects.all()]
        min_value = min(values)
        max_value = max(values)
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})


#class MemberFilter(django_filters.FilterSet):

  #age = django_filters.AllValuesFilter()
#  age = django_filters.RangeFilter(
#        widget=django_filters.widgets.RangeWidget(attrs={'placeholder': '年齢を入力'}))
#  class Meta:
#      model = Member
#      fields = ['age']

class MemberFilter(FilterSet):
  age = AllRangeFilter()

  class Meta:
      model = Member
      fields = ['age']
      form = MemberFilterFormHelper