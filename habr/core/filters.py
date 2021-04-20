# import django_filters


# class ArticleFilter(django_filter.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
    
#     views_more = django_filters.NumberFilter(field_name='views', lookup_expr='gt')
#     views_lexx = django_filters.NumberFilter(field_name='views', lookup_expr='lt')

#     class Meta:
#         model = Article
#         fields = ('vews', 'created_at')