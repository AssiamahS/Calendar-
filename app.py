from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = []

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    event_name = request.form.get('event_name')
    event_date = request.form.get('event_date')
    if event_name and event_date:
        events.append({'name': event_name, 'date': event_date})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
