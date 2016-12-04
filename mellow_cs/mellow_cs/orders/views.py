# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import (DetailView, ListView, RedirectView,
                                  UpdateView, CreateView, TemplateView)

from django.contrib.auth.mixins import LoginRequiredMixin

from mellow_cs.core.mixins import ImportCsvMixin
from .models import Order
# from .models import Project, Document
# from .forms import (ProjectCreateForm, ProjectUpdateForm, DocumentCreateForm,
#                     DocumentUpdateForm)
# from vales.core.mixins import CheckMembershipMixin, AdminRequiredMixin, ActionMixin


class OrderListView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        # Fetch the queryset from the parent get_queryset
        queryset = super(OrderListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")
        if q:
            # Return a filtered queryset
            order_nr_set = queryset.filter(order_nr__iexact=q)
            email_set = queryset.filter(user_email__icontains=q)
            firstname_set = queryset.filter(user_bill_firstname__icontains=q)
            lastname_set = queryset.filter(user_bill_lastname__icontains=q)
            queryset = order_nr_set | email_set | firstname_set | lastname_set
            return queryset
        # Return the base queryset
        return queryset


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order


class Foo(LoginRequiredMixin, ImportCsvMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('orders:order_list')






