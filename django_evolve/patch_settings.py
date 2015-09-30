import os
import yaml
from core import settings as django_settings
from django_evolve.functions import django_evolve_log


def manage_settings_attr(key, val):
    if hasattr(django_settings, key):
        if key == 'DATABSES':
            attr = getattr(django_settings, 'DATABASES')
            for val in val:
                for k, v in val.items():
                    if k == 'db_name':
                        attr[v] = {}
                    elif k == 'NAME':
                        attr[val['db_name']][k] = os.path.join(django_settings.BASE_DIR, v),
                    else:
                        attr[val['db_name']][k] = v
        elif isinstance(val, bool) or isinstance(YamlVal, str):
            attr = val
        elif isinstance(val, list):
            attr = getattr(django_settings, key)
            for val in val:
                if isinstance(attr, dict):
                    django_evolve_log('error', 'dict type is not support yet please contact your god and master with details for fixing this bug')
                elif isinstance(attr, list):
                    attr.append(val)
                elif isinstance(attr, tuple):
                    attr += (val,)
                else:
                    django_evolve_log('error', type(attr), ' is not support yet please contact your god and master')
            setattr(django_settings, key, attr)
        elif val is None:
            django_evolve_log('warning', 'value  of ', key, ' is not define so we escape this sorry')
        else:
            django_evolve_log('info', 'due to laziness "', key, '" case is not supported please contact your god and master for fix this')
    else:
        setattr(django_settings, key, val)

conf_path = django_settings.BASE_DIR + '/conf.yaml'
if os.path.isfile(conf_path):
    with open(conf_path, 'r') as f:
        doc = yaml.load(f)
    if doc is not None:
        for YamlKey, YamlVal in doc.items():
            manage_settings_attr(YamlKey, YamlVal)
    else:
        django_evolve_log('warning', conf_path, ' is empty')
else:
    open(conf_path, 'a').close()

STATICFILES_DIRS = ()
TEMPLATES = getattr(django_settings, 'TEMPLATES')

for a in django_settings.INSTALLED_APPS:
    APP_PATH = os.path.join(django_settings.BASE_DIR, a)
    static = os.path.join(APP_PATH, 'statics')
    template = os.path.join(APP_PATH, 'templates')
    if os.path.isdir(static):
        STATICFILES_DIRS += (static,)
    if os.path.isdir(template):
        TEMPLATES[0]['DIRS'].append(template)
    if os.path.isfile(os.path.join(APP_PATH, 'settings.py')):
        app = __import__(a,  globals(), locals(), ['settings'])
        attrs_app = dir(app.settings)
        for KeyAttr in attrs_app:
            if KeyAttr[0:2] != '__':
                manage_settings_attr(KeyAttr, attrs_app[attrs_app.index(KeyAttr)])

setattr(django_settings, 'STATICFILES_DIRS', STATICFILES_DIRS)
setattr(django_settings, 'TEMPLATES', TEMPLATES)
