import os
from core import settings as django_settings


def custom_django_cmd(args):
    if args[1] == "startapp":
        path_app = os.path.join(django_settings.BASE_DIR, args[2])
        to_create = [
            {
                'type': 'folder',
                'name': 'forms',
                'path': path_app,
                'package': True
            },
            {
                'type': 'folder',
                'name': 'statics',
                'path': path_app,
                'sub_folders': [
                    os.path.join(path_app, os.path.join('statics', args[2])),
                    os.path.join(path_app, os.path.join('statics', os.path.join(args[2], 'css'))),
                    os.path.join(path_app, os.path.join('statics', os.path.join(args[2], 'imgs'))),
                    os.path.join(path_app, os.path.join('statics', os.path.join(args[2], 'js'))),
                ],
            },
            {
                'type': 'folder',
                'name': 'templates',
                'path': path_app,
                'sub_folders': [
                    os.path.join(path_app, os.path.join('templates', args[2])),
                ],
            },
            {
                'type': 'folder',
                'name': 'tests',
                'path': path_app,
                'sub_folders': [],
                'delete_files': [
                    os.path.join(path_app, 'tests.py'),
                ],
                'package': True
            },
            {
                'type': 'folder',
                'name': 'views',
                'path': path_app,
                'delete_files': [
                    os.path.join(path_app, 'views.py'),
                ],
                'package': True
            },
            {
                'type': 'file',
                'name': 'urls.py',
                'path': path_app,
                'content': '# -*-coding:utf-8 -*-\nfrom django.conf.urls import patterns\nfrom django.conf.urls import url\n\nurlpatterns = []',
            },
        ]
        for t_c in to_create:
            if t_c['type'] == 'file':
                urls = open(os.path.join(t_c['path'], t_c['name']), 'a')
                urls.write(t_c['content'])
                urls.close()
            elif t_c['type'] == 'folder':
                os.mkdir(os.path.join(t_c['path'], t_c['name']))
                if 'sub_folders' in t_c.keys() and len(t_c['sub_folders']) > 0:
                    for s_f in t_c['sub_folders']:
                        os.mkdir(os.path.join(t_c['path'], os.path.join(t_c['name'], s_f)))
                if 'package' in t_c.keys() and t_c['package']:
                    open(os.path.join(t_c['path'], '__init__.py'), 'a').close()
            else:
                print('[ERROR] : ', t_c['type'], ' is not supported')
            if 'delete_files' in t_c.keys() and len(t_c['delete_files']) > 0:
                for delete_file in t_c['delete_files']:
                    os.remove(delete_file)
            if 'delete_folders' in t_c.keys() and len(t_c['delete_folders']) > 0:
                    for delete_folders in t_c['delete_folders']:
                        os.remove(delete_folders)
