import { useState } from 'react';
import MedianIncomeChart from './MedianIncomeChart';
import HealthRankChart from './HealthRankChart';
import GiniCoeffientChart from './GiniCoeffientChart';
import DeathBirthChart from './DeathBirthChart';

const chartComponents = {
  medianIncome: MedianIncomeChart,
  healthRank: HealthRankChart,
  giniCoefficient: GiniCoeffientChart,
  deathBirth: DeathBirthChart,
};

const Charts = ({ selectedRegion }) => {
  const countyLabel = selectedRegion
    ? `Results For ${selectedRegion} County`
    : "Select a county to see its data";

  // Track selected charts in order
  const [selectedCharts, setSelectedCharts] = useState([]);
  const [infoPopup, setInfoPopup] = useState(null);
  const [isInfoPopupOpen, setIsInfoPopupOpen] = useState(false);

  // Toggle chart selection
  const toggleChart = (chart) => {
    setSelectedCharts((prev) => {
      if (prev.includes(chart)) {
        // Remove it
        return prev.filter((c) => c !== chart);
      } else {
        // Add to end
        return [...prev, chart];
      }
    });
  };

  function retrieveInfo(value) {
    const BACKEND_URL =
      process.env.NODE_ENV === "development"
        ? "http://localhost:5050"
        : "/health_analytics_backend";

    fetch(`${BACKEND_URL}/get-info`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        calculationType: value,
      }),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Request failed");
        return res.json();
      })
      .then((data) => {
        setInfoPopup({ value, data });
        setIsInfoPopupOpen(true);
      })
      .catch((err) => console.error(err));
  }

  return (
    <>
      <div className="label">{countyLabel}</div>

      {/* Checkboxes */}
      <div style={{ marginBottom: '10px' }}>
        {/* Check All */}
      <label>
        <input
          type="checkbox"
          // Checked if all charts are selected
          checked={
            selectedCharts.length === Object.keys(chartComponents).length
          }
          onChange={() => {
            if (selectedCharts.length === Object.keys(chartComponents).length) {
              // If all are selected, uncheck all
              setSelectedCharts([]);
            } else {
              // Otherwise, check all
              setSelectedCharts(Object.keys(chartComponents));
            }
          }}
        />
        Check All
      </label>
        <label>
          <input
            type="checkbox"
            checked={selectedCharts.includes('medianIncome')}
            onChange={() => toggleChart('medianIncome')}
          />
          Median Income
          <button type="button" onClick={() => retrieveInfo('medianIncome')}>
            ?
          </button>
        </label>{' '}
        <label>
          <input
            type="checkbox"
            checked={selectedCharts.includes('healthRank')}
            onChange={() => toggleChart('healthRank')}
          />
          Health Rank
          <button type="button" onClick={() => retrieveInfo('healthRank')}>
            ?
          </button>
        </label>{' '}
        <label>
          <input
            type="checkbox"
            checked={selectedCharts.includes('giniCoefficient')}
            onChange={() => toggleChart('giniCoefficient')}
          />
          Gini Coefficient
          <button type="button" onClick={() => retrieveInfo('giniCoefficient')}>
            ?
          </button>
        </label>
        <label>
          <input
            type="checkbox"
            checked={selectedCharts.includes('deathBirth')}
            onChange={() => toggleChart('deathBirth')}
          />
          Deaths & Births
          <button type="button" onClick={() => retrieveInfo('deathBirth')}>
            ?
          </button>
        </label>{' '}
      </div>

      {/* Render charts in the order they were selected */}
      {selectedCharts.map((chartKey) => {
        const ChartComponent = chartComponents[chartKey];
        return (
          <div key={chartKey} className="chart">
            <ChartComponent selectedRegion={selectedRegion} />
          </div>
        );
      })}

      {isInfoPopupOpen && infoPopup && (
        <div
          style={{
            position: 'fixed',
            inset: 0,
            background: 'rgba(0, 0, 0, 0.45)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 1000,
          }}
          onClick={() => setIsInfoPopupOpen(false)}
        >
          <div
            style={{
              background: '#fff',
              borderRadius: '12px',
              padding: '16px',
              width: 'min(640px, 90vw)',
              maxHeight: '80vh',
              overflow: 'auto',
              boxShadow: '0 20px 60px rgba(0, 0, 0, 0.3)',
            }}
            onClick={(event) => event.stopPropagation()}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', gap: '12px' }}>
              <h3 style={{ margin: 0 }}>{infoPopup.value} data</h3>
              <button type="button" onClick={() => setIsInfoPopupOpen(false)}>
                Close
              </button>
            </div>
            <pre style={{ marginTop: '12px', whiteSpace: 'pre-wrap' }}>
{JSON.stringify(infoPopup.data, null, 2)}
            </pre>
          </div>
        </div>
      )}
    </>
  );
};

export default Charts;
