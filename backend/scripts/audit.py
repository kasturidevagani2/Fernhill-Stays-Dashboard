import pandas as pd

# Load dataset
df = pd.read_csv("data/bookings_jan_may_2026.csv")

print("=" * 60)
print("FERNHILL STAYS - DATA AUDIT")
print("=" * 60)

# Dataset information
print(f"\nTotal Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

# -----------------------------
# Missing Values
# -----------------------------
print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# -----------------------------
# Duplicate Rows
# -----------------------------
print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

print("Duplicate Rows :", df.duplicated().sum())

# -----------------------------
# Duplicate Booking IDs
# -----------------------------
print("\n" + "=" * 60)
print("DUPLICATE BOOKING IDs")
print("=" * 60)

print(df["booking_id"].duplicated().sum())

# -----------------------------
# Unique Booking Status
# -----------------------------
print("\n" + "=" * 60)
print("BOOKING STATUS")
print("=" * 60)

print(df["status"].value_counts())

# -----------------------------
# Booking Channels
# -----------------------------
print("\n" + "=" * 60)
print("BOOKING CHANNELS")
print("=" * 60)

print(df["booking_channel"].value_counts())

# -----------------------------
# Property Names
# -----------------------------
print("\n" + "=" * 60)
print("PROPERTY NAMES")
print("=" * 60)

print(df["property"].value_counts())

# -----------------------------
# Revenue Statistics
# -----------------------------
print("\n" + "=" * 60)
print("REVENUE SUMMARY")
print("=" * 60)

print(df["total_amount_inr"].describe())

# -----------------------------
# Date Conversion
# -----------------------------
# -----------------------------
# Date Validation
# -----------------------------

print("\n" + "=" * 60)
print("DATE VALIDATION")
print("=" * 60)

df["check_in_date"] = pd.to_datetime(
    df["check_in_date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

print("Invalid Dates :", df["check_in_date"].isnull().sum())