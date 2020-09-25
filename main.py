<<<<<<< HEAD
<<<<<<< HEAD
import flask
import os
import random
=======
import flask,os,random
>>>>>>> 464601109f17a12ff618ba26c93df8960c343362
=======
import flask,os,random
>>>>>>> wesSetup

app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():
    return flask.render_template("index.html")
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
