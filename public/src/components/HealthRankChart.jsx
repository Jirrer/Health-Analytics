import { useEffect, useState } from "react";
import {Chart as ChartJS } from "chart.js/auto";
import { Bar, Doughnut, Line } from "react-chartjs-2";

const HealthRankChart = ({ selectedRegion }) => { // AI slop
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    if (!selectedRegion) return; 

    setLoading(true);

    setData(null);

    fetch(`${BACKEND_URL}/get-health-rank`, {
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
      
      console.log(data)
      
      return<div className="LineChart">
        <Line
        data={{
            labels: countyData.map(item => item[0]),
            datasets: [
            {
                label: "Health Rank",
                data: countyData.map(item => item[1]),
                backgroundColor: "#FF3030",
                borderColor: "#FF3030",
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
                reverse: true, // <-- this flips the Y-axis
                title: { display: true, text: "Health Rank" },
            },
            },
        }}
        />
    </div>
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

export default HealthRankChart;