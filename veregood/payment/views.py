
from django.http import HttpResponse
from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_checkout_session(request, id):

    # request_data = json.loads(request.body)
    # product = get_object_or_404(Product, pk=id)

    stripe.api_key = settings.STRIPE_SECRECT_KEY
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        customer_email = "dextern@aaitpro.com",
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                    'name': id,
                    },
                    'unit_amount': int(500* 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('payment:success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('payment:failure')),
    )

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )


 

    # return JsonResponse({'data': checkout_session})
    return render(request,"payment/start.html",{'sessionId': checkout_session.id,"stripe_public_key":settings.STRIPE_PUBLIC_KEY})
    


class PaymentSuccessView(TemplateView):
    template_name = "payments/payment_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(OrderDetail, stripe_payment_intent=session.payment_intent)
        order.has_paid = True
        order.save()
        return render(request, self.template_name)

class PaymentFailedView(TemplateView):
    template_name = "payments/payment_failed.html"

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRECT
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRECT
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        order = Order.objects.get(payment_id=payload["payment_id"])
        order.paid = True
        order.save()
        cart = Cart.objects.get(user=order.user)
        cart.user = None
        cart.save()

    return HttpResponse(status=200)


