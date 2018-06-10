from flask import Flask, render_template
app=Flask(__name__)


@app.route('/')
def index():
    users = (
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    );

    first_N = []
    last_N = []
    arr = []
    for first_name in users:
        first_N.append(first_name['first_name'])
    print(first_N)

    for last_name in users:
        last_N.append(last_name['last_name'])
    print(last_N)

    for person in users:
        first = person['first_name']
        last = person['last_name']
        full = person['first_name'] + " " +person['last_name']
        arr.append(full)
    print(arr)
    print(arr[0])
    
    return render_template('index.html', first=first_N, last=last_N, full=arr)
app.run(debug=True)