from django.urls import path
from .views import *

urlpatterns = [
    path('item/<int:pk>/', ProductLandingPageView.as_view(), name='item'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('order/<int:pk>/', OrderLandingPageView.as_view(), name='order'),
    path('order-buy/<int:pk>/', CreateOrderCheckoutSessionView.as_view(), name='order-buy'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel')
]
