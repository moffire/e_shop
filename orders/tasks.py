from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    # send mail after successful order
    order = Order.objects.get(id=order_id)
    subject = 'Order №{0} '.format(order.id)
    message = f'Dear {order.first_name}\n\nYour order number is {order_id}'
    mail_sent = send_mail(subject, message, 'shop@mail.ru', ['client@mail.ru'])
    return mail_sent