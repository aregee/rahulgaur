from fabric.api import *
import os
import fabric.contrib.project as project 

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'myblog/diy/')

print os.getcwd()

def clean():
    local('rm -rf ./deploy ./myblog')

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

   
def smush():
    local('smusher ./media/images')


def openshift():
    
    os.chdir('../myblog')
    local('git add -p && git commit')
    local('git push')

 
