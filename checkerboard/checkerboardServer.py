from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def eightbyEight():
    print("Hello")
    return render_template('checkerboard.html', number=8)

@app.route('/(x)/(y)')
def board_change():
    print("WHAZUUUUUUUUUUP", "-"*200)
    # return render_template('checkerboard.html', x=int(x), y=int(y), color=color, alt_color=alt_color)#orange corresponds with html//white corresponds with the parameters
    return render_template('checkerboard.html', x=int(x), y=int(y))


app.run(debug=True)