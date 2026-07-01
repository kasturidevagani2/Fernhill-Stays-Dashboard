# TEST-REPORT.md

## Test Environment

Backend:
- FastAPI
- Python 3.x

Frontend:
- React + Vite

Browser:
- Google Chrome

---

# Tests Performed

## 1. API Testing

Test:
- Opened http://127.0.0.1:8000/metrics

Expected Result:
- JSON containing all dashboard metrics.

Result:
- Passed

---

## 2. Dashboard Loading

Test:
- Started React application.

Expected Result:
- Dashboard loads successfully.

Result:
- Passed

---

## 3. KPI Cards

Checked:

- Total Bookings
- Total Revenue
- Total Guests
- Total Properties
- Average Stay
- Average Nightly Rate

Result:
- All values displayed correctly.

---

## 4. Booking Status Chart

Expected:
- Pie chart should display booking status distribution.

Result:
- Passed

---

## 5. Booking Channels Chart

Expected:
- Bar chart should display booking channels.

Result:
- Passed

---

## 6. Revenue by Property

Expected:
- Bar chart should display revenue for each property.

Result:
- Passed

---

## 7. Property Health Score

Expected:
- Bar chart should display calculated health scores.

Result:
- Passed

---

# Data Validation

Verified:

- Duplicate bookings removed
- Missing values handled
- Standardized property names
- Standardized booking channels
- Revenue calculated from cleaned data

Result:
- Passed

---

# Issues Found During Development

Issue 1:
Frontend initially could not display some values because the backend API did not return all required fields.

Fix:
Updated the FastAPI API response and restarted the backend.

---

Issue 2:
React chart displayed empty data because the frontend referenced incorrect variable names.

Fix:
Updated the React code to use the correct API response fields.

---

# Edge Cases Tested

- Missing booking channel
- Missing nightly rate
- Duplicate booking IDs
- Inconsistent property names

Result:
Handled successfully after data cleaning.

---

# Known Limitation

The dashboard currently uses data from January to May 2026 only.

Future versions could support dynamic file uploads and filtering.