# DECISIONS.md

## Data Cleaning Decisions

### 1. Duplicate Booking IDs
Decision:
- Removed duplicate booking IDs and kept the first occurrence.

Reason:
- Every booking should have a unique booking ID.
- Duplicate bookings would increase booking counts and revenue incorrectly.

---

### 2. Missing Booking Channel

Decision:
- Replaced missing booking channels with "Unknown".

Reason:
- Removing these records would lose booking information.
- Using "Unknown" keeps the data complete while identifying missing values.

---

### 3. Missing Nightly Rate

Decision:
- Filled missing nightly rates using the median nightly rate.

Reason:
- The median is less affected by extreme values than the mean.

---

### 4. Missing Total Amount

Decision:
- Recalculated missing total amounts using:

Total Amount = Nights × Nightly Rate

Reason:
- This keeps revenue calculations consistent.

---

### 5. Standardized Property Names

Examples:

Palm grove inn → Palm Grove Inn

cedar court → Cedar Court

MARIGOLD SUITES → Marigold Suites

Reason:
- Different spellings represented the same property.
- Standardization prevents duplicate property names.

---

### 6. Standardized Booking Status

Examples:

confirmed → Confirmed

CHECKED OUT → Checked-Out

Reason:
- Consistent values improve reporting accuracy.

---

### 7. Standardized Booking Channels

Examples:

direct → Direct

ota-mmt → OTA-MMT

walk-in → Walk-In

Reason:
- Consistent naming improves chart accuracy.

---

## Dashboard Decisions

Business KPIs selected:

- Total Bookings
- Total Revenue
- Total Guests
- Total Properties
- Average Stay
- Average Nightly Rate

Charts Selected:

- Booking Status Distribution
- Booking Channels
- Revenue by Property
- Property Health Score

Reason:
These charts directly answer the client's business questions and provide clear insights into property performance and booking behavior.