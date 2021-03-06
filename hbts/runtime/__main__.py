"""Start the main :mod:`hbts` application using the
specified command-line parameters.
"""
import argparse
import logging
import os
import sys

import yaml

import sq.runtime


DEPLOYMENT_ENV = os.getenv('QUANTUM_DEPLOYMENT_ENV') or 'production'

# This is a hook to load secrets or other environment variables
# from YAML-encoded file, for example when using Docker Swarm
# secrets.
if os.getenv('HBTS_SECRETS'):
    with open(os.getenv('HBTS_SECRETS')) as f:
        secrets = yaml.safe_load(f.read()) #pylint: disable=invalid-name
    for key, value in secrets.items():
        if not key.startswith('HBTS'):
            continue
        os.environ[key] = str(value)

    del secrets


os.environ['SQ_ENVIRON_PREFIX'] = 'HBTS'
DEFAULT_SECRET_KEY = "197fb52f8305c461a677256c3cb588e64936dc814e8fcda98f5a0148be514da6"
os.environ.setdefault('HBTS_SECRET_KEY', "197fb52f8305c461a677256c3cb588e64936dc814e8fcda98f5a0148be514da6")
os.environ.setdefault('HBTS_DEBUG', "1")
os.environ.setdefault('HBTS_IOC_DEFAULTS', "/etc/hbts/ioc.conf")
os.environ.setdefault('HBTS_IOC_DIR', "/etc/hbts/ioc.conf.d/")
os.environ.setdefault('HBTS_RDBMS_DSN', "postgresql+psycopg2://hbts:hbts@rdbms:5432/hbts")


class MainProcess(sq.runtime.MainProcess):
    """The main :mod:`hbts` process manager."""
    framerate = 10
    components = [
        sq.runtime.HttpServer,
    ]


parser = argparse.ArgumentParser() #pylint: disable=invalid-name
parser.add_argument('-c', dest='config',
    default='./etc/hbts.conf',
    help="specifies the runtime configuration file (default: %(default)s)")
parser.add_argument('--loglevel',
    help="specifies the logging verbosity (default: %(default)s)",
    choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], default='INFO')


if __name__ == '__main__':
    logger = logging.getLogger('hbts') #pylint: disable=invalid-name
    args = parser.parse_args() #pylint: disable=invalid-name
    p = MainProcess(args, logger=logger) #pylint: disable=invalid-name

    if DEFAULT_SECRET_KEY == os.getenv('HBTS_SECRET_KEY'):
        logger.critical("The application is started using the default secret key")
        if DEPLOYMENT_ENV == 'production':
            logger.critical("DEFAULT_SECRET_KEY may not be used in production")
            sys.exit(128)


    try:
        sys.exit(p.start() or 0)
    except Exception: #pylint: disable=broad-except
        logger.exception("Fatal exception caused program termination")
        sys.exit(1)


# !!! SG MANAGED FILE -- DO NOT EDIT !!!
