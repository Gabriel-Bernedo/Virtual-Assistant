import React, {Fragment, useState} from 'react'

import AssistantInput from '../components/AssistantInput'
import AssistantOutput from '../components/AssistantOutput'
import axios from "axios"

export default class Assistant extends React.Component {

  

  constructor(props){
    super(props)

    this.actions = ["welcome", "learning", "tests", "games"]
    this.greetings = ["HOLA, COMO ESTAS ?", "SCISYNC LE DA LA BIENVENIDA", "BIENVENIDO A UNA NUEVA EXPERIENCIA"]

    this.state = {
      dialogue : [this.greet()],
      action : this.actions[0]
    }
  }
  
  greet = () => {
    return (
      <span>
        {this.greetings[Math.floor(Math.random() * this.greetings.length)]}
      </span>
    )
  }

  response = (input) => {
    this.setState({dialogue: [...this.state.dialogue, input]})
    switch(this.state.action){
      case "welcome":
        this.selectMode(input)
        break;
      case "learning":
        break;
      case "tests":
        break;
      case "games":
        break;
      default:
    }
  }

  selectMode = (input) => {

  }

  render() {
    return (
      <div className="container-fluid">
        <AssistantOutput dialogue={this.state.dialogue}></AssistantOutput>
        <AssistantInput interact={this.response}></AssistantInput>
      </div>
    )
  }
}
