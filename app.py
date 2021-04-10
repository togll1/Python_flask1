from flask import Flask,render_template
import jungbo as jb

jb.make_name()
jb.make_url()
urls = jb.urls
names = jb.names

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",
        urls = urls,
        names = names,
        count = jb.count,)

if __name__ == '__main__':
    app.run(debug=True)

    