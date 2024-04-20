from django.contrib.auth.models import User

def UserRegistration():
    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

    user.first_name = 'John'
    user.last_name = 'Citizen'
    user.save()