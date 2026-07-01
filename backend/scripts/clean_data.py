import pandas as pd
import os

print("=" * 60)
print("FERNHILL STAYS - DATA CLEANING")
print("=" * 60)

# -----------------------------
# Load Dataset
# -----------------------------
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "bookings_jan_may_2026.csv")

df = pd.read_csv(file_path)

print(f"Original Rows: {len(df)}")

# -----------------------------
# Remove Duplicate Booking IDs
# -----------------------------
df = df.drop_duplicates(subset="booking_id", keep="first")

print(f"Rows after removing duplicate booking IDs: {len(df)}")

# -----------------------------
# Standardize Property Names
# -----------------------------
df["property"] = (
    df["property"]
    .str.strip()
    .str.title()
)

# -----------------------------
# Standardize Booking Channel
# -----------------------------
df["booking_channel"] = (
    df["booking_channel"]
    .fillna("Unknown")
    .str.strip()
    .str.title()
)

channel_mapping = {
    "Ota-Mmt": "OTA-MMT",
    "Ota-Booking": "OTA-Booking",
    "Direct": "Direct",
    "Corporate": "Corporate",
    "Walk-In": "Walk-In",
    "Unknown": "Unknown"
}

df["booking_channel"] = df["booking_channel"].replace(channel_mapping)
# -----------------------------
# Standardize Booking Status
# -----------------------------
df["status"] = (
    df["status"]
    .str.strip()
    .str.title()
)

status_mapping = {
    "Checked Out": "Checked-Out",
    "Checked-Out": "Checked-Out",
    "Confirmed": "Confirmed",
    "Cancelled": "Cancelled",
    "No-Show": "No-Show"
}

df["status"] = df["status"].replace(status_mapping)

# -----------------------------
# Convert Date
# -----------------------------
df["check_in_date"] = pd.to_datetime(
    df["check_in_date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

# -----------------------------
# Fill Missing Values
# -----------------------------
df["nightly_rate_inr"] = df["nightly_rate_inr"].fillna(
    df["nightly_rate_inr"].median()
)

df["total_amount_inr"] = df["total_amount_inr"].fillna(
    df["total_amount_inr"].median()
)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "bookings_cleaned.csv"
)

df.to_csv(output_path, index=False)

print("\nCleaning Completed Successfully!")
print(f"Cleaned file saved as:\n{output_path}")
print(f"Final Rows: {len(df)}")
print("=" * 60)