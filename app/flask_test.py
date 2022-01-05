from flask import Flask, render_template
import datetime
app = Flask(__name__)

def calc():
    x = 10
    y = 20
    z = x * y
    return z

def funcmsg():
    val = "testmessage"
    return val

@app.route('/')
def index():
  dt_now = datetime.datetime.now()
  result = calc()
  values = { "name": "test", "date" : dt_now, "result" : result}
  return render_template('index.html', data=values)

# Second Page
@app.route("/msg")
def msg():
  message = funcmsg()
  values = { "message":"Hello! This is test page." , "funcmsg" : message}
  return render_template('msg.html', data=values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
