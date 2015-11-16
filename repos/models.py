from django.db import models

# Create your models here.

class Repo(models.Model):
    name = models.CharField(max_length=100)
    directory = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, default="master")
    remote = models.CharField(max_length=100, default="origin")
    post_deploy = models.ForeignKey('DeploymentScript', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    site_id = models.ForeignKey('Site')

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    server_id = models.ForeignKey('Server', default=1)

    def __str__(self):
        return self.name

class Server(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class DeploymentScript(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
