import csv
from datetime import datetime

from pytz import timezone

from mellow_cs.orders.models import Order

row = ['348', 'mirko.koellmann@web.de', 'Mirko', 'Köllmann', '2015-10-15 13:43:26', 'oxidpayadvance', '1348', '0', '', '', 'Battery-Pack', '1', '199', 'Deutschland', '0', 'MR', 'Am Plack', '102', '21217', 'Seevetal', '', '', '', '', '', '', 'ORDERFOLDER_NEW']


def create_order_object(row):
    order_nr = int(row[0])
    order_total = float(row[6])
    voucher_discount = float(row[7])
    article_quantity = int(row[11])
    article_price = float(row[12])
    order_delivery_cost = float(row[14])
    order_date = datetime.strptime(
        row[4], '%Y-%m-%d %H:%M:%S'
    )
    order_date_CET = timezone('Europe/Berlin').localize(order_date)
    Order.objects.create(
        order_nr=order_nr,
        user_email=row[1],
        user_bill_firstname=row[2],
        user_bill_lastname=row[3],
        order_date=order_date_CET,
        order_payment=row[5],
        order_total=order_total,
        voucher_discount=voucher_discount,
        voucher_nr=row[8],
        article_nr=row[9],
        article_title=row[10],
        article_quantity=article_quantity,
        article_price=article_price,
        country_title=row[13],
        order_delivery_cost=order_delivery_cost,
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


def import_csv():
    with open('Export Orders-2016-11-30--21-08-07.csv',
              newline='',
              encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            create_order_object(row)

# def get_project_path(doc, filename):
#     # file will be uploaded to MEDIA_ROOT/<org.slug>/<project.name>/<filename>
#     return '{0}/{1}/{2}'.format(
#         doc.project.organization.slug,
#         doc.project.name,
#         filename)


# def get_logo_path(org, filename):
#     # file will be uploaded to MEDIA_ROOT/<org.slug>/<project.name>/<filename>
#     return '{0}/logos/{1}'.format(
#         org.slug,
#         filename)


# def get_profile_path(profile, filename):
#     # file will be uploaded to MEDIA_ROOT/<org.slug>/<project.name>/<filename>
#     return '{0}/{1}/photos/{2}'.format(
#         profile.member.organization.slug,
#         profile.member,
#         filename)
