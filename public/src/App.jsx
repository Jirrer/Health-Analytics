import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import TopBar from './components/TopBar'
import Map from './components/Map'
import Charts from './components/Charts'

function App() {

  return (
    <>
    <div className="AppGrid">
      <div className='TopBar'><TopBar /></div>
      <div className='LeftSide'><Map /></div>
      <div className='RightSide'><Charts /></div>
    </div>
    
   
    </>
  )
}

export default App
