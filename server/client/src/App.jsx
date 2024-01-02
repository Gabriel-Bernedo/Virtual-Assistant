import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Navigation from 'components/Navs/Navigation'

import {navigation} from "resources/nav.json"

import Index from 'pages/general/Index'
import OhWeHaveAProblem from 'pages/general/OhWeHaveAProblem'

import Demo_Learn from 'pages/demo/Learn'
import Demo_Quiz from 'pages/demo/Quiz'
import Demo_Games from 'pages/demo/Games'
import Demo_Docs from 'pages/demo/Docs'

import Dev_Docs from 'pages/dev/Docs'
import Dev_Games from 'pages/dev/Games'
import Dev_Learn from 'pages/dev/Learn'
import Dev_Quiz from 'pages/dev/Quiz'

const pages = {
  "Index": Index,
  "OhWeHaveAProblem": OhWeHaveAProblem,
  "Demo_Learn": Demo_Learn,
  "Demo_Quiz": Demo_Quiz,
  "Demo_Games": Demo_Games,
  "Demo_Docs": Demo_Docs,
  "Dev_Learn": Dev_Learn,
  "Dev_Quiz": Dev_Quiz,
  "Dev_Games": Dev_Games,
  "Dev_Docs": Dev_Docs,
}

function renderPage( item ){
  let Page = pages[item.page]
  return <Page {...item.params}/>
}

export default function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        {navigation.map((e) => 
          <Route key={e.page} path={e.href} element={renderPage(e)}/>
        )}
      </Routes>
    </BrowserRouter>
  )
}
