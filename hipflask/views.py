from watercooler.hipflask import app

@app.route("/")
def hello():
    return "Hello World!"
