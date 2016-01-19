from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

SHAKES_INSULTS = [
    'barnacle', 'boar-pig', 'pignut', 'pugnut', 'miscreant', 'ratsbane', 'whey-face', 'lout', 'nincompoop',
    'measle','bugbear','pigeon-egg','haggard horn-beast', 'beslubbering hedge-pig'
    ]

@app.route('/')
def start_here():
    """Home page."""

    return """Hi! This is the home page. <br> 
              Click <a href=\"/hello\">here</a> for a 
              super-duper-awesome greeting generator."""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1> 
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          Choose an adjective  <!-- <select name="compliment">
            <option value="terrific">terrific</option>
             <option value="neato">neato</option>
             <option value="fantabulous">fantabulous</option>
             <option value="smashing">smashing</option> -->

          <input type="radio" name="compliment" value="awesome">awesome
          <input type="radio" name="compliment" value="wowza">wowza
          <input type="radio" name="compliment" value="neato">neato
          <br>
          <input type="submit">
        </form> 

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    # compliment = choice(AWESOMENESS)
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def insult_person():
    """Get user by name."""

    player = request.args.get("person")
    diss = choice(SHAKES_INSULTS)
    return """
    <!doctype html>
    <html>
      <head>
        <title>How Insulting</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, diss)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
