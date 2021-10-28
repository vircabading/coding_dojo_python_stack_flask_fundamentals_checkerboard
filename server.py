# /////////////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python > Flask > Fundamentals: Playground
# By: Virgilio D. Cabading Jr.  Created: October 27, 2021
# /////////////////////////////////////////////////////////////////////

from flask import Flask, render_template                # Import Flask to allow us to create our app
app = Flask(__name__)                                   # Create a new instance of the Flask class called "app"

# **** Default App Route **********************************************
@app.route('/')                                         # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', hnum=8, vnum=8, lcolor='red', dcolor='black')

# **** /y *************************************************************
@app.route('/<int:vnum>')                             # The "@" decorator associates this route with the function immediately following
def index_vnum(vnum):
    return render_template('index.html', hnum=8, vnum=vnum, lcolor='red', dcolor='black')

# **** /x/y *************************************************************
@app.route('/<int:hnum>/<int:vnum>')                    # The "@" decorator associates this route with the function immediately following
def index_xnum_vnum(hnum,vnum):
    return render_template('index.html', hnum=hnum, vnum=vnum, lcolor='red', dcolor='black')

# **** /x/y/lcolor/dcolot ***********************************************
@app.route('/<int:hnum>/<int:vnum>/<string:lcolor>/<string:dcolor>')                    # The "@" decorator associates this route with the function immediately following
def index_xnum_vnum_color_color(hnum,vnum,lcolor,dcolor):
    return render_template('index.html', hnum=hnum, vnum=vnum, lcolor=lcolor, dcolor=dcolor)

# **** Handle invalid routes ******************************************
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.