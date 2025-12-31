export const progressData = {
  total: 10,
  completed: 6,
  skipped: 1,
  percentage: 70,
  streak: 5,
  timeSpent: 320,
  modules: [
    { name: "Python Basics", progress: 80 },
    { name: "ML Foundations", progress: 60 }
  ],
  resources: [
    {
      id: 1,
      skill: "Python",
      title: "Python Official Docs",
      estimated_time_minutes: 45,
      status: "pending"
    },
    {
      id: 2,
      skill: "ML",
      title: "Intro to ML",
      estimated_time_minutes: 60,
      status: "completed"
    }
  ]
}

export const adminStats = {
  users: 120,
  resources: 340,
  roles: 8,
  activeUsers: 78
}

export const users = [
  { id: 1, name: "Alice", role: "Student" },
  { id: 2, name: "Bob", role: "Admin" }
]
