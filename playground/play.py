from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')#flask listens for an http request
def play():
    return render_template("play.html")

@app.route('/play/<number>') #anything after play gets passed as a variable 
#alternatively you could write: @app.route('/play/<int:number>') //converts it in the url
def play_choice(number):
    print("\n\n\n", "-"*80, "Gangnam Style!!", "-"*80)
    return render_template('play.html', number=int(number))

# @app.route('/play/<int:number>/<color>')
# def play_more_choices(number, color):
#     print("\n\n\n", "*"*80, "Get it Poppin'!!!", "*"*80)
#     return render_template('play.html', number=number, color=color)




# if __name__=="__main__": #we know we are running this file directly and not importing it from a different module
app.run(debug=True)