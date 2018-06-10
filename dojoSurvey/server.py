from flask import Flask, render_template, redirect, request, session
#pullin request so we can use request
app=Flask(__name__)
app.secret_key = "nunya"

@app.route('/')
def index():
    print("Is this thing on?")
    return render_template("table.html")


#session isn't tied to forms-not interdependent

#redirect to the url that will render the page
#we redirect to a route
#process function
@app.route('/danger', methods=['POST'])
def process():
    #1
    #get the data from the form dictionary
    the_name = request.form["name"]
    # put that data in the section dict
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]

    # session["logged"] = True
    print(request)
    print("*"*20)
    print(request.form)
    return redirect('/result')
    #we redirect to a route



#tells another function to fire
#render function
@app.route('/result')
def result():
    print('information has been submitted and will put up the right page')
    #do something with the data we got from post
    # refreshing redoes what the request just made
    #2
    name = session["name"]
    location = session["location"]
    language = session["language"]
    comment = session["comment"]
    print("-"*100)
    print(session)
    print("-"*100)
    #have the variables render to the page 
    return render_template("results.html", the_name = name, the_location=location, the_language=language, the_comment=comment)

#handles form submission






app.run(debug=True)