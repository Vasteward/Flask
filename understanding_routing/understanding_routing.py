from flask import Flask
app = Flask(__name__)
print (__name__)


#say "Hello World!" 
@app.route('/')
def hello_world():
    return "Hello World!"
# say "Dojo!"
@app.route('/dojo')
def dojo():
    print("The Dojo is where it's at!!")
    return "Dojo!"

##VARIABLE RULES
#have it say Hi to flask, Michael, and john when writing different url request in the same function
@app.route('/say/<username>')
def say(username):
    print("Just said hi, check your browser B)")
    return 'Hello %s' % username # need the % sign between the string and the variable because it is valid syntax
    #don't hardcode this. Realistically, you can't expect to do this for every single person that uses your site ex. # say("Flask")

#INT and multiply
@app.route('/repeat/<num>/<word>')
def hello(num, word):
    print("let's hope this prints hello 35 times", "\n\n\n", "-"*80)
    return word*int(num)

app.run(debug=True)#run application ran earlier and run in debug mode to see any errors in browser
