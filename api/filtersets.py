from django_filters import rest_framework as filters
from api.models import Transaction

class TransactionFilterSet(filters.FilterSet):
    date = filters.DateFilter(field_name="datetime", lookup_expr="date", label= 'Transaction date')
    date__lt = filters.DateFilter(field_name="datetime", lookup_expr="date__lt", label= 'Transactions before date')
    date__gt = filters.DateFilter(field_name="datetime", lookup_expr="date__gt", label= 'Transactions after date')
    time = filters.TimeFilter(field_name="datetime", lookup_expr="time", label= 'Transaction time')
    time__lt = filters.TimeFilter(field_name="datetime", lookup_expr="time__lt", label= 'Transaction time is less than')
    time__gt = filters.TimeFilter(field_name="datetime", lookup_expr="time__gt", label= 'Transaction date is greater than')
    datetime__lt = filters.DateTimeFilter(field_name="datetime", lookup_expr="lt", label= 'Transactions before date and time')
    datetime__gt = filters.DateTimeFilter(field_name="datetime", lookup_expr="gt", label= 'Transactions after date and time')
    
    class Meta:
        model = Transaction
        fields = {
            'money_amount': ['exact', 'lt', 'gt'],
        }
        