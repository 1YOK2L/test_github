# manage.py
import os
from django.core.management import execute_from_command_line
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Programming.settings')
    execute_from_command_line(sys.argv)