# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, get_connection
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.


def index(request):

    sms = render_to_string('sendler/letter_template.html', {'name': 'Gabriel', 'date': '01.01.2022',
                                                            'company': 'Hui s gor', 'from_name': 'Ramil'
                                                            })
    send_mail('TestSendlerFromPython 2.7',
              message=sms,
              from_email='hikmatullin_ramil@mail.ru',
              recipient_list=['deviti8411@lance7.com'],
              fail_silently=False)
              # connection=connection)
    return render(request, 'sendler/index.html')

