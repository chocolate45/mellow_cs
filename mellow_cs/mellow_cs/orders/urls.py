# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.core.urlresolvers import reverse, reverse_lazy

from . import views


urlpatterns = [
    # Order patterns
    url(
        regex=r'^$',
        view=views.OrderListView.as_view(),
        name='order_list',
    ),
    url(
        regex=r'^(?P<pk>[\d+-]+)/$',
        view=views.OrderDetailView.as_view(),
        name='order_detail',
    ),
    url(
        regex=r'^~import/$',
        view=views.Foo.as_view(),
        name='order_fetch',
    ),
]
