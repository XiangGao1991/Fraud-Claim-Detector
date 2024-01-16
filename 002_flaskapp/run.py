from flask import Flask, jsonify, request, render_template
import json
import numpy as np
import joblib
import pandas as pd
from processor import ProcessorIP, ProcessorOP

IP_model = joblib.load('IP_model.joblib')
OP_model = joblib.load('OP_model.joblib')
IP_processor = joblib.load('IP_processor.joblib')
IP_one_hot_encoder = joblib.load('IP_one_hot_encoder.joblib')
OP_processor = joblib.load('OP_processor.joblib')
OP_one_hot_encoder = joblib.load('OP_one_hot_encoder.joblib')

app = Flask(__name__)



@app.route('/',methods=["GET","POST"])
def index():
    pred = ""
    form_data = {}
    if request.method == "POST":
        # raw data
        patient_type = None
        form_data = request.form        
        patient_type = request.form.get('patientType')
        ClaimStartDt = request.form["ClaimStartDt"]
        ClaimEndDt = request.form["ClaimEndDt"]
        AttendingPhysician = request.form["AttendingPhysician"]
        InscClaimAmtReimbursed = request.form["InscClaimAmtReimbursed"]
        IPAnnualReimbursementAmt = request.form["IPAnnualReimbursementAmt"]
        State = request.form["State"]
        Race = request.form["Race"]
        ClmAdmitDiagnosisCode = request.form["ClmAdmitDiagnosisCode"]
        DiagnosisGroupCode = request.form["DiagnosisGroupCode"]
        ClmDiagnosisCode_1 = request.form["ClmDiagnosisCode_1"]
        ClmProcedureCode_1 = request.form["ClmProcedureCode_1"]
        data = {}

        if not patient_type:
            pred = "Please select claim type(Inpatient/Outpatient)."
            return render_template("index.html", pred = pred, form_data = form_data)

        if patient_type=="inpatient":
            preprocessor = IP_processor
            one_hot_encoder = IP_one_hot_encoder
            model = IP_model

            data["ClaimStartDt"] = ClaimStartDt
            data["ClaimEndDt"] = ClaimEndDt
            data["AttendingPhysician"] = AttendingPhysician

            try: 
                data["InscClaimAmtReimbursed"] = int(InscClaimAmtReimbursed)
            except:
                pred = "Please type valid InscClaimAmtReimbursed value."
                return render_template("index.html", pred = pred, form_data = form_data)

            try:
                data["IPAnnualReimbursementAmt"] = int(IPAnnualReimbursementAmt)
            except:
                pred = "Please type valid IPAnnualReimbursementAmt value."
                return render_template("index.html", pred = pred, form_data = form_data)

            try:
                data["State"] = int(State)
            except:
                pred = "Please type valid State code."
                return render_template("index.html", pred = pred, form_data = form_data)

            if len(ClmAdmitDiagnosisCode)==0:
                pred = "Please type valid Claim Admit Diagnosis Code."
                return render_template("index.html", pred = pred, form_data = form_data)
            data["ClmAdmitDiagnosisCode"] = ClmAdmitDiagnosisCode

            if len(DiagnosisGroupCode)==0:
                pred = "Please type valid Diagnosis Group Code."
                return render_template("index.html", pred = pred, form_data = form_data)
            data["DiagnosisGroupCode"] = DiagnosisGroupCode

            if len(ClmDiagnosisCode_1)==0:
                pred = "Please type valid Claim Diagnosis Code."
                return render_template("index.html", pred = pred, form_data = form_data)
            data["ClmDiagnosisCode_1"] = ClmDiagnosisCode_1

            try:
                data["ClmProcedureCode_1"] = int(ClmProcedureCode_1)
            except:
                pred = "Please type valid Claim Procedure Code."
                return render_template("index.html", pred = pred, form_data = form_data)

        if patient_type=="outpatient":
            preprocessor = OP_processor
            one_hot_encoder = OP_one_hot_encoder
            model = OP_model     

            data["AttendingPhysician"] = AttendingPhysician

            try: 
                data["InscClaimAmtReimbursed"] = int(InscClaimAmtReimbursed)
            except:
                pred = "Please type valid InscClaimAmtReimbursed value."
                return render_template("index.html", pred = pred, form_data = form_data)
            
            try:
                data["Race"] = int(Race)
            except:
                pred = "Please type valid Race value."
                return render_template("index.html", pred = pred, form_data = form_data)

            try:
                data["State"] = int(State)
            except:
                pred = "Please type valid State code."
                return render_template("index.html", pred = pred, form_data = form_data)

            if len(ClmDiagnosisCode_1)==0:
                pred = "Please type valid Claim Diagnosis Code."
                return render_template("index.html", pred = pred, form_data = form_data)
            data["ClmDiagnosisCode_1"] = ClmDiagnosisCode_1
        
        df = pd.DataFrame({0:data}).T
        
        df_transform = preprocessor.transform(df)
        df_transform = one_hot_encoder.transform(df_transform)
        pred = model.predict(df_transform)
        prob = model.predict_proba(df_transform)[0][1] * 100
        print(prob)
        if pred[0] == 0:
            pred = f"This may not be a fraudulent claim due to its probability {prob:.2f}%"
        else:
            pred = f"Note! This may be a fraudulent claim due to its probability {prob:.2f}%"
        
        return render_template("index.html", pred = pred, form_data = form_data)
    
    return render_template("index.html", pred = pred, form_data = form_data)

if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port=5000)