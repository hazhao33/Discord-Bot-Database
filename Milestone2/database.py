# In this file you must implement your main query methods
# so they can be used by your database models to interact with your bot.

import os
import pymysql.cursors

# note that your remote host where your database is hosted
# must support user permissions to run stored triggers, procedures and functions.
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class Database:

  def _connect(self):
    """
        This method creates a connection with your database
        IMPORTANT: all the environment variables must be set correctly
                   before attempting to run this method. Otherwise, it
                   will throw an error message stating that the attempt
                   to connect to your database failed.
        """
    try:
      conn = pymysql.connect(host=db_host,
                             port=3306,
                             user=db_username,
                             password=db_password,
                             db=db_name,
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
      print("Bot connected to database {}".format(db_name))
      return conn
    except:
      print(
        "Bot failed to create a connection with your database because your secret environment variables "
        +
        "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
      print("\n")

  def _query_response(self,
                      query,
                      values=None,
                      fetchresults=False,
                      many=False):
    connection = self._connect()
    cursor = connection.cursor()
    if values:
      if many:
        cursor.executemany(query, values)
      else:
        cursor.execute(query, values)
    else:
      cursor.execute(query)
    connection.commit()
    connection.close()
    if fetchresults:
      return cursor.fetchall()
    return None

  @staticmethod
  def select(query, values=None):
    db = Database()
    return db._query_response(query, values, fetchresults=True)


class Query:
  getAllStudentEnrollment = """
    SELECT *
    FROM EducationDB.Student s
    JOIN EducationDB.Student_Enrollment se ON s.student_id = se.student
    JOIN EducationDB.Class c ON s.student_id = c.class_id
    JOIN EducationDB.Semester sem ON s.student_id = sem.semester_id
    """
  getStudentEnrollment = """
    SELECT *
    FROM EducationDB.Student s
    JOIN EducationDB.Student_Enrollment se ON s.student_id = se.student
    JOIN EducationDB.Class c ON s.student_id = c.class_id
    JOIN EducationDB.Semester sem ON s.student_id = sem.semester_id
    WHERE s.student_id = %s
    """

  getMajorAvgGPA = """
    SELECT major_id, m.major_name, AVG(ar.gpa) AS Average_GPA
    FROM Major_enrollment me
    JOIN Major m ON me.major = m.major_id
    JOIN Student s ON me.student = s.student_id
    JOIN Academic_Record ar ON me.student = ar.student
    WHERE m.major_id = %s
    GROUP BY me.major, m.major_id;
    """

  getAllMajorAvgGPA = """
   SELECT major_id, m.major_name, AVG(ar.gpa) AS Average_GPA
    FROM Major_enrollment me
    JOIN Major m ON me.major = m.major_id
    JOIN Student s ON me.student = s.student_id
    JOIN Academic_Record ar ON me.student = ar.student
    GROUP BY me.major, m.major_id;
    """

  getAMajorGpa = """
   SELECT major_id, m.major_name, AVG(ar.gpa) AS Average_GPA
    FROM Major_enrollment me
    JOIN Major m ON me.major = m.major_id
    JOIN Student s ON me.student = s.student_id
    JOIN Academic_Record ar ON me.student = ar.student
    WHERE m.major_name = %s
    GROUP BY me.major, m.major_id;
    """

  getHighGpaStudent = """
    SELECT student_id, name, gpa
    FROM  EducationDB.Student s
    INNER JOIN  EducationDB.Academic_Record ar ON s.student_id = ar.student
    WHERE student_id = %s
    """

  getAllHighGpaStudent = """
    SELECT student_id, name, gpa
    FROM  EducationDB.Student s
    INNER JOIN  EducationDB.Academic_Record ar ON s.student_id = ar.student
    """

  getAcademicRecord = """
    SELECT * FROM Academic_Record ar
    JOIN Student s ON s.student_id = ar.student
    WHERE student_id = %s;
  """
  updateStudentGpa = """
    UPDATE Academic_Record SET gpa = %s
    WHERE student = %s;
  """

  addStaff = """
    INSERT INTO Staff (staff_id, name, dob)
    SELECT COALESCE(MAX(staff_id), 0) + 1, %s, %s FROM Staff;
  """

  getLastStaff = """
    SELECT * FROM Staff ORDER BY staff_id DESC
  """

  addDepartment = """
    INSERT INTO Staff_Department (sd_id, staff, department) 
    SELECT COALESCE(MAX(sd_id), 0) + 1, %s, %s FROM Staff_Department;
  """

  getstaffAndDepartment = """
    SELECT name, title FROM Staff s
    JOIN Staff_Department sd ON s.staff_id = sd.staff
    JOIN Department d ON sd.department = d.department_id
    WHERE staff_id = %s;
  """

  studentCourseEnrollment = """
    INSERT INTO Course_Enrollment (course_enroll_id, class, student) 
    SELECT COALESCE(MAX(course_enroll_id), 0) + 1, %s, %s FROM Course_Enrollment;
  """

  studentSemesterEnrollment = """
    INSERT INTO Student_Enrollment (student_enroll_id, student, semester) 
    SELECT COALESCE(MAX(student_enroll_id), 0) + 1, %s, 2 FROM Student_Enrollment;
  """

  getAccount = """
    SELECT * FROM Account
    WHERE account_id = %s
  """

  updateAccount = """
    UPDATE Account
    SET email = %s, phone_num = %s
    WHERE account_id = %s;
  """

  removeFailStudent = """
    DELETE se FROM Student_Enrollment se
    INNER JOIN Student s ON se.student = s.student_id
    INNER JOIN Academic_Record ar ON s.student_id = ar.student
    WHERE s.student_id = %s;
  """

  getFailStudent = """
    SELECT DISTINCT student_id, name, gpa FROM Student_Enrollment se
    INNER JOIN Student s ON se.student = s.student_id
    INNER JOIN Academic_Record ar ON s.student_id = ar.student
    INNER JOIN Semester sem ON se.semester = sem.semester_id
    WHERE ar.gpa < 2;
  """

  getStaffAndQualifcation = """
    SELECT * FROM Staff
    INNER JOIN Qualification ON Staff.staff_id = Qualification.staff
    WHERE staff_id = %s;
  """

  removeStaff = """
    DELETE s FROM Staff s
    INNER JOIN Qualification q ON s.staff_id = q.staff
    WHERE s.staff_id = %s;
  """