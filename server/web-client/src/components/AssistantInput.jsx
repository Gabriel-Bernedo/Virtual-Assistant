import React, {useRef} from 'react'

export default function AssistantInput({interact}) {

  const input = useRef("")

  function send(){
    interact((
      <span>
        {input.current.value}
      </span>
    ))
    input.current.value = ""
  }

  return (
    <div>
      <input ref={input} type="text" name="" id="" placeholder="Responda con la verdad XD" required
        className="form-control"/>
      <button type="button"
        className="btn" onClick={send}>
        <i className="bi bi-send"></i> Enviar Consulta
      </button>
      <button 
        className="btn">
        <i className="bi bi-mic"></i> Grabar Audio
      </button>
    </div>
  )
}
