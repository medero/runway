from django.shortcuts import render
from django.http import HttpResponse
from .models import Repo, Site, Log
import os
import subprocess
#from subprocess import call
import git

# Create your views here.

def index(request):
    site_name = request.GET.get('site')
    branch = request.GET.get('branch')
    if site_name is not None and branch is not None:
        repo = findRepo(site_name, branch)

        if repo:
            Deploy(repo)
        else:
            return HttpResponse('not found 2')

    else:
        return HttpResponse('not found.')

def findRepo(site_name, branch):
    sites = Site.objects.filter(name=site_name)
    found = False

    if sites:
        site_id = sites[0].id
        o = Repo.objects.filter(site_id=site_id,branch=branch)
        if o:
            return o[0]

    return None

def Deploy(repo):
    directory = repo.directory
    #r = git.Repo(directory)
    os.chdir(directory)

    output = ''
    output += subprocess.check_output(["git", "reset", '--hard', 'HEAD'])
    output += subprocess.check_output(["git", "pull", repo.remote, repo.branch])
    output += subprocess.check_output(['chmod', '-R', 'og-rx', '.git'])
    output += 'directory: ' + directory + ', site_name=' + repo.site_id.name
    x = Log(log_text=output, repo=repo)
    x.save()

    #if r:
        #r.git.reset('--hard')
        #if r.remotes[repo.remote]:
            #r.remotes[repo.remote].pull()
            #call(['chmod', '-R', 'og-rx', '.git'])
            #x = Log(log_text='Successfully pulled.', repo=repo)
            #x.save()
