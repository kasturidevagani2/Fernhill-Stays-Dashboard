from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pandas as pd
import os

app = FastAPI(title="Fernhill Stays API")

# Allow React frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Load Cleaned Dataset
# -----------------------------
file_path = os.path.join(
    os.path.dirname(__file__),
    "data",
    "bookings_cleaned.csv"
)

df = pd.read_csv(file_path)

frontend_dist = Path(__file__).resolve().parent.parent / "frontend" / "dist"
if frontend_dist.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dist), html=True), name="static")


@app.get("/metrics")
def metrics():

    total_bookings = len(df)

    total_revenue = float(df["total_amount_inr"].sum())

    total_properties = int(df["property"].nunique())

    total_guests = int(df["guests"].sum())

    average_nightly_rate = round(
        float(df["nightly_rate_inr"].mean()),
        2
    )

    average_stay = round(
        float(df["nights"].mean()),
        2
    )

    booking_status = (
        df["status"]
        .value_counts()
        .to_dict()
    )

    booking_channels = (
        df["booking_channel"]
        .value_counts()
        .to_dict()
    )

    property_revenue = (
        df.groupby("property")["total_amount_inr"]
        .sum()
        .to_dict()
    )

    property_bookings = (
        df.groupby("property")
        .size()
        .to_dict()
    )

    property_health = {}

    for property_name in property_revenue:
        revenue = property_revenue[property_name]
        bookings = property_bookings[property_name]

        score = (revenue / 20000) + (bookings * 2)

        if score > 100:
            score = 100

        property_health[property_name] = round(score, 1)
        # Monthly Revenue
    df["check_in_date"] = pd.to_datetime(df["check_in_date"])

    monthly_revenue = (
        df.groupby(df["check_in_date"].dt.strftime("%b"))["total_amount_inr"]
        .sum()
        .reindex(["Jan", "Feb", "Mar", "Apr", "May"])
        .fillna(0)
        .to_dict()
    )
    top_property = max(
    property_revenue,
    key=property_revenue.get
)  

    return {
        "total_bookings": total_bookings,
        "total_revenue": total_revenue,
        "total_properties": total_properties,
        "total_guests": total_guests,
        "average_nightly_rate": average_nightly_rate,
        "average_stay": average_stay,
        "booking_status": booking_status,
        "booking_channels": booking_channels,
        "property_revenue": property_revenue,
        "property_health": property_health,
        "monthly_revenue": monthly_revenue,
        "top_property": top_property,
        "top_property_revenue": property_revenue[top_property]
    }