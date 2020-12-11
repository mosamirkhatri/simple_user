import os


class Config:
    """
    docstring
    """
    class MySql:
        DATABASE_SERVER = os.environ.get('RDS_SERVER')
        DATABASE_USER = os.environ.get('RDS_USER')
        DATABASE_PASS = os.environ.get('RDS_PASS')
        DATABASE_NAME = os.environ.get('RDS_DB')
