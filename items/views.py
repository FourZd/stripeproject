import stripe
from .models import Item, Order
from django.views import View
from django.views.generic import DetailView, TemplateView, RedirectView
from django.http import JsonResponse
from urllib.parse import urljoin

stripe.api_key = "sk_test_51LjPvTHAdBUTkVTLbyC8sx6DbsUXuHVAyl8rvdg1EX6GqSiEWz9Omihuolge6D01zBmCn3iElT5llwxdWvFf8NwK00EA192ioL"

class SuccessView(TemplateView):
    template_name = 'items/success.html'

class CancelView(RedirectView):
    url = 'https://youtu.be/dQw4w9WgXcQ'


class ProductLandingPageView(DetailView):
    model = Item
    template_name = 'items/item.html'
    context_object_name = 'item'


class CreateCheckoutSessionView(View): 
    def get(self, request, pk):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)

        checkout_session = stripe.checkout.Session.create(
            success_url= urljoin(YOUR_DOMAIN, "/success"),
            cancel_url= urljoin(YOUR_DOMAIN, "/cancel"),
            mode="payment",
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    "quantity": 1,
                }
            ]
            )
            
        return JsonResponse({
            'id': checkout_session.id   
        })


class OrderLandingPageView(DetailView):
    model = Order
    template_name = 'items/order.html'
    context_object_name = 'order'


class CreateOrderCheckoutSessionView(View): 
    def get(self, request, pk):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        order_id = self.kwargs["pk"]
        order = Order.objects.get(id=order_id)

        checkout_session = stripe.checkout.Session.create(
            success_url= urljoin(YOUR_DOMAIN, "/success"),
            cancel_url= urljoin(YOUR_DOMAIN, "/cancel"),
            mode="payment",
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': order.totalprice,
                        'product_data': {
                            'name': f'Order № {order.pk}'
                        },
                    },
                    "quantity": 1,
                }
            ]
            )
            
        return JsonResponse({
            'id': checkout_session.id   
        })