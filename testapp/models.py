from django.db import models
from django.utils import timezone

class Question(models.Model):
    """
    Code is from the book Instant Django 1.5 Application Development Starter
    There may be additional comments written by me for understanding once 
    I see the code.
    Note that each model is represented by a class that is a subclass of
    django.db.models.Model. The class variables in the models represent
    the database field
    After the creation of these two classes modify INSTALLED_APPS(settings.py)
    """
    
    subject = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.subject
    
    def published_today(self):
        return self.publication_date.date() == timezone.now().date()

class Answer(models.Model):
    """ 
    Also note that each field is an instance of Field class and tells Django
    what kind of data each field holds.Ex: TextField, BooleanField.
    The name of each field instance is the name that will be used in my python
    code to reference the field as well as the column in the database.
    Example: In this class question, content, best_answer are the field names
    column names in the db.
    Note that the relationship is also specified between the two classes through
    field class ForeignKey.
    Django uses these models which are ready, to create db tables for me and
    provides an API to access and manipulate the data.AWESOME!
    """   
    
    question = models.ForeignKey(Question)
    content = models.TextField()
    best_answer = models.BooleanField("preferred answer", default=False)
    
    def __unicode__(self):
        return self.content
