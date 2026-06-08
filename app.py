from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

app.config["SECRET_KEY"] = "airbus-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventory.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# DATABASE MODEL

class Inventory(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    part_number = db.Column(db.String(100))
    part_name = db.Column(db.String(200))
    category = db.Column(db.String(100))

    current_stock = db.Column(db.Integer)
    unit_cost = db.Column(db.Float)

    lead_time_days = db.Column(db.Integer)
    monthly_demand = db.Column(db.Integer)


with app.app_context():
    db.create_all()



# UPLOAD ROUTE

@app.route("/")
@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["file"]

        df = pd.read_csv(file)

        Inventory.query.delete()

        for _, row in df.iterrows():

            db.session.add(
                Inventory(
                    part_number=row["Part_Number"],
                    part_name=row["Part_Name"],
                    category=row["Category"],
                    current_stock=row["Current_Stock"],
                    unit_cost=row["Unit_Cost"],
                    lead_time_days=row["Lead_Time_Days"],
                    monthly_demand=row["Monthly_Demand"]
                )
            )

        db.session.commit()

        flash(
            f"{len(df)} records uploaded successfully",
            "success"
        )

        return redirect("/dashboard")

    return render_template("upload.html")



# DASHBOARD

@app.route("/dashboard")
def dashboard():

    items = Inventory.query.all()

    total_parts = len(items)

    inventory_value = round(
        sum(i.current_stock * i.unit_cost for i in items),
        2
    )

    low_stock = len([
        i for i in items
        if i.current_stock < i.monthly_demand
    ])

    avg_stock = round(
        sum(i.current_stock for i in items) / total_parts,
        2
    ) if total_parts else 0

    category_summary = {}

    for item in items:

        category_summary[item.category] = (
            category_summary.get(item.category, 0) + 1
        )

    return render_template(
        "dashboard.html",
        total_parts=total_parts,
        inventory_value=inventory_value,
        low_stock=low_stock,
        avg_stock=avg_stock,
        category_labels=list(category_summary.keys()),
        category_values=list(category_summary.values())
    )



# ABC ANALYSIS

@app.route("/abc-analysis")
def abc_analysis():

    items = Inventory.query.all()

    inventory_data = []

    for item in items:

        inventory_data.append({
            "part_number": item.part_number,
            "part_name": item.part_name,
            "value": item.current_stock * item.unit_cost
        })

    inventory_data.sort(
        key=lambda x: x["value"],
        reverse=True
    )

    total_value = sum(
        item["value"]
        for item in inventory_data
    )

    cumulative = 0

    for item in inventory_data:

        cumulative += item["value"]

        percentage = (
            cumulative / total_value
        ) * 100 if total_value else 0

        if percentage <= 80:
            item["class"] = "A"

        elif percentage <= 95:
            item["class"] = "B"

        else:
            item["class"] = "C"

    return render_template(
        "abc.html",
        inventory_data=inventory_data
    )



# FORECASTING

@app.route("/forecasting")
def forecasting():

    items = Inventory.query.all()

    forecast_data = [

        {
            "part_number": i.part_number,
            "part_name": i.part_name,
            "current_demand": i.monthly_demand,
            "forecast": round(
                i.monthly_demand * 1.10,
                2
            )
        }

        for i in items

    ]

    return render_template(
        "forecasting.html",
        forecast_data=forecast_data
    )



# REORDER POINT

@app.route("/reorder-point")
def reorder_point():

    items = Inventory.query.all()

    reorder_data = []

    for item in items:

        rop = round(
            (item.monthly_demand / 30)
            * item.lead_time_days,
            2
        )

        reorder_data.append({

            "part_number": item.part_number,
            "part_name": item.part_name,
            "current_stock": item.current_stock,
            "rop": rop,
            "status":
                "REORDER"
                if item.current_stock <= rop
                else "SAFE"

        })

    return render_template(
        "reorder.html",
        reorder_data=reorder_data
    )



# API

@app.route("/api/inventory")
def inventory_api():

    items = Inventory.query.all()

    return jsonify([

        {
            "part_number": i.part_number,
            "part_name": i.part_name,
            "category": i.category,
            "current_stock": i.current_stock,
            "unit_cost": i.unit_cost,
            "lead_time_days": i.lead_time_days,
            "monthly_demand": i.monthly_demand
        }

        for i in items

    ])



# RUN APPLICATION

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )