import json
import requests
import os
import time
from subprocess import Popen, PIPE

#5 for now
url = "https://artifacthub.io/api/v1/packages/search?offset=0&limit=60&facets=false&kind=0&deprecated=false&sort=stars"

if os.path.exists("helm-charts.json"):
    with open("helm-charts.json", "r") as f:
        templates = json.loads(f.read())
else:
    r = requests.get(url)
    templates = json.loads(r.text)

    # Save to file
    with open("helm-charts.json", "w") as f:
        json.dump(templates, f)

blacklist = ['cilium', 'longhorn']
uninstall = True
install = True

if install:
    p = Popen("helm repo update", shell=True)
    p.communicate()

time.sleep(1)

if install:
    for package in templates['packages']:
        repo_name = package['repository']['name']
        repo_url = package['repository']['url']
        chart_name = package['name']
        version = package['version']

        # Check blacklist, these repos have issues
        if chart_name in blacklist:
            continue
        
        # command = "helm repo add {repo_name} {repo_url}".format(repo_name=repo_name, repo_url=repo_url)
        # print("######" + command) 
        # p = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        # p.communicate()

        # time.sleep(2)

        command = "helm install my-{chart_name} {repo_name}/{chart_name2} --namespace {chart_name3} --create-namespace --version {version} --timeout 45s".format(chart_name=chart_name, repo_name=repo_name, chart_name2=chart_name, chart_name3=chart_name, version=version)
        print("######" + command)
        p = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        p.communicate()

        time.sleep(10)

time.sleep(5)

if uninstall:
    for package in templates['packages']:
        repo_name = package['repository']['name']
        repo_url = package['repository']['url']
        chart_name = package['name']
        version = package['version']

        command = "helm uninstall --namespace {chart_name3} my-{chart_name} --timeout 45s".format(chart_name3=chart_name, chart_name=chart_name)
        print("######" + command)
        p = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        p.communicate()

        time.sleep(6)
