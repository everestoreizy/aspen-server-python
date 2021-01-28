from flask import Flask, request, render_template, url_for, g
from classes import Item, ItemCollection, sort_items
from ics import Calendar
import datetime, requests
from google.cloud import firestore


# Project ID is determined by the GCLOUD_PROJECT environment variable.
#   Should be set to the path of the Aspen Planner alskjflsdjfa;slkjfda;sld json file
db = firestore.Client()

# CLEAR BROWSER CACHE EVERY TIME OR ELSE THINGS WON'T UPDATE PROPERLY
# Settings > Additional Settings > Privacy & Security > Clear browsing data > Only select "Cached images and files"

my_ical = "https://eastsideprep.instructure.com/feeds/calendars/user_MPUy1VMR3ETeTWnqhcr7AwY5ni2jUfM4UgHu14T9.ics"

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

#TESTING VARS
username = "eoreizy"
fname = "Everest"
lname = "Oreizy"
test_items = [
    Item(0, "CW Tener Mas", "n", False, datetime.date(2020, 10, 11), datetime.date(2020, 10, 15)),
    Item(1, "Contemplation Day 13", "n", False, datetime.date(2020, 10, 11), datetime.date(2020, 10, 12)),
    Item(2, "Rational Roots", "nx", False, datetime.date(2020,10,11), datetime.date(2020, 10, 13)),
    Item(3, "Mixed Nomenclature", "nx", False, datetime.date(2020, 10, 12), datetime.date(2020, 10, 15)),
    Item(4, "Lab 4", "lab4", True, datetime.date(2020, 10, 11), datetime.date(2020, 10, 12)),
    Item("string", "SM3DAS", "sm3d", False, datetime.date(2020, 10, 15), datetime.date(2020, 10, 16))
]


@app.route('/', methods=['GET'])
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello World!\n <a href='/dashboard'> Go to dashboard </a>"

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # test_items.extend(update_calendar(my_ical))
    g.username = username
    g.fname = fname
    g.lname = lname

    #.where(u'userid', u'==', u'everestoreizy')

    docs = db.collection(u'tasks').stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

    g.item_collections = sort_items(test_items)
    return render_template('dashboard.html')

@app.route('/update_calendar', methods=['GET'])
def update_calendar():
    # ical = my_ical
    # calendar = Calendar(requests.get(ical).text)
    # planned_date = datetime.date(2020, 10, 13)
    # items = []
    # count = 0
    # for event in calendar.events:
        # items.append(Item(count, event.name, event.description, False, planned_date, event.begin))
        # count += 1
    # test_items.extend(items)
    return "Update successful"

@app.route('/account', methods=['GET'])
def account():
    return "/account under construction"

@app.route('/test/sayhello/<string:name>')
def test_sayhello(name):
    return f'Hello, {name}'

@app.route('/login/google')
def login_google():
    return render_template('google_login.html')

@app.route('/privacy')
def privacy():
    return "we don't sell your data"

@app.route('/tos')
def tos():
    return "need to write a terms of service"


if __name__ == '__main__':
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='localhost', port=8080, debug=True)
    
#so i remember
#dashboard_url = url_for('dashboard') #gets the url associated with the dashboard() function
#css_url = url_for('static', filename='style.css') #gets the url associated with static/style.css

# this exists: https://static.aspenplanner.appspot.com/static/css/style.css
# but dont use it
