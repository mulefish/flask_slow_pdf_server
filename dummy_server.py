
from flask import Flask
from flask import request, send_from_directory, abort, jsonify
from flask_cors import CORS
import time
import os
import sys
import random

app = Flask(__name__)
CORS(app) # allow CORS for all domains on all routes

rel_path = "static{}".format(os.sep)

# PDF from https://www.learningcontainer.com/sample-pdf-files-for-testing/#Sample_PDF_File_for_Testing 
filename = "sample-pdf-download-10-mb.pdf"

@app.route("/", methods=["GET", "POST"])
def how_to_use_this():
    return "! use GET /really_slow or /really_slow?pause=3"
# localhost:5000/really_slow?pause=1 
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
        return send_from_directory(rel_path, filename, as_attachment=False)
    except FileNotFoundError:
        abort(404)


def _getRandomCategory():
    # pretend this categories make sense
    categories = []
    categories.append("blue")
    categories.append("ocean")
    categories.append("orange")
    categories.append("maggy")
    categories.append("shabone")
    categories.append("eeboo")
    categories.append("sawako")
    categories.append("sakm")
    categories.append("andy")
    categories.append("stuart")
    categories.append("randy")
    categories.append("doug")
    categories.append("suzette")
    categories.append("snickersnap")
    categories.append("venus")
    categories.append("mars")
    categories.append("jupiter")
    categories.append("finch")
    categories.append("wren")
    categories.append("swift")
    categories.append("bewick")

    return random.choice(categories)

# TODO - Remove this. I am building out the client axios and I just want a simple GET for now.
@app.route("/doc_hub_get", methods=["GET"])
def pretend_doc_hub_get():
    try:
        # Return back something from the json just to prove that
        # the json is being passed in correctly
        #

        result = {}
        result["loanId"] = "test"
        result["data"] = []

        not_finished_count = random.randint(1,10)
        is_finished_count = random.randint(1,10)

        i = 0
        for x in range(not_finished_count):
            x = {}
            x["category"] = _getRandomCategory()
            # random number between 0 and 1
            x["confidence"] = random.random()
            x["finished"] = False
            x["id"] = i
            i += 1
            result["data"].append(x)

        for x in range(is_finished_count):
            x = {}
            x["category"] = _getRandomCategory()
            # random number between 0 and 1
            x["confidence"] = random.random()
            x["finished"] = True
            x["id"] = i
            i += 1

            result["data"].append(x)
        print("pretend_doc_hub_get")
        return jsonify( result )

    except:
        # Bad form to be this open/sloppy but this is just a test
        bad_times = sys.exc_info()
        print( bad_times)
        return jsonify({"error":"Ack! Ill-formed json payload! (Most likely)"})






@app.route("/doc_hub", methods=["POST"])
def pretend_doc_hub():
    """
    Incoming json body ( with the optional 'forceCount' )
    {
        "loanId":"29292",
        "forceCount":"actually the value here does not matter, only the key"
    }
    
    Incoming json body ( without the optional 'forceCount' )
    {
        "loanId":"29292"
    }

    """
    try:
        # Return back something from the json just to prove that
        # the json is being passed in correctly
        content = request.json
        loadId = content["loanId"]
        result = {}
        result["loanId"] = loadId
        result["data"] = []

        not_finished_count = random.randint(1,10)
        is_finished_count = random.randint(1,10)
        if "forceCount" in content:
            not_finished_count = 6
            is_finished_count = 3

        i = 0
        for x in range(not_finished_count):
            x = {}
            x["category"] = _getRandomCategory()
            # random number between 0 and 1
            x["confidence"] = random.random()
            x["finished"] = False
            x["id"] = i
            i += 1
            result["data"].append(x)

        for x in range(is_finished_count):
            x = {}
            x["category"] = _getRandomCategory()
            # random number between 0 and 1
            x["confidence"] = random.random()
            x["finished"] = True
            x["id"] = i
            i += 1

            result["data"].append(x)


        print("pretend_doc_hub")
        print( jsonify( result ))

        return jsonify( result )

    except:
        # Bad form to be this open/sloppy but this is just a test
        bad_times = sys.exc_info()
        print( bad_times)
        return jsonify({"error":"Ack! Ill-formed json payload! (Most likely)"})


if __name__ == '__main__':
    port = 4040
    print("URL is localhost:{}".format(port ))
    app.run(port=4040)
