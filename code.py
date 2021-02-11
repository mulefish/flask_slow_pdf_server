# TODO: 
# Replace everything here with:
# https://github.com/Shopify/toxiproxy

from flask import Flask
from flask import request, send_from_directory, abort
import time

app = Flask(__name__)

abs_path  = "/Users/paul.montgomery/UWM/mocks/static/"
# PDF from https://www.learningcontainer.com/sample-pdf-files-for-testing/#Sample_PDF_File_for_Testing 
filename = "sample-pdf-download-10-mb.pdf"

@app.route("/", methods=["GET", "POST"])
def how_to_use_this():
    return "use GET /really_slow or /really_slow?pause=3"

# This serves up the PDF, but how to slow it down?
@app.route("/really_slow", methods=["GET"])
def really_slow():
    pause = int(request.args.get('pause'))
    if pause is None:
        pause = 0
    print( "really_slow() is about to pause for {} seconds ".format( pause))
    time.sleep(pause)
    print("really_slow() is done pausing")

    try:
        return send_from_directory(abs_path, filename, as_attachment=False)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run()