import React from 'react'
import MedianIncomeChart from './MedianIncomeChart';



//  need to have a way for users to select what charts are shown

const Charts = ({ selectedRegion  }) => {
    const countyLabel = selectedRegion
    ? `Results For ${selectedRegion} County`
    : "Select a county to see its data";

  return (
    <>
      <div className='label'>{countyLabel}</div>
      <div className='chart'><MedianIncomeChart selectedRegion={selectedRegion} /></div>
      <div className='chart'>chart 2</div>
      <div className='chart'>chart 3</div>
      <div className='chart'>chart 4</div>
    </>
  );
}

export default Charts