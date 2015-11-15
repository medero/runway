from django.contrib import admin

# Register your models here.
from .models import Repo, Server, DeploymentScript, Sites

admin.site.register(Repo)
admin.site.register(Server)
admin.site.register(Site)
admin.site.register(DeploymentScript)
