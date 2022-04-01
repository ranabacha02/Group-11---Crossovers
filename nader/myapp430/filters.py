from . models import ShopItem
import django_filters
from django_filters.filters import RangeFilter

class ShopFilter(django_filters.FilterSet):

	price = django_filters.NumberFilter()
	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
	# date_created = django_filters.NumberFilter(field_name='date_created', lookup_expr='year')
    
	date_created = django_filters.NumberFilter(field_name='date_created', lookup_expr='gt')
	date_created = django_filters.NumberFilter(field_name='date_created', lookup_expr='lt')

	# date_created__gt = django_filters.NumberFilter(field_name='date_created', lookup_expr='year__gt')
    
	# date_created__lt = django_filters.NumberFilter(field_name='date_created', lookup_expr='year__lt')

	category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')
	name = django_filters.CharFilter(lookup_expr='icontains')
    
    # price = RangeFilter()

	class Meta:
		model = ShopItem
		fields = {
			'price': ['lt', 'gt'],
			# 'date_created': ['year_lt', 'year__gt'],
			'date_created': ['gt', 'lt'],
			'category': ['exact'],
            'name': ['icontains']
		}

	
