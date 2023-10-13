import React, {Fragment} from 'react'
import Navigation from '../components/Navigation'
import Banner from '../components/Banner'
import {Routes, Route, BrowserRouter, Navigate} from 'react-router-dom'
export default function Index() {
  return (
    <Fragment>
      <BrowserRouter>
        <Navigation />
        <Routes>
          <Route path="/home/" element={
            <Banner></Banner>
          } />
          <Route path="/" element={
            <Navigate to="/home/"></Navigate>
          } />
          
        </Routes>
      </BrowserRouter>
      
    </Fragment>
  )
}
