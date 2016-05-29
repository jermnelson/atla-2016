__author__ = "Jeremy Nelson"

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
@app.route("/")
def page(name=None):
    if name is None:
        template_name = "index.html"
    else:
        template_name = "{}.html".format(name)
    return render_template(template_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
