from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)
    # password = models.CharField(max_length=50)


    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=2500)

    def __str__(self):
        return self.first_name, self.last_name, self.email, self.subject, self.message


class ProjectIdea(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    subject_genre = models.CharField(max_length=150)
    project_name = models.CharField(max_length=150)
    project_description = models.CharField(max_length=4000)


