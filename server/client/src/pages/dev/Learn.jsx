import React, {useState, useEffect} from 'react'

import SideBar from 'components/SideBars/SideBar'
import LearnEditor from 'components/Frames/LearnEditor'
import Database from 'api/Database'
import { SubEncoder } from 'api/subs.api'

export default function Dev_Learn() {
  const [data, setData] = useState([])
  useEffect(() => {
    Database.getSubsTree().then(res => {
      setData(res)
    })
  },[])

  const [subject, setSubject] = useState({})

  return (
    <div className="w-full h-full bg-slate-500 ">
      <LearnEditor data={subject}></LearnEditor>      
      <SideBar items={data} encoder={SubEncoder} select={setSubject} />
    </div>
  )
}
