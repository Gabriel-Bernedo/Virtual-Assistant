import React from 'react'

export default function NarrowSpan({data}) {
  return (
    <div className="bg-indigo-700 rounded-md w-5/6 m-auto p-2 mb-2">
      {data.info}
    </div>
  )
}
