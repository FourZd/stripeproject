# StripeTestProject
This is a job test project using Django+Stripe

❗ You have to use Docker compose ❗

1. Open terminal
2. Open stripeproject folder
3. Type ```docker compose up```
4. The server is working now. Endpoints are below,


Available pages:

![image](https://user-images.githubusercontent.com/91225680/191079931-6e2d8b17-7980-48dd-8710-7465a133b251.png)

admin/ - admin page, use it to create items and orders
item/<int:pk>/ - Item landing
order/<int:pk>/ [name='order'] - Order landing (you can set up orders in admin)
buy/<int:pk>/ [name='buy'] - Create Checkout Session Page, it responds with session ID
order-buy/<int:pk>/ [name='order-buy'] Create Order Checkout Session Page, it responds with session ID
success/ - Success redirect page
cancel/ - Cancel redirect page
