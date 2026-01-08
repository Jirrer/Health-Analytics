import React, { useState } from 'react';
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
        </label>{' '}
        <label>
          <input
            type="checkbox"
            checked={selectedCharts.includes('healthRank')}
            onChange={() => toggleChart('healthRank')}
          />
          Health Rank
        </label>{' '}
        <label>
          <input
            type="checkbox"
            checked={selectedCharts.includes('giniCoefficient')}
            onChange={() => toggleChart('giniCoefficient')}
          />
          Gini Coefficient
        </label>
        <label>
          <input
            type="checkbox"
            checked={selectedCharts.includes('deathBirth')}
            onChange={() => toggleChart('deathBirth')}
          />
          Deaths & Births
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
    </>
  );
};

export default Charts;
