# AI-WORKFLOW.md

## AI Tools Used

- ChatGPT (GPT-5.5)

---

## How AI Was Used

AI was used to speed up development, generate React components, create FastAPI endpoints, debug frontend and backend issues, and explain implementation steps.

AI assisted with:
- Cleaning and preparing the dataset
- Creating FastAPI REST APIs
- Building the React dashboard
- Connecting React to FastAPI using Axios
- Creating charts using Recharts
- Debugging API integration issues

---

## Important Prompts

### Prompt 1

"Build a FastAPI backend that reads the cleaned booking dataset and returns dashboard metrics such as total bookings, revenue, booking channels, and property revenue."

---

### Prompt 2

"Create a React dashboard using Axios and Recharts that displays KPI cards, booking status, booking channels, revenue by property, and property health score."

---

### Prompt 3

"Help debug React and FastAPI integration and explain each step for testing the API and connecting the frontend."

---

## Example of AI Mistake

The AI initially generated frontend code that referenced data fields which were not yet available in the backend API response. This caused the dashboard to display errors.

I verified the API response by opening the `/metrics` endpoint in the browser, updated the FastAPI backend to return the missing fields, restarted the backend, and confirmed the frontend worked correctly.

---

## Reflection

AI significantly accelerated development by generating boilerplate code and suggesting solutions. However, every response was verified by testing the API, checking outputs, and fixing issues before accepting the generated code.