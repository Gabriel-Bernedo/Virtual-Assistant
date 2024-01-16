import axios from "axios"
import { apiRoutes } from "./Database"

const url = apiRoutes.info

export const getAllInfo = () => axios.get(url)
export const createInfo = (el) => axios.post(url, sub)
export const deleteInfo = (el) => axios.delete(url, sub)
export const updateInfo = (id, el) => axios.post(`${url}${id}/`, el)

export const addInfoT