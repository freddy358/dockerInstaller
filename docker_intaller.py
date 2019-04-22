#!/usr/bin/env python3.7
import subprocess, os, logging

myCmd = os.popen('rpm -qa | grep docker').read()
myComp = os.popen('which docker-compose').read()

def composer():
    install_composer = 'curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose ; chmod +x /usr/local/bin/docker-compose'
    subprocess.call(install_composer, shell=True)
    print("Docker composer installed succesfully")


def docker():
    install_docker = "curl -fsSL https://get.docker.com/ | sh"
    start_docker = 'systemctl start docker'
    enable_docker = 'systemctl enable docker'
    for i in install_docker, start_docker, enable_docker:
        subprocess.call(i, shell=True)
    print("Docker succesfully installed")


if myCmd:
    if not myComp:
        print("Docker was installed, do you want to install docker-compose? (y/n):")
        read = input()
        if read == "y" or read == "yes" or read == "Y" or read == "YES":
            composer()
    else:
        print("Docker and docker-compose already installed")
else:
    print("Docker not installed, do you want to install? (y/n):" )
    read = input()
    if read == "y" or read == "yes" or read == "Y" or read == "YES":
        docker()
        print("Docker was installed, do you want to install docker-compose? (y/n):")
        read = input()
        if read == "y" or read == "yes" or read == "Y" or read == "YES":
            if not myComp:
                composer()
        else:
            print("Good bye!")
    else:
        print("Good bye!")

