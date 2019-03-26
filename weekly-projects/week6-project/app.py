import datetime

from flask import Flask
from flask import flash, render_template, request, url_for, session, redirect

from auth import Auth
from call import Call
from customer import Customer

app = Flask(__name__)
app.secret_key = b'J.;0ajk>,m8jkLIn89hans*jkj90($'


def is_logged_in():
    auth = Auth()
    return auth.is_logged_in()

def is_valid_customer_id(customer_id):
    customer = Customer.get(customer_id)
    return customer is not None


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        auth = Auth()
        if auth.login(username, password):
            return redirect(url_for('show_customers'))
        else:
            flash('Could not log you in')
    return render_template('auth/login.html')


@app.route("/logout/")
def logout():
    auth = Auth()
    auth.logout()
    return redirect(url_for('login'))


@app.route("/customers/")
def show_customers():
    if not is_logged_in():
        return redirect(url_for('login'))
    customers = Customer.get_all()
    print(customers)
    return render_template('customer/show-list.html', customers=customers)


@app.route("/customers/add/", methods=['GET', 'POST'])
def add_customer():
    if not is_logged_in():
        return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('customer/add.html')
    else:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        postal_code = request.form.get('postal_code')
        city = request.form.get('city')
        country = request.form.get('country')

        user = Auth().get_current_user()
        added_by = user['user_id']

        customer = Customer(first_name, last_name, phone, email,
                            address1, address2, postal_code, city,
                            country, None, added_by)
        customer.save()
        return redirect(url_for('show_customers'))


@app.route("/customers/<int:customer_id>/edit/", methods=['GET', 'POST'])
def edit_customer(customer_id):
    if not is_logged_in():
        return redirect(url_for('login'))
    if not is_valid_customer_id(customer_id):
        return redirect(url_for('show_customers'))
    customer = Customer.get(customer_id)

    if request.method == 'GET':
        return render_template('customer/edit.html', customer=customer)

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address1 = request.form.get('address1')
    address2 = request.form.get('address2')
    postal_code = request.form.get('postal_code')
    city = request.form.get('city')
    country = request.form.get('country')

    customer.first_name = first_name
    customer.last_name = last_name
    customer.phone = phone
    customer.email = email
    customer.address1 = address1
    customer.address2 = address2
    customer.postal_code = postal_code
    customer.city = city
    customer.country = country

    customer.save()
    flash('Customer saved')
    return redirect(url_for('show_customers'))


@app.route("/customers/<int:customer_id>/")
def show_customer(customer_id):
    if not is_logged_in():
        return redirect(url_for('login'))
    if not is_valid_customer_id(customer_id):
        return redirect(url_for('show_customers'))
    customer = Customer.get(customer_id)
    calls = Call.get_for_customer(customer_id, True)

    return render_template('customer/show-one.html', customer=customer, calls=calls)


@app.route("/calls/add/", methods=['POST'])
def add_call():
    if not is_logged_in():
        return redirect(url_for('login'))

    customer_id = request.form.get('customer_id')
    if not is_valid_customer_id(customer_id):
        return redirect(url_for('show_customers'))

    customer = Customer.get(customer_id)
    user = Auth().get_current_user()
    user_id = user['user_id']

    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notes = request.form.get('notes', '')

    call = Call(customer_id, user_id, date, notes)
    call.save()
    flash('Call saved')
    return redirect(url_for('show_customer', customer_id=customer_id))
