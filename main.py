from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    # Renders the UI form where the user enters details
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    # Captures data from the form and passes it to the resume template UI
    data = {
        'name': request.form.get('name'),
        'title': request.form.get('title'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'summary': request.form.get('summary'),
        'skills': request.form.get('skills', '').split(','),
        'experience': request.form.get('experience'),
        'education': request.form.get('education')
    }
    return render_template('resume.html', user=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
