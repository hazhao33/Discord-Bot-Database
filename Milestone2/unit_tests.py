# This file will be used to create your unit tests to test your database models.
from models import *
#1
# students = ClassEnrollment.getFall2023()
# print(students)

# #2
# majors = MajorAveGPA.getAll()
# print(majors)

# #3
# students = HighGPA.getHigherGpa(3)
# print(students)

# #4
# students = ClassEnrollment.getDatabaseClassEnrollment("Database Intro")
# print(students)

#5
# staff = StaffAndDepartment.addStaffAndToDepartment('Gnar', '2000-01-01', 1)
# print(staff)
#6
# student = ClassEnrollment.enrollToClassAndSemester(1, 1)
# print(student)
#7

#8
# account = UpdateAccount.updateStudentInfo(1, "null@mail.com", "111-111-1111")
# print(account)
#9
# student = RemoveStudent.removeFailStudent()
# print(student)
#10
# staff = RemoveStaff.remove(1)
# print(staff)

#15
major = MajorAveGPA.aMajorGpa('Computer Science')
print(major)