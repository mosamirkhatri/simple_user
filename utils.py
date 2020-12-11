import pymysql.cursors
from cerberus import Validator
from .config import Config


def call_procedure(query, parameter_values=None):
    connection = pymysql.connect(host=Config.MySql.DATABASE_SERVER, user=Config.MySql.DATABASE_USER,
                                 password=Config.MySql.DATABASE_PASS, db=Config.MySql.DATABASE_NAME,
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameter_values)
        result = []
        if cursor.rowcount == 1:
            result = cursor.fetchone()
        elif cursor.rowcount > 1:
            result = cursor.fetchall()
        return result
    except Exception as e:
        raise Exception(e)
    finally:
        connection.commit()
        cursor.close()
        connection.close()


schema = {
    'name': {"type": "string", "minlength": 3, "maxlength": 50, "required": True},
    'email': {"type": "string", "minlength": 7, "maxlength": 100},
    'mobile': {"type": "string", "minlength": 10, "maxlength": 10, "required": True},
    'address': {
        "type": "dict",
        "schema": {
            'flat_number': {"type": "string", "minlength": 3, "maxlength": 50, "required": True},
            'address_line_one': {"type": "string", "minlength": 3, "maxlength": 100, "required": True},
            'address_line_two': {"type": "string", "minlength": 3, "maxlength": 100},
            'city': {"type": "string", "minlength": 3, "maxlength": 30, "required": True},
            'state': {"type": "string", "minlength": 3, "maxlength": 30, "required": True},
            'pincode': {"type": "string", "minlength": 6, "maxlength": 6, "required": True}
        },
        "required": True
    }
}


def validate_request(request_body):
    v = Validator()
    valid = v.validate(request_body, schema)
    return valid, v.errors
