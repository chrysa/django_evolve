import time


GREEN = "\033[1;32m"
BLUE = "\033[2;34m"
ORANGE = "\033[0;33m"
RED = "\033[2;31m"
WHITE = "\033[00m"


def django_evolve_log(*argc, **argv):
    argc = list(argc)
    if argc[0].lower() == "success":
        mess = GREEN
    elif argc[0].lower() == "info":
        mess = BLUE
    elif argc[0].lower() == "warning":
        mess = ORANGE
    elif argc[0].lower() == "error":
        mess = RED
    else:
        mess = WHITE
    mess += '[' + time.strftime("%d/%b/%Y  %H:%M:%S") + '][DJANGO EVOLVE] [' + argc[0].upper() + '] : '
    argc.remove(argc[0])
    for ac in argc:
        mess += str(ac)
    mess += WHITE
    print(mess)
