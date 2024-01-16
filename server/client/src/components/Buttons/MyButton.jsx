import React from 'react'
import MyIcon from 'components/Icons/MyIcon'

export default function MyButton({className, icon, label, action}) {
  return (
    <button type="button" className={className} onClick={action}>
      {(icon) ? 
        <MyIcon icon={icon} /> 
        : ""
      }
      {(label) ? 
        <span> {label} </span> 
      : ""
      }
    </button>
  )
}
