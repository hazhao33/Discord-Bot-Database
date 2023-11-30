"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them
statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""

from database import *


class ClassEnrollment:

  def __init__(self):
    student_id = 0
    name = None
    class_name = None
    year = 0
    sem_type = None

  @staticmethod
  def get(student_id):
    student_data = Database.select(Query.getStudentEnrollment, student_id)[0]
    student = ClassEnrollment()
    student.name = student_data['name']
    student.class_name = student_data['class_name']
    student.year = student_data['year']
    student.sem_type = student_data['type']
    return student

  @staticmethod  #feature 1
  def getFall2023():
    students = []
    student_data = Database.select(Query.getAllStudentEnrollment)
    for s in student_data:
      id = s['student_id']
      student = ClassEnrollment.get(id)
      if 2023 == student.year:
        students.append(student.name)
        students.append(student.class_name)
        students.append(student.year)
    return students

  @staticmethod  #feature 4
  def getDatabaseClassEnrollment(className):
    students = []
    student_data = Database.select(Query.getAllStudentEnrollment)
    for s in student_data:
      id = s['student_id']
      student = ClassEnrollment.get(id)
      if className in student.class_name:  #find student enroll with class name match with input
        students.append(student.name)
        students.append(student.class_name)
    return students

  @staticmethod
  def addToStudentEnrollment(student_id):
    addToSemester = Database.select(Query.studentSemesterEnrollment,
                                    student_id)

  @staticmethod
  def addToClass(class_id, student_id):
    enrollStudent = Database.select(Query.studentCourseEnrollment,
                                    (class_id, student_id))

  @staticmethod  #feature 6
  def enrollToClassAndSemester(student_id, class_id):
    student = []
    addToClass = ClassEnrollment.addToClass(class_id, student_id)
    addToSemester = ClassEnrollment.addToStudentEnrollment(student_id)
    student_info = ClassEnrollment.get(student_id)
    student.append(student_info.name)
    student.append(student_info.class_name)
    student.append(student_info.sem_type)
    student.append(student_info.year)
    return student


class MajorAveGPA:

  def __init__(self):
    major_id = 0
    major_name = None
    average_gpa = 0

  @staticmethod
  def get(major_id):
    major_data = Database.select(Query.getMajorAvgGPA, major_id)[0]
    major = MajorAveGPA()
    major.major_id = major_data['major_id']
    major.major_name = major_data['major_name']
    major.average_gpa = major_data['Average_GPA']
    return major

  @staticmethod  #feature 2
  def getAll():
    majors = []
    major_data = Database.select(Query.getAllMajorAvgGPA)
    for m in major_data:
      id = m['major_id']
      major = MajorAveGPA.get(id)
      majors.append(major.major_name)
      majors.append(major.average_gpa)
    return majors

  @staticmethod  #feature 15
  def aMajorGpa(major_name):
    print("In aMajorGpa:", major_name)
    major_info = Database.select(Query.getAMajorGpa, major_name)
    print(major_info)
    major = []
    for m in major_info:
      major.append(m['major_name'])
      major.append(m['Average_GPA'])
    return major


class HighGPA:

  def __init__(self):
    student_id = 0
    name = None
    gpa = 0

  @staticmethod
  def get(student_id):
    student_data = Database.select(Query.getHighGpaStudent, student_id)[0]
    student = HighGPA()
    student.student_id = student_data['student_id']
    student.name = student_data['name']
    student.gpa = student_data['gpa']
    return student

  @staticmethod  #feature 3
  def getHigherGpa(wantGpa):
    students = []
    student_data = Database.select(Query.getAllHighGpaStudent)
    for s in student_data:
      student_id = s['student_id']
      student = HighGPA.get(student_id)
      if (float(student.gpa)
          > float(wantGpa)):  #find student with gpa higher than wantGpa
        students.append(student.name)
        students.append(student.gpa)
    return students


