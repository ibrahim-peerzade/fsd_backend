from flask import Flask ,render_template,request,flash,url_for,redirect,session,jsonify
import travels_conntroller as travels
from flask_cors import CORS

app= Flask(__name__)
CORS(app, origins="http://localhost:4200")  # Enable CORS for all routes and origins

app.secret_key = 'your_secret_key'

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


@app.route('/')
def hello_word():
    return "hello word"

@app.route('/user_register')
def user_registration():
    return render_template('user_register.html')


@app.route('/user_register', methods=['POST'])
def user_register():
    if request.method == 'POST':
        data = request.json  # Parse JSON data from Angular
        username = data.get('username')
        password = data.get('password')
        full_name = data.get('full_name')  # Use snake_case keys
        Address = data.get('Address')
        Mob_no = data.get('Mob_no')
        Email = data.get('Email')
        Gender = data.get('Gender')


        # Mocked result for demonstration purposes
        # Replace this with your database logic
        if username and password and Email:
            # Simulate a successful database operation
            travels.user_register(full_name,Email,Mob_no,Gender,Address,username,password)
            return jsonify({'message': 'REGISTER SUCCESSFUL'})
        else:
            return jsonify({'message': 'REGISTER FAILURE'})
    return jsonify({'message': 'INVALID DATA'})
    
@app.route('/login-user', methods=['POST'])
def login_user(): 
    if request.method == 'POST':
        data = request.get_json()  # Parse JSON data from the request body
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'message': 'Username and password are required'}, 400

        result = travels.login(username, password)
        if result is not None:
            session['userid'] = result['Id']
            session['username'] = result['full_name']
            return {'message': 'LOGIN SUCCESSFUL', 'userId': result['Id']}
        else:
            return {'message': 'Login failed', 'error': 'Invalid username or password'}, 401

# @app.route('/login-user', methods=['GET', 'POST'])
# def login_user():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         result = travels.login(username, password)

#         if result is not None:
#             session['userid'] = result['Id']
#             session['username'] = result['full_name']
#             return {'message': 'LOGIN SUCCESSFUL'}
#         else:
#             return {'message': 'Login failure', 'error': 'Invalid username or password'}, 401
#     else:
#         return {'message': 'Please log in using POST method'}

@app.route('/logout')
def logout():
    # Clear the session data to log the user out
    session.clear()
    return redirect(url_for('login'))


@app.route('/travel/book', methods=['POST'])
def booking():
    if request.method == 'POST':
        data = request.json  # Expecting JSON data
        full_name = data['full_name']
        Email = data['Email']
        Mob_No = data['Mob_no']
        Date_and_Time = data['Date_and_Time']
        AddressFrom = data['Addressfrom']
        AddressTo = data['AddressTo']
        Car_Model = data['carmodel']

        result = travels.save_booking(full_name, Email, Mob_No, Date_and_Time, AddressFrom, AddressTo, Car_Model)
        if result:
            return {'message': 'BOOKING SUCCESSFUL'}
        else:
            return {'message': "BOOKING FAILED"}
    else:
        return {'message': "BOOKING FAILED"}


if __name__ == '__main__':
    app.run(debug=True)