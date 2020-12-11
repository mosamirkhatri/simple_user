from flask import Flask, request, render_template

from utils import call_procedure, validate_request

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    call_procedure('CALL create_user_table')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/users', methods=['POST', 'GET'])
def get_users():
    try:
        if request.method == 'GET':
            query_output = call_procedure("CALL get_all_users();")

            response_data = []
            for i in query_output:
                response_data.append({
                    'user_id': i.get('user_id'),
                    'name': i.get('name'),
                    'email': i.get('email'),
                    'mobile': i.get('mobile'),
                    'address': {
                        'flat_number': i.get('flat_number'),
                        'address_line_one': i.get('address_line_one'),
                        'address_line_two': i.get('address_line_two'),
                        'city': i.get('city'),
                        'state': i.get('state'),
                        'pincode': i.get('pincode')
                    }
                })

            return {"data": response_data, "success": True}, 200

        elif request.method == "POST":
            request_data = request.get_json()

            [valid, error] = validate_request(request_data)
            if not valid:
                return {"success": False, "message": error}, 400

            name = request_data.get('name')
            email = request_data.get('email')
            mobile = request_data.get('mobile')

            # Check duplicates for email/mobile
            duplicate_values = call_procedure(
                "CALL check_existing_email_mobile(%s, %s);", (email, mobile))
            if duplicate_values:
                return {"success": False, "message": "Email or Mobile Exists!!"}, 409

            address = request_data.get('address')
            flat_number = address.get('flat_number')
            address_line_one = address.get('address_line_one')
            address_line_two = address.get('address_line_two')
            city = address.get('city')
            state = address.get('state')
            pincode = address.get('pincode')

            query_output = call_procedure('''CALL insert_new_user(%s, %s, %s, %s, %s, %s, %s, %s, %s);''',
                                          (name, email, mobile, flat_number, address_line_one, address_line_two, city, state, pincode))
            result = {
                'user_id': query_output.get('user_id'),
                'name': query_output.get('name'),
                'email': query_output.get('email'),
                'mobile': query_output.get('mobile'),
                'address': {
                    'flat_number': query_output.get('flat_number'),
                    'address_line_one': query_output.get('address_line_one'),
                    'address_line_two': query_output.get('address_line_two'),
                    'city': query_output.get('city'),
                    'state': query_output.get('state'),
                    'pincode': query_output.get('pincode')
                }
            }
            return {"data": result, "success": True}, 200

    except Exception as e:
        print(e)
        return {"success": False, "message": e.args}, 500
