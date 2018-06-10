from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    print("YOLO")
    return render_template('index.html')

@app.route('/<int:x>/<int:y>')
def flexMatrix(x,y):
    print("is this thing on?")
    return render_template('index.html', column=x, row=y)

app.run(debug=True)