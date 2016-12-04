# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mellow_cs.core.models import TimeStampedModel

# class Product(models.Model):
#     Battery-Pack
#     Fast Charger
#     Front Truck
#     Front Wheels
#     Mellow Board
#     Mellow Board 4x4
#     Mellow Drive
#     Mellow Drive 4x4
#     Mellow Remote


#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = 'SR'
#     YEAR_IN_SCHOOL_CHOICES = (
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#     )


class Order(TimeStampedModel):

    order_nr = models.IntegerField()
    user_email = models.EmailField()
    user_bill_firstname = models.CharField(max_length=250)
    user_bill_lastname = models.CharField(max_length=250)
    order_date = models.DateTimeField()
    order_payment = models.CharField(max_length=250)
    order_total = models.DecimalField(max_digits=7, decimal_places=2)
    voucher_discount = models.DecimalField(
        max_digits=7, decimal_places=2,
        default=0.00
    )
    voucher_nr = models.CharField(blank=True, max_length=250)
    article_nr = models.CharField(blank=True, max_length=250)
    article_title = models.CharField(max_length=250)
    article_quantity = models.IntegerField()
    article_price = models.DecimalField(max_digits=7, decimal_places=2)
    country_title = models.CharField(max_length=250)
    order_delivery_cost = models.DecimalField(max_digits=7, decimal_places=2)
    user_address = models.CharField(max_length=250)
    user_bill_street = models.CharField(max_length=250)
    user_bill_street_nr = models.CharField(max_length=250)
    user_bill_zipcode = models.CharField(max_length=250)
    user_bill_city = models.CharField(max_length=250)
    user_delivery_firstname = models.CharField(blank=True, max_length=250)
    user_delivery_lastname = models.CharField(blank=True, max_length=250)
    user_delivery_street = models.CharField(blank=True, max_length=250)
    user_delivery_street_nr = models.CharField(blank=True, max_length=250)
    user_delivery_zipcode = models.CharField(blank=True, max_length=250)
    user_delivery_city = models.CharField(blank=True, max_length=250)
    status = models.CharField(max_length=250)

    class Meta:
        get_latest_by = 'order_date'
        ordering = ['-order_date']

    def __str__(self):
        return self.user_email

    def get_absolute_url(self):
        return reverse(
            'orders:ororder_detail',
            kwargs={
                'pk': self.pk,
            }
        )
