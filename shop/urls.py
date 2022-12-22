from django.urls import path

from .views import statistics_view, get_filter_options, get_sales_chart, spend_per_customer_chart, payment_success_chart, payment_method_chart

urlpatterns = [
    path('statistics/', statistics_view, name='shop-statistics'),
    path('chart/filter-options/', get_filter_options, name='chart-filter-options'),
    path('chart/sales/<int:year>/', get_sales_chart, name='chart-sales'),
    path('chart/spend-per-customer/<int:year>/', spend_per_customer_chart, name='chart-spend-per-customer'),
    path('chart/payment-success/<int:year>/', payment_success_chart, name='chart-payment-success'),
    path('chart/payment-method/<int:year>/', payment_method_chart, name='chart-payment-method'),
]