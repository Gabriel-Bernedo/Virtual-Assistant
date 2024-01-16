import axios from "axios"
import { apiRoutes } from "./Database"

const url = apiRoutes.subs

export const getAllSubs = () => axios.get(url)
export const createSub = (el) => axios.post(url, sub)
export const deleteSub = (el) => axios.delete(url, sub)
export const updateSub = (id, el) => axios.post(`${url}${id}/`, el)

export const generateSubsTree = () => {
  return getAllSubs().then( res => res.data).then(data => {
    return SetChilds(data, null)
  })
}



function makeTree(data, node){
  const childs = SetChilds(data,node)
  node.childs = node
}

function SetChilds (data, parent) {
  const childs = data.filter((sub) => sub.subject_parent == parent)
  for(let e of childs){
    e.childs = SetChilds(data, e.id)
  }
  return childs
}

export function SubEncoder(sub){
  const res = {}
  res.name = sub.subject_name
  res.childs = sub.childs
  res.type = sub.childs.length > 0 ? "menu": "single"
  return res  
}