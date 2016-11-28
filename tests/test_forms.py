import pytest

from payu.forms import PayULiveUpdateForm, ValueHiddenInput


@pytest.mark.parametrize("payload,signature", [
    ({
        'ORDER_REF': 112457,
        'ORDER_DATE': '2012-05-01 15:51:35',
        'ORDER': [
            {
                'PNAME': 'MacBook Air 13 inch',
                'PCODE': 'MBA13',
                'PINFO': 'Extended Warranty - 5 Years',
                'PRICE': 1750,
                'PRICE_TYPE': 'GROSS',
                'QTY': 1,
                'VAT': 24
            },
        ],
        'BILL_FNAME': 'Joe',
        'BILL_LNAME': 'Doe',
        'BILL_COUNTRYCODE': 'RO',
        'BILL_PHONE': '+040000000000',
        'BILL_EMAIL': 'joe.doe@gmail.com',
        'BILL_COMPANY': 'ACME Inc',
        'BILL_FISCALCODE': None,
        'PRICES_CURRENCY': 'RON',
        'CURRENCY': 'RON',
        'PAY_METHOD': 'CCVISAMC'
    }, '5b118e083e52a24872f579134c5db6cc'),
    ({
        'ORDER_REF': 112457,
        'ORDER_DATE': '2012-05-01 15:51:35',
        'ORDER': [
            {
                'PNAME': 'MacBook Air 13 inch',
                'PCODE': 'MBA13',
                'PINFO': '',
                'PRICE': 1750,
                'PRICE_TYPE': 'GROSS',
                'QTY': 1,
                'VAT': 24
            },
        ],
        'BILL_FNAME': 'Joe',
        'BILL_LNAME': 'Doe',
        'BILL_COUNTRYCODE': 'RO',
        'BILL_PHONE': '+040000000000',
        'BILL_EMAIL': 'joe.doe@gmail.com',
        'BILL_COMPANY': 'ACME Inc',
        'BILL_FISCALCODE': None,
        'PRICES_CURRENCY': 'RON',
        'CURRENCY': 'RON',
        'LANGUAGE': 'RO',
        'TEST': True,
        'PAY_METHOD': 'CCVISAMC'
    }, 'e327589caadf200996521a4d0b433ef5'),
    ({
        'ORDER_REF': '789456123',
        'ORDER_DATE': '2016-10-05 11:12:27',
        'ORDER': [
            {
                'PNAME': 'CD Player',
                'PCODE': 'PROD_04891',
                'PINFO': 'Extended Warranty - 5 Years',
                'PRICE': '82.3',
                'PRICE_TYPE': 'GROSS',
                'QTY': '7',
                'VAT':'20'
            },
            {
                'PNAME': 'Mobile Phone',
                'PCODE': 'PROD_07409',
                'PINFO': 'Dual SIM',
                'PRICE': '1945.75',
                'PRICE_TYPE': 'GROSS',
                'QTY': '3',
                'VAT':'20'
            },
            {
                'PNAME': 'Laptop',
                'PCODE': 'PROD_04965',
                'PINFO': '17" Display',
                'PRICE': '5230',
                'PRICE_TYPE': 'GROSS',
                'QTY': '1',
                'VAT':'20'
            },
        ],
        'PRICES_CURRENCY': 'RON',
        'ORDER_SHIPPING': '0',
        'DISCOUNT': '55',
        'PAY_METHOD': 'CCVISAMC',
        'DESTINATION_CITY': 'Bucuresti',
        'DESTINATION_STATE': 'Bucuresti',
        'DESTINATION_COUNTRY': 'RO',
        'TESTORDER': 'TRUE',
        'BILL_FNAME': 'Joe',
        'BILL_LNAME': 'Doe',
        'BILL_COUNTRYCODE': 'RO',
        'BILL_PHONE': '+040000000000',
        'BILL_EMAIL': 'joe.doe@gmail.com',
    }, 'a9b838e17a04cc045699e5501f8f12c6')
])
def test_calculate_correct_hash(payload, signature):
    payu_form = PayULiveUpdateForm(initial=payload)
    assert payu_form.signature == signature
    assert payu_form.fields['ORDER_HASH'].initial == signature


@pytest.mark.parametrize("payload,orders", [
    ({
        'ORDER': [
            {
                'PNAME': 'MacBook Air 13 inch',
                'PCODE': 'MBA13',
                'PINFO': 'Extended Warranty - 5 Years',
                'PRICE': 1750,
                'PRICE_TYPE': 'GROSS',
                'QTY': 1,
                'VAT': 24
            },
        ],
    }, [{
        'VER': None,
        'PRICE_TYPE': 'GROSS',
        'PRICE': 1750,
        'QTY': 1,
        'PINFO': 'Extended Warranty - 5 Years',
        'PCODE': 'MBA13',
        'PNAME': 'MacBook Air 13 inch',
        'PGROUP': None,
        'VAT': 24
    }]),
    ({
        'ORDER': [
            {
                'PNAME': 'MacBook Air 13 inch',
                'PCODE': 'MBA13',
                'PRICE': 1750,
                'PRICE_TYPE': 'GROSS',
            },
        ],
    }, [{
        'VER': None,
        'PRICE_TYPE': 'GROSS',
        'PRICE': 1750,
        'QTY': 1,
        'PINFO': None,
        'PCODE': 'MBA13',
        'PNAME': 'MacBook Air 13 inch',
        'PGROUP': None,
        'VAT': 24
    }])
])
def test_orders_parsing(payload, orders):
    payu_form = PayULiveUpdateForm(initial=payload)
    assert payu_form._prepare_orders(payload['ORDER']) == orders


@pytest.mark.parametrize("field,html", [
    (ValueHiddenInput().render('name', None), ''),
    (ValueHiddenInput().render('name', ''), '<input name="name" type="hidden" />'),
    (ValueHiddenInput().render('name', 'value'), '<input name="name" type="hidden" value="value" />'),
    (ValueHiddenInput().render('ORDER_10_0', 'a'), '<input name="ORDER_PNAME[]" type="hidden" value="a" />'),
    (ValueHiddenInput().render('ORDER_10_10', 'a'), '<input name="ORDER_10_10" type="hidden" value="a" />'),
])
def test_value_input_hidden(field, html):
    assert field == html