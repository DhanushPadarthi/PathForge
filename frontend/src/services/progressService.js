import { progressData } from "../mock/mockData"

export const getUserProgress = async () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(progressData), 500)
  })
}

export const completeResource = async (id) => {
  console.log("Completed resource:", id)
}

export const skipResource = async (id) => {
  console.log("Skipped resource:", id)
}
