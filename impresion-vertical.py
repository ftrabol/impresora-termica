import os, sys, base64
import win32print
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG']      = False
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
 
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "code":404,
        "message":str("no found")
    })

@app.route("/thermalPrinter/<string:base64code>", methods = ['GET','POST'])
@cross_origin()
def thermalPrinter(base64code):
    
    try:
        raw_str     = str(base64code)
        raw_base    = base64.b64decode(raw_str)
        data        = bytes(raw_base)
        nameprinter = win32print.GetDefaultPrinter()
        
        hPrinter = win32print.OpenPrinter(nameprinter)
        win32print.StartDocPrinter(hPrinter, 1, ("Print data otros pagos", None, "RAW"))

        try:
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, data)
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)
            win32print.ClosePrinter(hPrinter)

        except Exception as e:

            return jsonify({
                "code":500,
                "message":str(e.message)
            })
    except Exception as e:
        return jsonify({
            "code":500,
            "message":str(e.message)
        })
    return jsonify({
        "code":200,
        "message":"printer!!!"
    })

if __name__ == "__main__":
    app.run()