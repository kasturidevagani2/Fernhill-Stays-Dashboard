import pandas as pd
import os

print("=" * 60)
print("FERNHILL STAYS - BUSINESS METRICS")
print("=" * 60)

# -----------------------------
# Load Cleaned Dataset
# -----------------------------
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "bookings_cleaned.csv"
)

df = pd.read_csv(file_path)

# -----------------------------
# KPI Calculations
# -----------------------------

total_bookings = len(df)

total_revenue = df["total_amount_inr"].sum()

total_properties = df["property"].nunique()

total_guests = df["guests"].sum()

average_nightly_rate = df["nightly_rate_inr"].mean()

average_stay = df["nights"].mean()

print(f"Total Bookings        : {total_bookings}")
print(f"Total Revenue         : ₹ {total_revenue:,.2f}")
print(f"Total Properties      : {total_properties}")
print(f"Total Guests          : {total_guests}")
print(f"Average Nightly Rate  : ₹ {average_nightly_rate:.2f}")
print(f"Average Stay          : {average_stay:.2f} nights")

print("\n" + "=" * 60)
print("BOOKING STATUS")
print("=" * 60)

print(df["status"].value_counts())

print("\n" + "=" * 60)
print("BOOKING CHANNELS")
print("=" * 60)

print(df["booking_channel"].value_counts())