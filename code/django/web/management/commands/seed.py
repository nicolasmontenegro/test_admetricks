from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from web.models import Dollar
from datetime import date
from decimal import *
import datetime
import requests

# python manage.py seed --mode=[refresh|clear|update]

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def run_seed(self, mode):    
    if mode == "clear":
        clear_data(self)
        return
    elif mode == "refresh":
        clear_data(self)
        get_data(
            self,
            date(year=2018, month=1, day=1),
            date.today())
        return
    elif mode == "update":
        lastest_record = Dollar.objects.latest('value_at')
        if lastest_record:
            get_data(
                self,
                lastest_record.value_at + datetime.timedelta(days=1),
                date.today())
        return


def clear_data(self):
    """Deletes all the table data"""
    self.stdout.write("Delete all data")
    Dollar.objects.all().delete()

def get_data(self, date_start, date_end):
    getcontext().prec = 2

    days_total = (date_end - date_start).days

    d_old = None

    self.stdout.write("to process %d days" % (days_total))

    for x in range(0,days_total):
        if x % 10 == 0:
            self.stdout.write("parsing day %d of %d" % (x, days_total))

        date_query = date_start + datetime.timedelta(days=x)
        r = requests.get('https://mindicador.cl/api/dolar/%s' % date_query.strftime("%d-%m-%Y"))

        if r.status_code == 200:
            r_parsed = r.json()
            if len(r_parsed["serie"]) == 1:
                value = r_parsed["serie"][0]

                delta = (value["valor"] - float(d_old.value)) if (d_old != None) else 0.0

                d = Dollar(
                    value = Decimal(str(round(value["valor"], 2))),
                    delta = Decimal(str(round(delta, 2))),
                    value_at = datetime.datetime.strptime(value["fecha"], '%Y-%m-%dT%H:%M:%S.%fZ').date())

                try:
                    d.full_clean()
                    d.save()
                    d_old = d
                except ValidationError as e:
                    self.stdout.write("error in day %d" % (x))
                    print(d)
                    print(e)
                    pass

