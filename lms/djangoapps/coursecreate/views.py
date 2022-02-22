from django.shortcuts import render
from django.http import HttpResponse
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.db import connection
from datetime import datetime

def index(request):
    return HttpResponse(test(5))

def test(id):
    cursor = connection.cursor()
    ##q = "SELECT created FROM course_overviews_courseoverview WHERE id = '{}'".format(id)
    q = "SELECT created FROM course_overviews_courseoverview WHERE id = '{}'".format(id)
    cursor.execute(q)
    row = cursor.fetchone()

    #datetime_object = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
    ##return CourseOverview.get_from_id(id).display_name
## create =  CourseOverview

    #return datetime_object.strftime("%Y")
    return row[0].strftime("%Y-%m-%dT%H:%M:%S%z")

