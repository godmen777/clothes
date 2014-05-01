# -*- coding: utf-8 -*-
from robokassa.signals import result_received, fail_page_visited
from webshop.checkout.models import Order


def payment_received(sender, **kwargs):
    order = Order.objects.get(id=kwargs['InvId'])
    order.status = Order.PROCESSED
    order.save()

result_received.connect(payment_received)