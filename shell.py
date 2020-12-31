import os
# os is used for accessing our operating system
try:
    os.system('cmd /c "virtualenv venv & pip install django & django-admin startproject new . & python manage.py startapp new_app"')
    '''
        # os.system('cmd /k') here /k is used when we don't want to close
        # the cmd after the excuation of the commands 
        # if you want to run more command just add '&' and add your command
    '''
except:
    print('Run into some error')
