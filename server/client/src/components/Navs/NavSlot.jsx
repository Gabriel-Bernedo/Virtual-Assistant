import React from 'react'
import { Link } from 'react-router-dom'

export default function NavSlot({slot}) {
  return (
    <Link to={slot.href} className="text-sm font-semibold leading-6 text-gray-900">
      {slot.name}
    </Link>
  )
}
