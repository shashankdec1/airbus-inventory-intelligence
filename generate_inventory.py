import pandas as pd
import random

parts = [
    "Hydraulic Actuator",
    "Fuel Control Valve",
    "Landing Gear Bolt",
    "Turbine Blade",
    "Avionics Sensor",
    "Brake Assembly",
    "Cockpit Display",
    "Engine Filter",
    "Pressure Sensor",
    "Navigation Unit",
    "Radar Module",
    "Wing Fastener",
    "Hydraulic Pump",
    "Compressor Blade",
    "Electrical Harness"
]

categories = [
    "Hydraulics",
    "Fuel System",
    "Landing Gear",
    "Engine",
    "Avionics",
    "Electronics"
]

data = []

for i in range(1, 201):

    data.append({

        "Part_Number": f"A{i:04}",

        "Part_Name": random.choice(parts),

        "Category": random.choice(categories),

        "Current_Stock": random.randint(10, 500),

        "Unit_Cost": random.randint(50, 5000),

        "Lead_Time_Days": random.randint(5, 30),

        "Monthly_Demand": random.randint(5, 100)

    })

df = pd.DataFrame(data)

df.to_csv(
    "sample_inventory.csv",
    index=False
)

print("200 records created successfully")