import React, {useRef} from 'react'
import Editor from './Editor'
import ContextSideBar from 'components/SideBars/ContextSideBar'
import MyButton from 'components/Buttons/MyButton'

const itemStyle = "m-3 flex space-x-4 "

export default function LearnEditor() {
  return (
    <div className="ml-[256px] h-full">
      <h1 className="flex text-5xl justify-center margin-4px"> Learn </h1>
      <hr />
      <Editor className="grid grid-cols-7 font-medium gap-1 ">
        <ContextSideBar title="Contenidos" className="col-span-2"/>
        <div className=" h-full text-gray-900 dark:text-white col-span-5 text-l grid grid-cols-subgrid gap-4">
          <div className={itemStyle + "col-span-1"}>
            <MyButton 
              icon={{
                type:"options", value:"Save"
              }}/>
            <MyButton 
              icon={{
                type:"options", value:"Delete"
              }}/>
            <MyButton 
              icon={{
                type:"options", value:"Add"
              }}/>
          </div>
          <div className="col-span-4"></div>          
          
          <label htmlFor="">Tema :</label>
          <input type="text" required className="col-span-4"/>
         
          <label htmlFor="">Introduccion :</label>
          <input type="text" className="col-span-4" />

          <label htmlFor="">Informacion :</label>
          <textarea required className="h-[10rem] resize-none col-span-4"/>

          <label htmlFor="">Orden de Prioridad :</label>
          <input type="text" pattern="[0-9]*" className='col-span-4'/>
          
        </div>
        
      </Editor>
    </div>
  )
}
