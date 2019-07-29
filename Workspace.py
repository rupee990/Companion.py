# Open All Applications for Work

import subprocess

def OpenWorkspace():
    print("Opening Workspace")
    
    #Open Unity Hub
    subprocess.Popen('C:\\Program Files\\Unity Hub\\Unity Hub.exe')

    #Open FireFox
    subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

    #Open Visual Studio
    subprocess.Popen('C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe')


