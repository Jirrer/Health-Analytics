import React, { useState } from 'react';
import MedianIncomeChart from './MedianIncomeChart';
import HealthRankChart from './HealthRankChart';
import GiniCoeffientChart from './GiniCoeffientChart';

const chartComponents = {
  medianIncome: MedianIncomeChart,
  healthRank: HealthRankChart,
  giniCoefficient: GiniCoeffientChart,
};

const Charts = ({ selectedRegion }) => {
  const countyLabel = selectedRegion
    ? `Results For ${selectedRegion} County`
    : "Select a county to see its data";

  // Track selected charts in order
  const [selectedCharts, setSelectedCharts] = useState([
    'medianIncome',
    'healthRank',
    'giniCoefficient',
  ]);

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
