import React, {Fragment} from 'react'
import ContextSideBar from './ContextSideBar'
export default function Sidebar({items, encoder, select}) {
  return (
   <Fragment>
   <aside id="default-sidebar" className="mt-[96px] fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
      <ContextSideBar items={items} encoder={encoder} select={select}></ContextSideBar>
   </aside>
    </Fragment>
  )
}
