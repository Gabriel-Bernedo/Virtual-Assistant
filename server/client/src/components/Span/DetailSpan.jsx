import React from 'react'
import { Link } from 'react-router-dom'

export default function DetailSpan({data}) {
  return (
    <section className="w-4/5 bg-gray-700 my-2 p-3 rounded-md">
      {(data.icon && data.side == "left") ? "":""}
      <div className={`text-${data.side}`} >
        <Link to={data.href} className="text-3xl">{data.title}</Link>
        <p className="whitespace pre-line">
          {data.content}
        </p>
      </div>
      {(data.icon && data.side == "right") ? "":""}
    </section>
  )
}
