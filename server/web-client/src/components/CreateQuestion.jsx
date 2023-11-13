import React, {useState, useRef, Fragment} from 'react'

export default function CreateQuestion({newQuestion}) {
  
    const [formMode, setFormMode] = useState(true)
    const [question, setQuestion] = useState({
        question: "¿Pregunta?",
        question_ans: "Respuesta Correcta",
        question_err: "Respuesta Errada",
        question_exp: "Explicacion",
        question_type: 0,
        question_subs: 1
    })

    const [quest, answer, wrong, explanation, type, subject, parser] = 
        [useRef(), useRef(), useRef(), useRef(), useRef(), useRef(), useRef()]
    
    function ChangeMode(){
        setFormMode(!formMode)
    }

    function ParseData(){
        
    }

    function Display(){
        prompt("XD")
    }

    function SubmitQuestion(){
        let requestData
        if(formMode){
            requestData = {
                "question" : quest.current.value,
                "question_ans" : answer.current.value,
                "question_err" : wrong.current.value,
                "question_exp" : explanation.current.value,
                "question_type" : type.current.value,
                "question_subs" : subject.current.value
            }
        } else {
            requestData = ParseData(parser.current.value)
        }
        alert(requestData.question)

        let r = fetch('http://localhost:8000/api/question/',
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(requestData)
            }
        )

        r.then((response) => response.json()).then((data) => {
            if(data.status == 500){
                for(let e in data.errors)
                alert(`${e} : ${data.errors[e]}`)
            } else if (data.status == 302){
                alert("Pregunta Almacenada correctamente")
                setFormMode(formMode)
            }
        })
    }
  
  return (
    <form>
        <div className="container form-group bg-light">
            { (formMode) ?
                <div className="row">
                    <div className="container col-md-6 form-group">
                        <label htmlFor="quest">Pregunta :</label>
                        <input ref={quest} type="text" id="quest" placeholder="Pregunta"
                            className="form-control" required/>
                        
                        <label htmlFor="answer">Respuesta :</label>
                        <input ref={answer} type="text" id="answer" placeholder="Respuesta"
                            className="form-control" required/>
                        
                        <label htmlFor="wrong">Alternativas :</label>
                        <input ref={wrong} type="text" id="wrong" placeholder="Erroneas"
                            className="form-control" required/>


                        <div className="row">
                            <div className="container col-md-6">
                                <label htmlFor="type">Tipo de Pregunta :</label>
                                <select ref={type} id="type"
                                    className="form-control" required>
                                    <option value="0">Alternativas</option>
                                    <option value="1">Verdadero / Falso</option>
                                    <option value="2">Completar</option>
                                </select>
                            </div>
                            
                            <div className="container col-md-6">
                                <label htmlFor="subject">Tema :</label>
                                <select ref={subject} name="" id=""
                                    className="form-control" required>
                                    <option value="1">2.1</option>
                                    <option value="2">2.2</option>
                                    <option value="3">2.3</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    
                    <div className="container col-md-6 form-group">
                        <label htmlFor="explanation">Explicacion :</label>
                        <textarea ref={explanation} id="explanation" cols="30" rows="10"
                            className="form-control"></textarea>
                    </div>
                </div>
            :
                <div className="row">
                    <div className="container col form-group">
                        <label htmlFor="parser">Texto</label>
                        <textarea ref={parser} name="" id="parser" cols="30" rows="10"
                            className="form-control"></textarea>
                    </div>
                </div>
            }
        </div>
        <div className="container px-3">
            <div className="row gx-3 form-group">
                <div className="col">
                    <button type="button" onClick={ChangeMode} className="btn btn-secondary form-control"> Cambiar a Modo {(formMode)? "Texto" : "Formulario"} </button>
                </div>
                <div className='col'>
                    <button type="button" onClick={SubmitQuestion} className="btn btn-primary form-control"> Nueva Pregunta </button>
                </div>
                <div className='col'>
                    <button type="button" onClick={Display} className="btn btn-warning form-control"> Message </button>
                </div>
            </div>
        </div>
    </form>
  )
}
