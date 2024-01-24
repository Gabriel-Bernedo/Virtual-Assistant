import axios from "axios"
import Database, { apiRoutes } from "./Database"
import { getAllSubs } from "./subs.api"

const url = "http://localhost:8000/dev/quiz/"

export const getAllQuiz = () => axios.get(url)
export const createQuiz = (el) => axios.post(url, sub)
export const deleteQuiz = (el) => axios.delete(url, sub)
export const updateQuiz = (id, el) => axios.post(`${url}${id}/`, el)

export const addQuizToSubjects = () => {
  return getAllQuiz().then((res) => res.data).then((data) => {
    const indexes = [...new Set(data.map((e)=> e.question_subject))]
    for(let e of indexes){
      Database.state.subsData.find((el) => el.id == e).quiz = data.filter((el) => el.question_subject == e)
    }
    return Database.state.subsData
  })
}

