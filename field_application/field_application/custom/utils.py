from datetime import datetime, timedelta

from django.utils import timezone


def generate_date_list_this_week():
    ''' the first day is Monday '''
    date_list = []
    now = timezone.now()
    date_of_this_Monday = now - timedelta(days=now.weekday())
    for i in range(0, 7):
        date_list.append(date_of_this_Monday + timedelta(days=i))
    return date_list


def gennerate_date_list_7days(offset=0):
    ''' the first day is today '''
    first_day = timezone.now().today() + timedelta(offset*7)
    return [ first_day + timedelta(days=i) for i in range(0,7) ]


def get_applications_a_week(application_model, offset=0):
    ''' get days apllcations of the application_model within 7 days
        the first day is today by default
        offset = -1 means last 7 days while 1 means next
    '''
    today = timezone.now().today()
    first_day = today + timedelta(offset*7)
    last_day = first_day + timedelta(days=(6+offset*7))
    applications_in_the_next_7days = application_model.objects.filter(
        date__gte=first_day,
        date__lte=last_day)
    return applications_in_the_next_7days 


def get_application_this_week(model):
    ''' get all applications whose applied field
        is going to be used this week
        depending on date field of model
    '''
    now = timezone.now()
    date_of_this_Monday = now - timedelta(days=now.weekday())
    date_of_next_Monday = date_of_this_Monday + timedelta(days=7)
    application_this_week = model.objects.filter(
        date__gte=date_of_this_Monday,
        date__lt=date_of_next_Monday)
    return application_this_week
