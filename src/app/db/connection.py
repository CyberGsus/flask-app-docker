from mongoengine import connect
from os import getenv
from ..log import setup_logger
from logging import DEBUG


logger = setup_logger("db:connect", DEBUG)

defaults = {"MONGO_URI": "localhost", "DB_NAME": "db",
            "MONGO_PORT": 27017, 'DOCKER': False}

defaults.update({k: (type(defaults[k])(getenv(k) or v))
                 for k, v in defaults.items()})

logger.debug(f"Settings: {defaults}")


def connection():
    logger.info(
        f'Connecting to %(169)s {defaults["MONGO_URI"]}:{defaults["MONGO_PORT"]}/{defaults["DB_NAME"]}'
    )

    connect(
        defaults["DB_NAME"], host=defaults["MONGO_URI"], port=defaults["MONGO_PORT"], connect=(
            not defaults['DOCKER'])
    )


connected = False
if not connected:
    connection()
    connected = True
