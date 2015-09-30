import sys
from django_evolve.django_evolve_cmd import django_evolve_cmd
from django_evolve import patch_settings

patch_settings
django_evolve_cmd(sys.argv)
