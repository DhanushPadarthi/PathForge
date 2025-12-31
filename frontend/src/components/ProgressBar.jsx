export default function ProgressBar({ value }) {
  return (
    <div style={{ background: "#ddd", borderRadius: 10 }}>
      <div
        style={{
          width: `${value}%`,
          background: "#4caf50",
          padding: 8,
          borderRadius: 10,
          color: "#fff"
        }}
      >
        {value}%
      </div>
    </div>
  )
}
