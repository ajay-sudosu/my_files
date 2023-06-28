from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

@api_view(['GET'])
def my_custom_sql(request):
    if request.method == "GET":
        res = {}
        with connection.cursor() as cursor:
            cursor.execute("select * from student")
            rows = cursor.fetchall()
            for row in rows:
                res[row[1]] = row[2]
        return Response({"message":res})




def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })