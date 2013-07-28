from django.http import HttpResponse
from testapp.models import Question

def index(request):
    """
    A view is just a python function that accepts a request object as 
    the first parameter and returns a valid HttpResponse Object
    The request parameter is mandatory and may contain possible 
    the POST or GET variables,sessions etcetra.
        * ROOT_URLCONF variable in settings.py
        * urlpatterns - sequence of tuples (regex, callback[, dict])
    Django matches the requested URL against each regex in the list,
    as soon as it finds one that matches it calls the callback python
    function by passing an HttpRequest object as the first arg.
    """
    
    questions = Question.objects.all()
    response_string = "Questions <br />"
    response_string += '<br/>'.join(["id: %s, subject: %s" 
                                      % (q.id, q.subject) for q in questions])
    return HttpResponse(response_string)

