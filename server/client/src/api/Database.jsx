import React, { Component } from 'react'

import axios from 'axios'
import { generateSubsTree, getAllSubs } from './subs.api'
import { addInfoToSubjects } from './info.api'
import { addQuizToSubjects } from './quiz.api,'

export const apiRoutes = {
  learn: "http://localhost:8000/dev/learn/",
  quiz: "http://localhost:8000/dev/quiz/",
  game: "http://localhost:8000/dev/game/",
  subs: "http://localhost:8000/dev/subs/",
}

class Database{

  state = {
    subsData : [],
    infoData : [],
    quizData : [],
    gameData : [],
    dataTree : [],
  }

  getInfo(){
    axios.get(apiRoutes.learn).then(res => {
      this.state.infoData = res.data
      console.log(this.state.infoData)

    })
  }

  getSubs(){
    return getAllSubs().then(res => res.data).then((data) => {
      this.state.subsData = data
      return data
    })
  }

  getSubsTree(){
    return generateSubsTree().then((res) => {
      this.state.dataTree = res
      return res
    })
  }

  getDataTree(){
    return this.getSubsTree().then((res) => 
      addInfoToSubjects().then(addQuizToSubjects) && res
    )
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