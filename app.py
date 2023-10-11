#!/usr/bin/env python3

import os
from argparse import ArgumentParser
from time import sleep
from modules.api_app import API_App

VERSION = '0.0.1'

app = API_App()

#
# Setup application
#
def setup(args):
    return True

#
# Main loop task
#
def do():
    return True

#
# Exit application
#
def terminate():
    app.close()
    print('Application terminated.')
    exit(0)

#
# Fatal error occured, exit application
#
def error(errortext):
    app.close()
    print('ERROR: ' + errortext)
    exit(1)


#
# Main entry point
#
if __name__ == '__main__':
    args = ArgumentParser(
        description='Template Application',
    )

    app.run(args)
    if not setup(args):
        error('Setup failed!')

    while True:
        try:
            if not do():
                error('Do failed!')
            sleep(0.01)

        except KeyboardInterrupt:
            error('User interrupt ^C')
        except Exception as ex:
            error(ex)
        
    terminate()

