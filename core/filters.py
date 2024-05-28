import django_filters
from core import models


# class News(django_filters.FilterSet):
#     title = django_filters.CharFilter(label='Название', lookup_expr='icontains')
#     created_to = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', label='Новости до')
#
#
#
#     class Meta:
#         model = models.News
#         fields = ('title', 'category', )
        # exclude = ('photo', )
