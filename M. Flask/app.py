from flask import Flask , request


app = Flask("__name__")

@app.route("/")
def home_page():
    return "<h1> Home </h1>"
 

about_us = "<body style=\"background-color: cyan;\"> <h1>About Me</h1></body>"
@app.route("/about")
def about_page():
    return about_us

@app.route("/contact")
def contact_page():
    return "<h1> Contact Us </h1>"

#get a data from request
@app.route("/checking")
def get_data_from_url():
    data = request.args.get("x")
    return f"You are checking for <h1 style=\"display:inline-block\">{data}?</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")