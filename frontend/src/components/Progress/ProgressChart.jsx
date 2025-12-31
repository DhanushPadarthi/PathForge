import { PieChart, Pie, Cell, Tooltip } from "recharts"

export default function ProgressChart({ completed, remaining }) {
  const data = [
    { name: "Completed", value: completed },
    { name: "Remaining", value: remaining }
  ]

  return (
    <PieChart width={250} height={250}>
      <Pie data={data} dataKey="value" outerRadius={80}>
        <Cell fill="#4caf50" />
        <Cell fill="#ccc" />
      </Pie>
      <Tooltip />
    </PieChart>
  )
}
