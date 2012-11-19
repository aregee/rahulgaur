from fabric.api import *
import os
import fabric.contrib.project as project 


print os.getcwd()

def clean():
    local('rm -rf ./deploy')

def generate():
    local('hyde -g -s .')
def regen():
    clean()
    generate()

def serve():
    local('hyde -w -s . -k')

def deploy():
    local('hyde -g -d ../myblog/diy/')

def reserve():
    regen()
    serve()

def openshift():
    
    os.chdir('../myblog')
    local('git add . && git commit')
    local('git push')

 
