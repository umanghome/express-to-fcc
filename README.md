### Express your concerns to FCC regarding Net Neutrality by just filling 3 fields!

This is a Python application that shows a dead-simple HTML form that asks for a person's name, email, and address and submits a Comment to FCC regarding Net Neutrality.

Requires PhantomJS on the server to work.

On the server, do the following:
1. Install `phantomjs`
2. Clone this repository.
3. `pip install splinter flask`
4. `python server.py 0.0.0.0 80 domain.com`

`index.html` contains the HTML page that contains the form.