"""Environment variables specified by the application Quantumfile."""
import os

import yaml


DEFAULT_SECRET_KEY = "197fb52f8305c461a677256c3cb588e64936dc814e8fcda98f5a0148be514da6"

# Set up some variables serving as hints to the Quantum framework.
os.environ['SQ_ENVIRON_PREFIX'] = 'HBTS'


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


# Provide some defaults to the environment prior to assigning the
# module-level constants.
os.environ.setdefault('HBTS_SECRET_KEY',
    "197fb52f8305c461a677256c3cb588e64936dc814e8fcda98f5a0148be514da6")
os.environ.setdefault('HBTS_DEBUG',
    "1")
os.environ.setdefault('HBTS_IOC_DEFAULTS',
    "/etc/hbts/ioc.conf")
os.environ.setdefault('HBTS_IOC_DIR',
    "/etc/hbts/ioc.conf.d/")
os.environ.setdefault('HBTS_RDBMS_DSN',
    "postgresql+psycopg2://hbts:hbts@rdbms:5432/hbts")
os.environ.setdefault('HBTS_HTTP_ADDR',
    "0.0.0.0")
os.environ.setdefault('HBTS_HTTP_PORT',
    "8443")
os.environ.setdefault('HBTS_TSA_REQUEST_URI',
    "https://freetsa.org/tsr")


SECRET_KEY = os.getenv('HBTS_SECRET_KEY')
DEBUG = os.getenv('HBTS_DEBUG', '').lower() in ('yes', '1', 'true')
IOC_DEFAULTS = os.getenv('HBTS_IOC_DEFAULTS')
IOC_DIR = os.getenv('HBTS_IOC_DIR')
RDBMS_DSN = os.getenv('HBTS_RDBMS_DSN')
HTTP_ADDR = os.getenv('HBTS_HTTP_ADDR')
HTTP_PORT = os.getenv('HBTS_HTTP_PORT')
TSA_REQUEST_URI = os.getenv('HBTS_TSA_REQUEST_URI')
DEPLOYMENT_ENV = os.getenv('QUANTUM_DEPLOYMENT_ENV') or 'production'
CONFIG_DIR = os.getenv('QUANTUM_CONFIG_DIR')
TEST_PHASE = os.getenv('SQ_TESTING_PHASE')
