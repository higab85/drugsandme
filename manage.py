#!/usr/bin/env python
import os
import sys
import logging

logging.basicConfig(filename='dev.log', filemode='w', level=logging.DEBUG, format='[%(asctime)s]%(levelname)s: %(message)s', datefmt='%H:%M:%S')


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drugsandme.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
