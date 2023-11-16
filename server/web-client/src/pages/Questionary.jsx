import React, { Fragment, useState, useRef, useEffect} from 'react'
import CreateQuestion from '../components/CreateQuestion'
import ListQuestions from '../components/ListQuestions'
export default function Questionary() {

  const [questions, setQuestions] = useState([])

  function HandleNewQuestion(){
    alert('nueva pregunta')
  }





  return (
    <Fragment>
      <CreateQuestion newQuestion={HandleNewQuestion}></CreateQuestion>
      <ListQuestions></ListQuestions>
    </Fragment>
  )
}
