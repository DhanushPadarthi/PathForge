import { adminStats, users } from "../mock/mockData"

export const getStats = async () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(adminStats), 500)
  })
}

export const getUsers = async () => {
  return users
}

export const deleteUser = async (id) => {
  console.log("Deleted user:", id)
}
