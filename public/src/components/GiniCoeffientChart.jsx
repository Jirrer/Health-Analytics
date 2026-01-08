import { useEffect, useState } from "react";
import {Chart as ChartJS } from "chart.js/auto";
import { Bar, Doughnut, Line } from "react-chartjs-2";

const GiniCoeffientChart = ({ selectedRegion }) => { // AI slop
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const BACKEND_URL =
  process.env.NODE_ENV === "development"
    ? "http://localhost:5050"     
    : "/health_analytics_backend";

  useEffect(() => {
    if (!selectedRegion) return; 

    setLoading(true);

    setData(null);

    fetch(`${BACKEND_URL}/get-gini-coeffient`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        region: selectedRegion
      })
    })
      .then(res => {
        if (!res.ok) throw new Error("Request failed");
        return res.json();
      })
      .then(data => setData(data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
      
  }, [selectedRegion]);

    const handleData = () => {
      if (!data) return <div></div>;            
      if (!data[selectedRegion]) return <div>No data found</div>; 

      const countyData = data[selectedRegion];              
      
      return<div className="LineChart">
        <Line
          data={{
            labels: countyData.map(item => item[0]),
            datasets: [
              {
                label: "Gini Coeffient",
                data: countyData.map(item => item[1]),
                backgroundColor: "#AAFF00",
                borderColor: "#AAFF00",
              },
            ],
          }}

          options={{
            responsive: true,
            plugins: {
            legend: { position: "top" },
            },
            scales: {
            y: {
                reverse: true,
                title: { display: true, text: "Gini Coeffient" },
            },
            },
        }}
          />
      </div>;
    };

    return (
      <>
        {loading ? (
          <div>Loading...</div> // show this while fetch is in progress
        ) : (
          handleData() // otherwise, show data or empty message
        )}
      </>
    );
  };

export default GiniCoeffientChart;