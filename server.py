from flask import Flask, request, send_from_directory
from splinter import Browser

FLASK_PORT = 80

url = 'https://www.fcc.gov/ecfs/search/proceedings?q=name:((17-108))'

app = Flask(__name__)

app.run(port=FLASK_PORT)

@app.route('/', methods=['GET', 'POST'])
def index_route ():
    if request.method == 'GET':
        return send_from_directory('static', 'index.html')
    print request.form
    browser = Browser('phantomjs')

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

    # Show confirmation number
    return 'Confirmation number: ' + number