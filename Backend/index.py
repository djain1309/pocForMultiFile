from flask import Flask, send_file
import io
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})




@app.route("/check", methods = ['POST', 'GET'])
def about():
    # This will return the 1.html, 2.html, and 3.html files.
    # all_html_files = ["./1.html", "./2.html", "./3.html", "./4.html"]
    # return send_file(all_html_files, mimetype="text/html")
    # # return "SECOND PAGE LOADED"
    html_files = ["1.html", "2.html", "3.html", "4.html"]
    content = ""
    for file_name in html_files:
        with open(file_name) as f:
            content += f.read()
    return send_file(io.BytesIO(content.encode()), mimetype="text/html")



@app.route("/", methods = ['POST', 'GET'])
def abouts():
    # This will return the 1.html, 2.html, and 3.html files.
    return "INDEX PAGE LOADED"

if __name__ == "__main__":
    app.run()
