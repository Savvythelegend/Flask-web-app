from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
Jobs = [{
    'id': "1",
    'title': "Data Analyst",
    'location': "Bengaluru, India",
    'salary': '$50,000'
}, {
    'id': "2",
    'title': "Data Engineer",
    'location': "Bengaluru, India",
    'salary': '$90,000'
}, {
    'id': "3",
    'title': "Product Manager",
    'location': "Hyderabad, India",
    'salary': '$100,000'
}, {
    'id': "4",
    'title': "Senior Software Enginner",
    'location': "San Francisco, California",
    'salary': '$150,000'
}]


@app.route('/')
def greet():
    return render_template('home.html')


@app.route('/home')
def home_joivan():
    return render_template('portal.html',
                           debug=True,
                           jobs=Jobs,
                           company_name='Jovian')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(Jobs)
