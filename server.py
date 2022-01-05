from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = ''

# write a function that will show a page with a form on it
# the index route will handle rendering the HTML form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got the POST info")
    # As the create_user method is the method in which we receive the information
    # from the POST request, we will write the information to session in this method
    # print(request.form)
    # Never render a template on a POST request.
    # To avoid this, redirect to the index route.
    # adding the two properties to be stored to session:
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # name = request.form['name']
    # email = request.form['email']
    return redirect('/show')

# adding the method below -Redirecting- in order to present the HTML form data
# to the user, in browser

# @app.route('/show')
# def show_user():
    # print("Showing the User Info From the Form")
    # print(request.form)
    # return render_template('show.html')
    # new version of method:
    # return render_template('show.html', name_on_template = session['username'], 
# email_on_template = session['useremail'])


# The above method passes the information that's stored in session to the correct
# templates using named arguments. Session data is also available 
# directly in the templates.

# Therefore, we can also access the session data like this, below:

@app.route('/show')
def show_user():
    return render_template('show.html')


if __name__ == "__main__":
    app.run(debug=True)
