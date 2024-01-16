import React from 'react'

export default function Editor({children, className}) {
  return (
    <div className={"m-[10px] border border-white " + className}>
      {children}
    </div>
  )
}
