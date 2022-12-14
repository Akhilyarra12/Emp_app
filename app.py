from flask import Flask, request
from dao import DataAccess
from service import check_user, add_user

app = Flask(__name__)

# Employee signup
'''
End point implementation
API Implementation
Backend code 
'''


@app.route('/')
def Home():
    return "<h1>Flask app created successfully</h1>"

@app.route("/createdb", methods=['GET'])
def create_database():
    with DataAccess("172.23.234.199", "pythondb", "python", "123456", 5432) as cursor:
        cursor.execute("CREATE TABLE employee(FirstName VARCHAR(100), LastName VARCHAR(100), Eid INTEGER, UserId INTEGER, Password VARCHAR(50), MobileNo VARCHAR(12), EmailId VARCHAR(50), DOB VARCHAR(50), Address VARCHAR(50), Gender VARCHAR(10), DOJ VARCHAR(50), Technology VARCHAR(50))")
    return "<h2>Table created successfully.</h2>"


@app.route('/sign_up/',methods = ['POST'])
def sign_up():
    data = request.get_json()
    print("Data : ", data)
    print("Signup operation in Progress")
    is_exists = check_user(data['eid'], data['userid'])
    print(is_exists)
    if is_exists == True:
        '''
        1. Check userid, Eid exists in db or not 
            1. If exists send error message
            2. Else pass data to service layer
        '''
        # Server side validation
        # Pass data to service layer
        return "The user already exist, please try again with different user."
    else:
        resp = add_user(data['firstname'], data['lastname'], data['eid'], data['userid'], data['password'], data['mobileno'], data['emailid'], data['dob'], data['address'], data['gender'], data['doj'], data['technology'])

        return resp


if __name__ == '__main__':
    app.run(debug = True)