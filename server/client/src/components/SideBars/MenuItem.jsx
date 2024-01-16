import React from 'react'
import MyIcon from 'components/Icons/MyIcon'
import { renderItem } from './ContextSideBar'
import { Disclosure } from '@headlessui/react'

export default function MenuItem({item, encoder, select}) {
   return (
      <li>
         {/*
         <button type="button" className="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700" aria-controls="dropdown-example" data-collapse-toggle="dropdown-example">
            {(item.icon) ? <MyIcon icon={item.icon}/> : ""}
                  
               <span className=" ms-3 text-left rtl:text-right">{item.name}</span>
               <MyIcon icon={{type:"original", value: "DownArrow"}} />
            
         </button>
   */}
         <Disclosure as="div" className="mx-1">
            {({ open }) => (
               <>
                  <Disclosure.Button 
                     className="flex w-full items-center justify-between rounded-lg py-2 pl-3 pr-3.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                     
                     >
                  {item.name}
                  <MyIcon icon={{type:"original", value: "DownArrow"}} 
                     className={`h-5 w-3 flex-none ${open ? 'rotate-180':''}`}
                     aria-hidden="true"
                  />
               
                  </Disclosure.Button>
                  <Disclosure.Panel className="mt-2 space-y-2">
                     <ul>

                  {item.childs.map((item) => {
                     return renderItem(item, encoder, select)
                     /*<button
                     key={item.name}
                     className="block rounded-lg py-2 pl-6 pr-3 text-sm font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                     >
                     {item.name}
                     </button>*/
                  })}
                  </ul>
                  </Disclosure.Panel>
               </>
            )}
            </Disclosure>
      </li>
  )
}
