import ProgressBar from "../ProgressBar"
import ProgressChart from "./ProgressChart"

export default function ProgressDashboard({ progress }) {
  return (
    <>
      <h2>Progress Overview</h2>
      <ProgressBar value={progress.percentage} />
      <p>🔥 Streak: {progress.streak} days</p>
      <p>⏱ Time Spent: {progress.timeSpent} mins</p>

      <ProgressChart
        completed={progress.completed}
        remaining={progress.total - progress.completed}
      />
    </>
  )
}
