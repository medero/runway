from django.contrib import admin

# Register your models here.
from .models import Repo, Server, DeploymentScript, Site, Log

class RepoAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'site_id', 'directory', 'branch', 'remote')
    list_display_links = ('id', 'name')
    search_fields = [ 'name' ]
    list_per_page = 15

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'log_text', 'repo', 'created_at', 'updated_at')
    list_display_links = ('id', 'log_text')
    list_per_page = 25

admin.site.register(Repo, RepoAdmin)
admin.site.register(Server)
admin.site.register(Site)
admin.site.register(Log, LogAdmin)
admin.site.register(DeploymentScript)
