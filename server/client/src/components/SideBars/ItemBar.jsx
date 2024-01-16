import React from 'react'
import MyIcon from 'components/Icons/MyIcon'
export default function ItemBar({item, select}) {
  return (
    <li>
      <button type="button"
        className="flex items-center w-full p-2 text-gray-900 rounded-lg dark:text-white hover:bg-indigo-200 dark:hover:bg-gray-700 group"
        onClick={() => {select(item)}}  
      >
          {(item.icon) ? <MyIcon icon={item.icon}/> : ""}
          <span className="ms-3">{item.name}</span>
          {/*(item.addon) ? 
          <span className={`inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-${item.addon.color}-800 bg-${item.addon.color}-100 rounded-full dark:bg-${item.addon.color}-900 dark:text-${item.addon.color}-300`}>
            {item.addon.value}
          </span>:
          ""*/}
      </button>
    </li>
  )
}
