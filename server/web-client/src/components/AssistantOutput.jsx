import React from 'react'
export default function AssistantOutput({dialogue}) {
  return (
    <div>
      {dialogue.map((set, index) => { 
        return (
          <div key={index} 
            className={"px-3 text-white " + ((index % 2 == 0) ? "bg-dark" : "bg-secondary")}>
            {(index % 2 == 1)? 
              <i className="bi bi-person-circle"> </i> : 
              <i className="bi bi-cpu"> </i>}
            {set}
          </div> 
        )
      })}
    </div>
  )
}
