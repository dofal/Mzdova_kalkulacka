
from flask import Flask, jsonify, render_template, request, session
import math

app = Flask(__name__)
app.secret_key = "jsiodjfiewnown7881U2HD912HND912"


@app.route("/", methods=["POST", "GET"] )
def home():
    
    if request.method == "POST":
        script = request.get_json()
        print(script)
        summ = script['summ']
        check = script['check']
        session["summ"] = summ
        session["check"] = check

    
       

    return render_template("home.html")

@app.route("/calculation", methods=["POST", "GET"])
def calculation():
   
    summ = int(session["summ"])
    check = session["check"]
    print(check)
    ### calculation ###

    tax = int(math.ceil(summ / 100.0)) * 100 * 0.15
    medical_tax = summ * 0.045
    social_tax = summ * 0.065

    

    

    if check == True:
        discount = "sleva uplatněna"
        if tax <= 2570:
            tax = 0
        else:
            tax = tax - 2570

    if check == False:
        discount = "sleva neuplatněna"

    result = summ - tax - math.ceil(medical_tax) - math.ceil(social_tax)

    return jsonify(' ',render_template("calculation.html", result = str(result), discount = discount, tax = tax, medical_tax = medical_tax, social_tax = social_tax))


if __name__ == "__main__":
    app.run(debug=True)
