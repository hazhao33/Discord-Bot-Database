"""
The code below is just representative of the implementation of a Bot. 
However, this code was not meant to be compiled as it. It is the responsability 
of all the students to modifify this code such that it can fit the 
requirements for this assignments.
"""
import database
from database import Database, Query
import os
import discord
from discord.ext import commands
from models import *

TOKEN = os.environ['DISCORD_TOKEN']
db = Database
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
  # everything in this method executes automatically when the bot is put online
  print(f"{bot.user.name} joined the room")
  # you need to import the file database.py as db for the next lines to work
  database = Database()
  if database._connect():
    print(f"{bot.user.name} is connected to the remote database")
  else:
    print(f"{bot.user.name} was unable to connect to the remote database")


@bot.command(
  name="test",
  description="write your database business requirement for this command here")
async def _test(ctx, arg1):
  testModel = TestModel(ctx, arg1)
  response = testModel.response()
  await ctx.send(response)


# TODO: complete the following tasks:
#       (1) Replace the commands' names with your own commands
#       (2) Write the description of your business requirement in the description parameter
#       (3) Implement your commands' methods.


#feature 1
@bot.command(
  description=
  "Find all the students and their enrolled classes for the semester year 2023."
)
async def getStudentEnrollment2023(ctx):
  student = ClassEnrollment.getFall2023()
  await ctx.send(f"{student}")


#feature 2
@bot.command(
  description="For each major, find the average GPA of the students.")
async def getMajorAvgGPA(ctx):
  major = MajorAveGPA.getAll()
  await ctx.send(f"{major}")


#feature 3
@bot.command(description="Find all the students with a GPA higher than input")
async def getStudentGPAhigh(ctx, wantGpa):
  student = HighGPA()
  studentWithHighGpa = student.getHigherGpa(wantGpa)
  await ctx.send(f"{studentWithHighGpa}")


#feature 4
@bot.command(
  description=
  "Find all the students enrolled in a class with class name as input.")
async def getStudentEnroll(ctx, className):
  student = ClassEnrollment()
  studentEnrolledInTheClass = student.getDatabaseClassEnrollment(className)
  await ctx.send(f"{studentEnrolledInTheClass}")


#feature 5
@bot.command(
  description=
  "Add a new staff member with name and date of birth  and assign the staff to a department with a department_id."
)
async def addStaffAndTpCSDept(ctx, name, dob, department_id):
  staff = StaffAndDepartment()
  addStaff = staff.addStaffAndToDepartment(name, dob, department_id)
  await ctx.send(f"{addStaff}")


#feature 6
@bot.command(
  description=
  "Enroll a student in a class in the spring 2023 semester with the student_id and class_id."
)
async def enrollCourseInSpring2023(ctx, student_id, class_id):
  student = ClassEnrollment()
  student_info = student.enrollToClassAndSemester(student_id, class_id)
  await ctx.send(f"{student_info}")


#feature 7
@bot.command(
  description="Update the student's GPA with student_id and new gpa score.")
async def updateGPA(ctx, student_id, gpa):
  student = UpdateGpa()
  newGpaStudent = student.updateGpa(student_id, gpa)
  await ctx.send(f"{newGpaStudent}")


#feature 8
@bot.command(
  description=
  "Update an account's email, and phone_num with account_id, new email, and new phone_num."
)
async def updateAccount(ctx, account_id, email, phone_num):
  account = UpdateAccount()
  account_info = account.updateStudentInfo(account_id, email, phone_num)
  await ctx.send(f"{account_info}")


#feature 9
@bot.command(
  description="Remove all student from a semester with GPA lower than 2")
async def removeFailStudent(ctx):
  student = RemoveStudent()
  student_info = student.removeFailStudent()
  await ctx.send(f"{student_info}")


#feature 10
@bot.command(
  description="Remove a staff member and their qualification with staff_id.")
async def removeStaff(ctx, staff_id):
  staff = RemoveStaff()
  staff_info = staff.remove(staff_id)
  await ctx.send(f"{staff_info}")


#feature 15
@bot.command(
  description=
  "Find all the students enrolled in a class with class name as input.")
async def getAvgGpaFor(ctx, majorName):
  major = MajorAveGPA()
  major_info = major.aMajorGpa(majorName)
  await ctx.send(f"{major_info}")


@bot.command(name="cmd_11",
             description="database business requirement #11 here")
async def _command11(ctx, *args):
  await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_12",
             description="database business requirement #12 here")
async def _command12(ctx, *args):
  await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_13",
             description="database business requirement #13 here")
async def _command13(ctx, *args):
  await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_14",
             description="database business requirement #14 here")
async def _command14(ctx, *args):
  await ctx.send("This method is not implemented yet")


bot.run(TOKEN)
