from flask import Flask 

app = Flask(__name__)


@app.route("/endpoint1")
def forecastResult():
    return {"AppName": {
        "Ecpected Downloads": 25,
        "Time Series": 25,
        "Sucess" : "Yes"
        }}
