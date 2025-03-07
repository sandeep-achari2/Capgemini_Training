# class StuTable:
#     def __init__(self, id, name, standard):
#         self.id = id
#         self.name = name
#         self.standard = standard

# class MarkTable:
#     def __init__(self, id, mark):
#         self.id = id
#         self.mark = mark

# class SqlOperation:
#     def __init__(self, students, marks):
#         self.students = students
#         self.marks = marks

#     def joinTable(self):
#         student_ids_with_marks = {mark.id for mark in self.marks}
#         return [student for student in self.students if student.id in student_ids_with_marks]

#     def selectByStandard(self, standard):
#         return [student.name for student in self.students if student.standard == standard]


# # Sample Input
# s1 = StuTable(1, "John", 3)
# s2 = StuTable(2, "Jack", 3)
# s3 = StuTable(3, "Jerry", 4)
# s4 = StuTable(4, "Tin", 5)

# m1 = MarkTable(1, 99)
# m2 = MarkTable(2, 99)
# m3 = MarkTable(2, 88)

# sql = SqlOperation([s1, s2, s3, s4], [m1, m2, m3])

# # Sample Output
# result = sql.joinTable()


print("He;lo=")