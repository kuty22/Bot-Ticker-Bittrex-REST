import os


MYSQL__USER = str(os.environ.get("MYSQL_USER"))
MYSQL__PASSWORD = str(os.environ.get("MYSQL_PASSWORD"))
MYSQL__DATABASE = str(os.environ.get("MYSQL_DATABASE"))
MYSQL__HOST = str(os.environ.get("MYSQL_HOST"))

NB_WORKER = int(os.environ.get("NB_WORKER"))
BASE_CURRENCY = str(os.environ.get("BASE_CURRENCY"))
