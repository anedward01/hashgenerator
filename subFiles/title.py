import os

def version():
    vers = '2.2.1'
    return vers

def title():
    if os.name == 'nt':
        _ = os.system('title Hash Generator V. ' + version())
    else:
        x = 5