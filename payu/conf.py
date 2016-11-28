# coding=utf-8
#
# Copyright 2012-2016 PressLabs SRL
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
from django.conf import settings

TEST = getattr(settings, "PAYU_TEST", True)


MERCHANT = settings.PAYU_MERCHANT
MERCHANT_KEY = settings.PAYU_KEY


PAYU_ORDER_DETAILS = ['PNAME', 'PGROUP', 'PCODE', 'PINFO', 'PRICE', 'PRICE_TYPE',
                      'QTY', 'VAT', 'VER']

PAYU_ORDER_DETAILS_DEFAULTS = {
    'QTY': 1,
    'VAT': 24
}

PAYU_DATE_FORMATS = (
    '%Y-%m-%d %H:%M:%S'
)

PAYU_CURRENCIES = (
    ('USD', 'USD'),
    ('RON', 'RON'),
    ('EUR', 'EUR')
)

PAYU_PAYMENT_METHODS = (
    ('CCVISAMC', 'VISA/Mastercard Card'),
    ('CCAMEX', 'AMEX Card'),
    ('CCDINERS', 'Diners Club Card'),
    ('CCJCB', 'JCB Card'),
    ('WIRE', 'Bank Wire'),
    ('PAYPAL', 'PayPal')
)

PAYU_LANGUAGES = (
    ('RO', u'Română'),
    ('EN', u'English'),
    ('DE', u'Deutsch'),
    ('ES', u'Español'),
    ('FR', u'Français'),
    ('IT', u'Italiano')
)

PAYU_PAYMENT_STATUS = (
    ('PAYMENT_AUTHORIZED', 'PAYMENT_AUTHORIZED'),
    ('PAYMENT_RECEIVED', 'PAYMENT_RECEIVED'),
    ('TEST', 'TEST'),
    ('CASH', 'CASH'),
    ('COMPLETE', 'COMPLETE'),
    ('REVERSED', 'REVERSED'),
    ('REFUND', 'REFUND')
)