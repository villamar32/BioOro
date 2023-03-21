import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# mysqlclient

MYSQL_LOCAL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_remota_local',
        'USER': 'root',
        'PASSWORD': 'villamar',
        'HOST': 'localhost',
        'PORT': '3306',

    }
}

MYSQL_REMOTO = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',
        'USER': 'root',
        'PASSWORD': 'LE2qVzN40GgwNCUaSbkI',
        'HOST': 'containers-us-west-126.railway.app',
        'PORT': '7575'

    }
}
