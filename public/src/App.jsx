import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import TopBar from './components/TopBar'
import Map from './components/Map'
import Charts from './components/Charts'

function App() {
  const [selectedRegion, setSelectedRegion] = useState(null);

  return (
    <>
    <div className="AppGrid">
      <div className="TopBar"><TopBar /></div>
      <div className="LeftSide">
        <Map setSelectedRegion={setSelectedRegion} />
      </div>
      <div className="RightSide">
        <Charts selectedRegion={selectedRegion} />
      </div>
    </div>
    
   
    </>
  )
}

export default App
