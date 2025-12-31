import { useEffect, useState } from "react"
import { getUserProgress } from "../services/progressService"

export const useProgress = () => {
  const [progress, setProgress] = useState(null)

  useEffect(() => {
    getUserProgress().then(setProgress)
  }, [])

  return progress
}
