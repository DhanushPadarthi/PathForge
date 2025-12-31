import { useProgress } from "../hooks/useProgress"
import ProgressDashboard from "../components/Progress/ProgressDashboard"
import ResourceCard from "../components/ResourceCard"
import { completeResource, skipResource } from "../services/progressService"

export default function DashboardPage() {
  const progress = useProgress()

  if (!progress) return <p>Loading...</p>

  return (
    <div>
      <h1>User Dashboard</h1>
      <ProgressDashboard progress={progress} />

      <h3>Learning Resources</h3>
      {progress.resources.map((r) => (
        <ResourceCard
          key={r.id}
          resource={r}
          onComplete={completeResource}
          onSkip={skipResource}
        />
      ))}
    </div>
  )
}
