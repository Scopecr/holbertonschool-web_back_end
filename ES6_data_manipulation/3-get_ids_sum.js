//Function that returns the students reduced IDs

export default function getStudentIdsSum(students) {
  return students.reduce((sum, student) => sum + student.id, 0);
}