from django.shortcuts import render
from django.http import HttpResponse
from .models import Repo, Site
import os
from subprocess import call
from git import Repo

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
    directory = '/home/meder/bla/'
    repo = Repo(directory)
    repo.git.reset('--hard HEAD')
    #repo.git.
    #call(["git", "reset", "--hard", "HEAD", ">output.log"])
    #call(["git", "pull", repo.remote, repo.branch, "2>&1"])
    #call(["chmod", "-R", "og-rx", ".git"])
