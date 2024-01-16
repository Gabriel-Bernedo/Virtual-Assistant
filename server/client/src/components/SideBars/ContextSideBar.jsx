import React, { Fragment } from 'react'
import ItemBar from './ItemBar'
import MenuItem from './MenuItem'

/*
 data: {
  items: [
    {
      "type": "single",
      "name": string,
      "addon": {
        "color": string,
        "value": string,
      },
      "icon": {
        "type": string,
        "value": string,
      },
    }
  ]
 } 
 */

const itemTypes = {
  "single": ItemBar,
  "menu": MenuItem,
}

export function renderItem(element, encoder, select){
  const item = encoder(element)
  let Item = itemTypes[item.type]
  return <Item key={item.name} item={item} select={select} encoder={encoder}/>
}

export default function ContextSideBar({items, title, select, className, encoder}) {
  return (
    <div className={"h-full px-3 py-4 overflow-y-auto bg-indigo-50 dark:bg-gray-800 text-gray-900 dark:text-white " + className}>
      {(title) ? (
        <Fragment>
          <h1 className="text-xl  font-medium">Contenido</h1>
          <hr className="my-2"/>
        </Fragment>
      ): ""}
      { (items) ? 
      <ul className="space-y-2 font-medium">
        {items.map((e) => 
          renderItem(e, encoder, select)
        )}
      </ul> : ""}
      
   </div>
  )
}
