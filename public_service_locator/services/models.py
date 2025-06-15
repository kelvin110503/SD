from django.db import models

# factory pattern for users
class UserFactory:
  def create_user(self, role, username, password):
    user = User.objects.create_user(username=username, password=password)
    if role == "admin":
      user.is_staff = True
    user.save()
    return user
  
# database models
class Service(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
  approved = models.BooleanField(default=False) # for admin approval