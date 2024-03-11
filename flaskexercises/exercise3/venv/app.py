from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This will be your in-memory data storage.
registrations = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Validate and process the form data
        name = request.form.get('name')
        organization = request.form.get('organization')
        # Perform validation checks here...
        # Add to the registrations dictionary
        registrations[name] = organization
        return redirect(url_for('registered_users'))
    # Render the home page template with form
    return render_template('home.html', organizations=['Org1', 'Org2', 'Org3', 'Org4', 'Org5'])

@app.route('/registrations')
def registered_users():
    # Render the page with the list of registered users
    return render_template('registrations.html', registrations=registrations)

if __name__ == '__main__':
    app.run(debug=True)
