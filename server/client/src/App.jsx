import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Navigation from './components/Navs/Navigation'
import Index from './pages/Index'
import OhWeHaveAProblem from './pages/OhWeHaveAProblem'
export default function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="" element={Index()}/>
        <Route path="/*" element={OhWeHaveAProblem()}/>

      </Routes>
    </BrowserRouter>
  )
}
