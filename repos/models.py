from django.db import models

# Create your models here.

class Repo(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Server(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DeploymentScript(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
