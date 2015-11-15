from django.contrib import admin

# Register your models here.
from .models import Repo, Server, DeploymentScript

admin.site.register(Repo)
admin.site.register(Server)
admin.site.register(DeploymentScript)
