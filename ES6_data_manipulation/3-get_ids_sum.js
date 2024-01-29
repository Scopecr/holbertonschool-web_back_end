export default function getStudentIdsSum() {
  return students.reduce((sum, student) => sum = student.id, 0);
}