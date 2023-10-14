import React, {Fragment, useState} from 'react'
import {Routes, Route, BrowserRouter, Navigate} from 'react-router-dom'

import Navigation from './components/Navigation'
import Index from './pages/Index'
import Assistant from './pages/Assistant'

export default function App() {
  const [count, setCount] = useState(0)

  return (
    <Fragment>
      <BrowserRouter>
        <Navigation />
        <Routes>

          <Route path="/home/" element={
            <Index />
          } />

          <Route path="/demo/" element={
            <Assistant />
          } />

          <Route path="/" element={
            <Navigate to="/home/"></Navigate>
          } />
          
        </Routes>
      </BrowserRouter>
    </Fragment>
  )
}
