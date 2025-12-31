export default function ResourceCard({ resource, onComplete, onSkip }) {
  return (
    <div className="card">
      <h4>{resource.title}</h4>
      <p>Skill: {resource.skill}</p>
      <p>Time: {resource.estimated_time_minutes} min</p>
      <button onClick={() => onComplete(resource.id)}>Complete</button>
      <button onClick={() => onSkip(resource.id)}>Skip</button>
    </div>
  )
}
