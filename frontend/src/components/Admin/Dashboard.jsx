import { useEffect, useState } from "react"
import { getStats } from "../../services/adminService"

export default function AdminDashboard() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    getStats().then(setStats)
  }, [])

  if (!stats) return <p>Loading...</p>

  return (
    <>
      <h2>Admin Metrics</h2>
      <p>Users: {stats.users}</p>
      <p>Resources: {stats.resources}</p>
      <p>Active Users: {stats.activeUsers}</p>
    </>
  )
}
