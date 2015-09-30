import os
import sys
from django.core.management import execute_from_command_line

from core import settings as django_settings

available_cmd = [
    'testandrun'
]

correspondance = [
    {
        'name': 'testandrun',
        'commande': [
            'test',
            'runserver'
        ]
    }
]


def custom_exec(cmd):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    cmd_index = next(index for (index, d) in enumerate(correspondance) if d["name"] == cmd[1])
    for commande in correspondance[cmd_index]['commande']:
        cmd[1] = commande
        print('before exec : ', getattr(django_settings, 'DEBUG'))
        execute_from_command_line(cmd)


def django_evolve_cmd(argv):
    if argv[1] in available_cmd:
        custom_exec(argv)
        sys.exit(0)
    else:
        pass
