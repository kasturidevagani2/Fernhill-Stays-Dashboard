import { useEffect, useState } from "react";
import axios from "axios";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
  LineChart,
  Line
} from "recharts";
const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042"];

function App() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    axios
      .get("/metrics")
      .then((res) => setMetrics(res.data))
      .catch((err) => console.error(err));
  }, []);

  if (!metrics) {
    return <h2 style={{ padding: "30px" }}>Loading Dashboard...</h2>;
  }

  const statusData = Object.entries(metrics.booking_status).map(
    ([name, value]) => ({
      name,
      value,
    })
  );

  const channelData = Object.entries(metrics.booking_channels).map(
    ([channel, bookings]) => ({
      channel,
      bookings,
    })
  );
  const propertyData = Object.entries(metrics.property_revenue || {}).map(
  ([name, value]) => ({
    property: name,
    revenue: value,
  })
  );
  const healthData = Object.entries(metrics.property_health).map(
  ([property, health]) => ({
    property,
    health,
  })
);
const monthlyData = Object.entries(metrics.monthly_revenue).map(
  ([month, revenue]) => ({
    month,
    revenue,
  })
);

console.log(healthData);
  const cardStyle = {
    background: "#fff",
    borderRadius: "12px",
    padding: "20px",
    textAlign: "center",
    boxShadow: "0 2px 8px rgba(0,0,0,0.15)",
  };

  return (
    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
        background: "#f4f6f9",
        minHeight: "100vh",
      }}
    >
      <h1>🏨 Fernhill Stays Analytics Dashboard</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3,1fr)",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        <div style={cardStyle}>
          <h3>Total Bookings</h3>
          <h2>{metrics.total_bookings}</h2>
        </div>

        <div style={cardStyle}>
          <h3>Total Revenue</h3>
          <h2>₹ {metrics.total_revenue.toLocaleString()}</h2>
        </div>

        <div style={cardStyle}>
          <h3>Total Guests</h3>
          <h2>{metrics.total_guests}</h2>
        </div>

        <div style={cardStyle}>
          <h3>Total Properties</h3>
          <h2>{metrics.total_properties}</h2>
        </div>

        <div style={cardStyle}>
          <h3>Average Stay</h3>
          <h2>{metrics.average_stay} Nights</h2>
        </div>

        <div style={cardStyle}>
          <h3>Average Nightly Rate</h3>
          <h2>₹ {metrics.average_nightly_rate}</h2>
          
        </div>
        <div style={cardStyle}>
  <h3>🏆 Top Property</h3>

  <h2>{metrics.top_property}</h2>

  <p>
    ₹ {metrics.top_property_revenue.toLocaleString()}
  </p>
</div>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "30px",
          marginTop: "50px",
        }}
      >
        <div style={cardStyle}>
          <h2>Booking Status</h2>

          <ResponsiveContainer width="100%" height={350}>
            <PieChart>
              <Pie
                data={statusData}
                dataKey="value"
                nameKey="name"
                outerRadius={120}
                label
              >
                {statusData.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>

              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div style={cardStyle}>
          <h2>Booking Channels</h2>

          <ResponsiveContainer width="100%" height={350}>
            <BarChart data={channelData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="channel" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="bookings" fill="#0088FE" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
      <div
        style={{
          background: "white",
          padding: 20,
          borderRadius: 12,
          marginTop: 30,
          boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
        }}
      >
        <h2 style={{ textAlign: "center" }}>
          Revenue by Property
        </h2>

        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={propertyData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="property" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar
              dataKey="revenue"
              fill="#4CAF50"
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div
  style={{
    background: "white",
    padding: 20,
    borderRadius: 12,
    marginTop: 30,
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
  }}
>
  <h2 style={{ textAlign: "center" }}>
    Property Health Score
  </h2>

  <ResponsiveContainer width="100%" height={400}>
    <BarChart data={healthData}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="property" />
      <YAxis domain={[0, 100]} />
      <Tooltip />
      <Legend />
      <Bar dataKey="health" fill="#FF8042" />
    </BarChart>
  </ResponsiveContainer>
</div>
<div style={{ ...cardStyle, marginTop: "40px" }}>
  <h2>Monthly Revenue Trend</h2>

  <ResponsiveContainer width="100%" height={350}>
    <LineChart data={monthlyData}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="month" />
      <YAxis />
      <Tooltip />
      <Legend />

      <Line
        type="monotone"
        dataKey="revenue"
        stroke="#1976d2"
        strokeWidth={3}
      />
    </LineChart>
  </ResponsiveContainer>
</div>
    </div>
  );
}

export default App;