class StaffAndDepartment:

  def __init__(self):
    staff_id = 0
    name = None
    department_id = 0
    title = None

  @staticmethod
  def getStaff(staff_id):
    staff_data = Database.select(Query.getstaffAndDepartment, staff_id)[0]
    staff = StaffAndDepartment()
    staff.name = staff_data['name']
    staff.title = staff_data['title']
    return staff

  @staticmethod
  def getLastStaff():
    staff_data = Database.select(Query.getLastStaff)[0]
    return staff_data['staff_id']

  @staticmethod
  def addToStaff(staff_name, dob):
    addToStaff = Database.select(Query.addStaff, (staff_name, dob))

  @staticmethod
  def addToDepartment(staff_id, department_id):
    addToDepartment = Database.select(Query.addDepartment,
                                      (staff_id, department_id))

  @staticmethod  #feature 5
  def addStaffAndToDepartment(staff_name, dob, department_id):
    addStaff = StaffAndDepartment.addToStaff(staff_name, dob)
    staff_id = StaffAndDepartment.getLastStaff()
    addToDepartment = StaffAndDepartment.addToDepartment(
      staff_id, department_id)
    staff = []
    staff_info = StaffAndDepartment.getStaff(staff_id)
    staff.append(staff_info.name)
    staff.append(staff_info.title)
    return staff


class UpdateGpa:

  def __init__(self):
    academic_record_id = 0
    student_id = 0
    studen_name = None
    gpa = 0

  @staticmethod
  def getAcademicRecord(student_id):
    student_data = Database.select(Query.getAcademicRecord, student_id)[0]
    student = UpdateGpa()
    student.academic_record_id = student_data['academic_record_id']
    student.student_id = student_data['student_id']
    student.student_name = student_data['name']
    student.gpa = student_data['gpa']
    return student

  @staticmethod  #feature 7
  def updateGpa(student_id, gpa):
    students = []
    updateStudentGpa = Database.select(Query.updateStudentGpa,
                                       (gpa, student_id))
    student = UpdateGpa.getAcademicRecord(student_id)
    students.append(student.student_name)
    students.append(student.gpa)
    return students


class UpdateAccount:

  def __init__(self):
    account_id = 0
    name = None
    email = None
    phone_num = None

  @staticmethod
  def getAcc(account_id):
    account_data = Database.select(Query.getAccount, account_id)[0]
    print("In getAcc--------------------------------")
    print(account_data)
    print("name:", account_data['name'])
    print("email:", account_data['email'])
    print("phone_num:", account_data['phone_num'])
    account = UpdateAccount()
    account.account_id = account_data['account_id']
    account.name = account_data['name']
    account.email = account_data['email']
    account.phone_num = account_data['phone_num']
    return account

  @staticmethod
  def updateAcc(account_id, email, phone_num):
    updateAcc = Database.select(Query.updateAccount,
                                (email, phone_num, account_id))

  @staticmethod  #feature 8
  def updateStudentInfo(account_id, email, phone_num):
    print("In updateStudentInfo------------------------------------")
    print("account_id:", account_id, "email:", email, "phone_num", phone_num)
    account = []
    updateAcc = UpdateAccount.updateAcc(account_id, email, phone_num)
    account_info = UpdateAccount.getAcc(account_id)
    account.append(account_info.name)
    account.append(account_info.email)
    account.append(account_info.phone_num)
    return account


class RemoveStudent:

  def __init__(self):
    student_id = 0
    name = None
    gpa = 0
    year = 0
    sem_type = None

  @staticmethod
  def removeStudent(student_id):
    removeStudent = Database.select(Query.removeFailStudent, student_id)

  @staticmethod  #feature 9
  def removeFailStudent():
    students = []
    student_data = Database.select(Query.getFailStudent)
    print(student_data)
    for s in student_data:
      students.append(s['name'])
      students.append(s['gpa'])
      removeStudent = RemoveStudent.removeStudent(s['student_id'])
    return students


class RemoveStaff:

  def __init__(self):
    staff_id = 0
    name = None
    education_level = None
    school_name = None
    degree = None

  @staticmethod
  def removeStaff(staff_id):
    removeStaff = Database.select(Query.removeStaff, staff_id)

  @staticmethod
  def remove(staff_id):  #feature 10
    staff = []
    staff_data = Database.select(Query.getStaffAndQualifcation, staff_id)
    print(staff_data)
    for s in staff_data:
      staff.append(s['name'])
      staff.append(s['education_level'])
      staff.append(s['school_name'])
      staff.append(s['degree'])
    print(staff)
    removeStaff = RemoveStaff.removeStaff(staff_id)
    return staff
