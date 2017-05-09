from flask import Flask, request, send_from_directory
from splinter import Browser
import sys

FLASK_PORT = 5005
BROWSER_TO_USE = 'phantomjs'
IP_TO_USE = '0.0.0.0'
SERVER_NAME = 'ffd51ee2.ngrok.io'

if len(sys.argv) != 4:
    print 'Usage: python server.py <IP to use> <Port to use> <Server Name>'

IP_TO_USE = sys.argv[1]
FLASK_PORT = sys.argv[2]
SERVER_NAME = sys.agrv[3]

url = 'https://www.fcc.gov/ecfs/search/proceedings?q=name:((17-108))'

app = Flask(__name__)
app.config['SERVER_NAME'] = SERVER_NAME

@app.route('/')
def index_route ():
    return send_from_directory("", 'index.html')

@app.route('/submit-us', methods=['POST'])
def submit_us ():
    print request.form

    required_keys = ['name', 'email', 'address', 'city', 'state', 'zip', 'comments']
    for r in required_keys:
        if not request.form.has_key(r):
            return 'Please enter all fiels!', 400

    browser = Browser(BROWSER_TO_USE)

    # Visit URL
    browser.visit(url)

    # Click +Express
    browser.find_by_css('#printElement > tbody > tr > td > div:nth-child(1) > div.col-lg-3.text-right > a:nth-child(2)').first.click()

    # Fill Name
    browser.find_by_css('#signupform > div:nth-child(3) > div.col-sm-10 > div > div > input').first.fill(request.form['name'] + '\n')

    # Fill Email
    browser.find_by_css('#email').first.fill(request.form['email'])

    # Fill Address
    browser.find_by_css('#address1').first.fill(request.form['address'])

    # Fill City
    browser.find_by_css('#city').first.fill(request.form['city'])

    # Select State
    browser.find_by_css('#userstate').first.select(request.form['state'])

    # Fill Zip
    browser.find_by_css('#zip').first.fill(request.form['zip'])

    # Fill Comment
    browser.find_by_css('#briefComment').fill(request.form['comments'])

    # Submit
    browser.find_by_css('#signupform > div.col-sm-offset-2 > div > div > a').first.click()
    browser.find_by_css('#signupform > div:nth-child(8) > div > div > button').first.click()

    # Get confirmation number
    number = browser.find_by_css('#confirmation').first.text

    # Show confirmation number
    return 'Confirmation number: ' + number

@app.route('/submit-international', methods=['POST'])
def submit_international ():
    print request.form

    required_keys = ['name', 'email', 'address', 'comments']
    for r in required_keys:
        if not request.form.has_key(r):
            return 'Please enter all fiels!', 400

    browser = Browser(BROWSER_TO_USE)

    # Visit URL
    browser.visit(url)

    # Click +Express
    browser.find_by_css('#printElement > tbody > tr > td > div:nth-child(1) > div.col-lg-3.text-right > a:nth-child(2)').first.click()

    # Fill Name
    browser.find_by_css('#signupform > div:nth-child(3) > div.col-sm-10 > div > div > input').first.fill(request.form['name'] + '\n')

    # Check checkbox for International Address
    browser.find_by_css('#interAddCheck').first.check()

    # Fill Email
    browser.find_by_css('#email').first.fill(request.form['email'])

    # Fill Address
    browser.find_by_css('#internationaladdressentity').first.fill(request.form['address'])

    # Fill Comment
    browser.find_by_css('#briefComment').fill(request.form['comments'])

    # Submit
    browser.find_by_css('#signupform > div.col-sm-offset-2 > div > div > a').first.click()
    browser.find_by_css('#signupform > div:nth-child(8) > div > div > button').first.click()

    # Get confirmation number
    number = browser.find_by_css('#confirmation').first.text

    print number

    browser.quit()

    # Show confirmation number
    return 'Confirmation number: ' + number

if __name__ == '__main__':
    app.run(port=FLASK_PORT)
