"""
Example usage of models.

Lines 11 - 25 of this code are just for configuring Django
so that you can run this file as a stand-alone script.

You can also run the examples by running:
  $ python manage.py shell (to start a Django-configured shell)
and then copying and pasting the examples into the shell
"""
import os
import sys
from pathlib import Path


# Make sure Python looks in your trivia_site directory when searching for modules
TRIVIA_SITE_DIR = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(TRIVIA_SITE_DIR))

# Let Django know where to find your settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trivia_project.settings.local')

# Configure Django so your models can be used
import django
django.setup()

# ------------ END of Django setup ----------------

# Import your models
from apps.questions.models import *
# If your IDE gives you an error here:
#   In PyCharm, mark the trivia_site folder as a source root
#   In VS Code, in the Pylance settings, add the trivia_site folder to the extra paths to search: https://stackoverflow.com/a/64103291


# Need to clean up test data from db (normally you would use a separate test db)
last_pk = Question.objects.last().pk  # save the last question's id so we can delete anything created afterwards

# ____________ CREATING OBJECTS ____________

# Create an object without saving to the database (manual save)
q = Question(text="What does ORM stand for?")  # Initialize some fields
q.details = "Hint: you use it to query the database in Python"  # Edit a field
q.difficulty = Question.Difficulty.EASY  # Set a Choice field from an Enum
q.save()  # Save to the db

c1 = Choice(question=q, text="One Radical Magic").save()  # Create related object
c2 = Choice(question=q, text="Object Relational Mapping", is_correct=True).save()

# Create an object and save it to the database
q2 = Question.objects.create(text="What was Django named after?")
Choice.objects.create(question=q2, text="Django Reinhardt (musician)", is_correct=True)
Choice.objects.create(question=q2, text="Django Unchained (movie)", is_correct=False)

# This next bit will make 3 database calls
q3 = Question.objects.create(
    text="What programming language is Django written in?",
    difficulty=Question.Difficulty.MEDIUM,
)  # Create and save to db

q3.difficulty = Question.Difficulty.EASY
q3.save()  # Update object and then save
print(q3.pk)  # Get the object's primary key (id)
q3.delete()  # Delete the object

# ____________ QUERYING THE DATABASE ____________

# Get a single object
try:
    a_question = Question.objects.get(pk=1)  # Try to get an object by ID, can put any filter in here though
    print(a_question)
except Question.DoesNotExist:
    print(f"Question does not exist")
except Question.MultipleObjectsReturned:
    print(f"Multiple questions were returned")

# Get the first/last object
first_q = Question.objects.first()  # Order is pk (default) or what is defined in the model's Meta.ordering
first_created_q = Question.objects.order_by('created_at').first()  # Specify ordering
last_created_q_1 = Question.objects.order_by('created_at').last()
last_created_q_2 = Question.objects.order_by('-created_at').first()  # Reverse order by adding "-" to field
assert last_created_q_1 == last_created_q_2

# Get the set of all objects (returns a QuerySet)
questions = Question.objects.all()

# Get a filtered set of objects
easy_questions = Question.objects.filter(difficulty=Question.Difficulty.EASY)

# Get the number of items in the QuerySet (qs)
print(f"There are {easy_questions.count()} easy questions (out of {questions.count()})")

# Filter based on related objects
qs_without_choices = Question.objects.filter(choices__isnull=True)
print(f"There are {qs_without_choices.count()} questions without choices")

# Can filter based on excluding items
qs_without_answer = Question.objects.exclude(choices__is_correct=True)
print(f"There are {qs_without_answer.count()} questions without answers")

# Bulk update
Question.objects.filter(pk__gt=last_pk).update(details="This is a test question")

# ____________ CLEANUP OF TEST DATA ____________
Question.objects.filter(pk__gt=last_pk).delete()

