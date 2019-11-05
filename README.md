# web_api
# api learning in this project with postman
# adding __init__.py in a directory helps to treat the directory as module in django/python
###############################################################################
# commands
pipenv --python 3.7
pipenv shell
pipenv install django==2.2.2
pipenv install djangorestframework==3.10

pipenv install djangorestframework_simplejwt

after installation visit https://github.com/davesque/django-rest-framework-simplejwt for configuration and instructions

Before running this command ensure that you have apis/accounts directory
python manage.py startapp accounts apis/accounts
choices field takes a list of lists or tuple of tuples, ...

models fields are related to database

#################################################################################

# related_name is required in foreignkey relationships to identify the fields and so get the field look in serializers.py...

# group identifies the custom user as auth user from settings AUTH_USER_MODEL


# _("date of birth") === single underscore is similar to verbose_name = "date of birth"
    
    from django.utils.translation import gettext_lazy as _

        dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)

    USERNAME_FIELD = "name" // "email also " -- but should be unique

# setting the environment variables using set variablename=value -- using cmd
# setting the environment variable using .env file which contains key and value with python-dotenv installation
            from dotenv import load_dotenv
                load_dotenv()
                print(os.getenv('name')) # overiding the system variables using override=True in load_dotenv(override=True)// look in documentation