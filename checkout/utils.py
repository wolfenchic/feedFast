from django.shortcuts import get_object_or_404
from .models import OrderLineItem
from restaurants.models import Restaurant, Menu, Menu_item
import stripe
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from cart.utils import get_cart_items_and_total

stripe.api_key = settings.STRIPE_SECRET

def save_order_items(order, cart):
    for id, quantity in cart.items():
        menu_item = get_object_or_404(Menu_item, pk=id)
        order_line_item = OrderLineItem(
            order = order,
            menu_item = menu_item,
            quantity = quantity
            )
        order_line_item.save()
        
def charge_card(stripe_token, total):
    total_in_cent = int(total*100)
    return stripe.Charge.create(
        amount=total_in_cent,
        currency="EUR",
        description="Dummy Transaction",
        card=stripe_token,
    )

def send_confirmation_email(email, username, cart_items_and_total):
    context = {
        'site_name': "Blah Blah dot com",
        'user': username,
    }
    context.update(cart_items_and_total)
    message = render_to_string('checkout/text_confirmation_email.html', context)
    html_message = render_to_string('checkout/html_confirmation_email.html', context)
                
    subject = 'Thanks for buying our stuff!'
    message = message
    from_email = settings.SYSTEM_EMAIL
    to_email = [email]
    
    send_mail(subject,message,from_email,to_email,fail_silently=True,html_message=html_message)