import axios from "axios"
import Database, { apiRoutes } from "./Database"
import { getAllSubs } from "./subs.api"

const url = "http://localhost:8000/dev/learn/"

export const getAllInfo = () => axios.get(url)
export const createInfo = (el) => axios.post(url, sub)
export const deleteInfo = (el) => axios.delete(url, sub)
export const updateInfo = (id, el) => axios.post(`${url}${id}/`, el)

export const addInfoToSubjects = () => {
  return getAllInfo().then((res) => res.data).then((data) => {
    const indexes = [...new Set(data.map((e)=> e.info_subject))]
    for(let e of indexes){
      Database.state.subsData.find((el) => el.id == e).info = data.filter((el) => el.info_subject == e)
    }
    return Database.state.subsData
  })
}

