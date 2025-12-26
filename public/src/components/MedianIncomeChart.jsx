import { useEffect, useState } from "react";

const MedianIncomeChart = ({ selectedRegion }) => { // AI slop
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    if (!selectedRegion) return; 

    setLoading(true);

    fetch(`${BACKEND_URL}/get-median-income`, {
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
    if (!data) return;

    console.log(data)
  };

    handleData();

    return (
      <>
        <div>MedianIncomeChart</div>
        {loading && <div>Loading...</div>}
        {!loading && !data && <div>Empty Chart...</div>}
        {!loading && data && <div>found data</div>}
      </>
    );
  };

export default MedianIncomeChart;