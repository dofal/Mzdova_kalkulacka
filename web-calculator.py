
# This Python file uses the following encoding: utf-8
from turtle import turtlesize
from flask import Flask, jsonify, render_template, request, session
import math

app = Flask(__name__)
app.secret_key = "jsiodjfiewnown7881U2HD912HND912"


@app.route("/", methods=["POST", "GET"] )
def home():
    
    ### data poslána ###
    if request.method == "POST":

        ### load data from fetch ###
        script = request.get_json()
        summ = script['summ']
        check = script['check']
        student = script["student"]
        handicap = script["handicap"]
        invalid = script["invalid"]
        kids = script["kids"]
        kids_handicap = script["kids_handicap"]
        
        
        ### make it global ###
        session["summ"] = summ
        session["check"] = check
        session["student"] = student
        session["handicap"] = handicap
        session["invalid"] = invalid
        session["kids"] = kids
        session["kids_handicap"] = kids_handicap

    
       

    return render_template("home.html")

@app.route("/calculation", methods=["POST", "GET"])
def calculation():
   
   ### get data from jQuery ###
    

    summ = request.args.get('summ', 0, type=int)
    check = request.args.get('check', 0, type=str)
    student = request.args.get('student', 0, type=str)
    handicap = request.args.get('handicap', 0, type=str)
    invalid = request.args.get('invalid', 0, type=str)
    kids = request.args.get('kids', 0, type=int)
    kids_handicap = request.args.get('kids_handicap', 0, type=int)

    print(summ, check, student, handicap, invalid)

    tax_basic = int(math.ceil(summ / 100.0)) * 100 ### hrubou mzdu musíme zaokrouhlit na stovky nahoru ###

    ### se solidární daní - nad částku 155644 ###
    if summ > 155644:
        higher = tax_basic - 155644
        lower = 155644
        lower = lower * 0.15
        higher = higher * 0.23
        tax = math.ceil(lower + higher)


    ### bez solidární daně - standartně 15% daň ###
    if summ <= 155644:
        tax = int(math.ceil(summ / 100.0)) * 100 * 0.15

    medical_tax = summ * 0.045
    social_tax = summ * 0.065

    ### děti ze str na int ###
    try:
        kids = int(kids)
    except ValueError:
        kids = None

    try:
        kids_handicap = int(kids_handicap)
    except ValueError:
        kids_handicap = 0

    ### Růžové prohlášení ano/ne ###
    if check == "true":
        discount = "sleva uplatněna"
        if tax <= 2570:
            tax = 0
        else:
            tax = tax - 2570

    else:
        discount = "sleva neuplatněna"

    ### student ano/ne ###
    if student == "true" and check == "true":
        if tax <= 335:
            tax = 0
        else:
            tax = tax - 335

    ### ZTP/P - 3 možnosti ###
    if handicap == "true" and check == "true":
        if tax <= 1345:
            tax = 0
        else:
            tax = tax - 1345
    
    if invalid == "1" and check == "true":
        if tax <= 210:
            tax = 0
        else:
            tax = tax - 210
    
    if invalid == "2" and check == "true":
        if tax <= 420:
            tax = 0
        else:
            tax = tax - 420
    
    
    ### daňový bonus - děti ###

    num_kids = 0 ### hlídač počtu dětí ###

    if kids is not None and check == "true" and summ >= 16200:
        if kids == 1:
            tax = tax - 1267
            num_kids += 1
        if kids == 2:
            tax = tax - 3127
            num_kids += 2
        if kids >= 3:
            tax = tax - (3127 + ((kids - 2) * 2320 ))
            num_kids += kids

    if num_kids <= 2:        
        num_kids = num_kids + 1

    if num_kids > 2:
        num_kids = 3

    ### daňový bonus - děti - hendikepované ###
    while kids_handicap != 0 and check == "true" and summ >= 16200:

        if num_kids == 1:
            tax = tax - 2534
            kids_handicap -= 1
            num_kids += 1
        elif num_kids == 2:
            tax = tax - 3720
            kids_handicap -= 1
            num_kids += 1
           
        else:
            tax = tax - 4640
            kids_handicap -= 1

    
    

    ### finální kalkulace čisté mzdy ###
    result = "{:,}".format(int( summ - tax - math.ceil(medical_tax) - math.ceil(social_tax))) + ",- Kč"
    tax = "{:,}".format(int(tax)) + ",- Kč"
    medical_tax ="{:,}".format(int(math.ceil(medical_tax))) + ",- Kč"
    social_tax ="{:,}".format(int(math.ceil(social_tax))) + ",- Kč"
    
    return jsonify(result = result, tax = tax, medical_tax = medical_tax, social_tax = social_tax)


if __name__ == "__main__":
    app.run(debug= True)
