import React, {useRef, useState} from 'react'
import MyButton from 'components/Buttons/MyButton'
import { hear, say } from 'objects/actions.assistant'
import NarrowSpan from 'components/Span/NarrowSpan'

export default function Demo_Learn() {
  const text = useRef(0)
  const [history, setHistory] = useState([])
  const [hearing, setHearing] = useState(false)

  function speak(){
    const message = text.current.value 
    say(message)
    setHistory([...history, {info:message}])
  }

  function recognize(){
    
    setHearing(!hearing)
    let val = hear()

    if(val){
      text.current.value = val
      speak()
    }

    console.log(hear)
  }

  return (
    <div className="w-full bg-slate-500">
      <div className="p-2">
        {history.map((e, i) => 
          <NarrowSpan key={i} data={e} />
        )}
      </div>
      <form action="" className="grid grid-cols-5 w-4/5 p-4 m-auto gap-4">
        <input ref={text} type="text" className="text-black px-2 dark:text-white col-span-3 rounded-md" />
        <MyButton label={"hablar"} className="rounded-md bg-gray-700 p-2" action={speak}/>
        <MyButton label={hearing ? "enviar": "escuchar"} className="rounded-md bg-gray-700 p-2" action={recognize}/>
      </form>
    </div>
  )
}
