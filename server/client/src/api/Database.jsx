import React, { Component } from 'react'

import axios from 'axios'
import { generateSubsTree, getAllSubs } from './subs.api'

export const apiRoutes = {
  learn: "http://localhost:8000/dev/learn/",
  quiz: "http://localhost:8000/dev/quiz/",
  game: "http://localhost:8000/dev/game/",
  subs: "http://localhost:8000/dev/subs/",
}

class Database{

  state = {
    subsData : {},
    infoData : {},
    quizData : {},
    gameData : {},
    dataTree : [],
  }

  getInfo(){
    axios.get(apiRoutes.learn).then(res => {
      this.state.infoData = res.data
      console.log(this.state.infoData)

    })
  }

  getSubs(){
    axios.get(apiRoutes.subs).then(res => {
      this.state.subsData = res.data
      console.log(this.state.subsData)

    })
  }

  getSubsTree(){
    return generateSubsTree().then((res) => {
      this.state.dataTree = res
      return res
    })
  }

  getQuiz(){
    axios.get(apiRoutes.quiz).then(res => {
      this.state.quizData = res.data
      console.log(this.state.quizData)
    })
  }

  

  ariseQuizData(){
    axios.get('localhost:8000/dev/learn')
  }


  render() {
    return (
      <div>
        
      </div>
    )
  }
}

export default new Database()