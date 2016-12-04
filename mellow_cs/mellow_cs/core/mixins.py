# -*- coding: utf-8 -*-
import csv

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from mellow_cs.orders.models import Order


class ImportCsvMixin(object):

    def import_csv():
        try:
            with open('Export Orders-2016-11-30--21-08-07.csv',
                      newline='',
                      encoding='utf-8') as f:
                        reader = csv.reader(f)
                        for row in reader:
                            Order.objects.create(
                                order_nr=row[0],
                                user_email=row[1],
                                user_bill_firstname=row[2],
                                user_bill_lastname=row[3],
                                order_date=row[4],
                                order_payment=row[5],
                                order_total=row[6],
                                voucher_discount=row[7],
                                voucher_nr=row[8],
                                article_nr=row[9],
                                article_title=row[10],
                                article_quantity=row[11],
                                article_price=row[12],
                                country_title=row[13],
                                order_delivery_cost=row[14],
                                user_address=row[15],
                                user_bill_street=row[16],
                                user_bill_street_nr=row[17],
                                user_bill_zipcode=row[18],
                                user_bill_city=row[19],
                                user_delivery_firstname=row[20],
                                user_delivery_lastname=row[21],
                                user_delivery_street=row[22],
                                user_delivery_street_nr=row[23],
                                user_delivery_zipcode=row[24],
                                user_delivery_city=row[25],
                                status=row[26]
                            )
            return True
        except:
            return False

    # def import_failed():
    #     msg = "Import Failed"
    #     return msg

    def dispatch(self, request, *args, **kwargs):
        # if not self.import_csv:
        #     return self.member_check_failed(request, *args, **kwargs)
        return super(ImportCsvMixin, self).dispatch(request, *args, **kwargs)

# class CheckMembershipMixin(object):
#     failure_path = ''  # should be namespace
#     org = None

#     def get_org(self):
#         org = Org.objects.get(slug=self.kwargs['org'])
#         return org

#     def is_member(self, user, org):
#         return True

#     def member_check_failed(self, request, *args, **kwargs):
#         return HttpResponseRedirect(reverse(
#             self.failure_path,
#             kwargs={'org': self.kwargs['org']}
#         ))

#     def dispatch(self, request, *args, **kwargs):
#         if not self.is_member(user=self.request.user, org=self.org):
#             return self.member_check_failed(request, *args, **kwargs)
#         return super(CheckMembershipMixin, self).dispatch(request, *args, **kwargs)


# class AdminRequiredMixin(CheckMembershipMixin):

#     def is_admin(self, user, org):
#         return True


class ActionMixin(object):

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super().form_valid(form)

    def member_check_failed(self, request, *args, **kwargs):
        messages.info(self.request, self.success_msg)
        return super().member_check_failed(request, *args, **kwargs)
