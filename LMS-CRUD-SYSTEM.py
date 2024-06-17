import os
import platform
from sys import exit

global studentlist
studentlist = ["Kushal Pokhrel", "Peter Parker", "Adam Weiss", "Steve Wozniack", "Larry Page", "John Hopkins"]

def studentmanagement():

	print("\n++++Welcome to AIH College Student Management System++++")
	print("\n++++The CRUD based Student Management System using Python++++")
	print("\n++++Created by AIH \N{COPYRIGHT SIGN} All Rights Reserved++++")
	print("\n++++Please Select from the Lists of Choices Below++++\n ")
	print("[Press 1 to Display the List of students]")
	print("[Press 2 to Add a New Student]")
	print("[Press 3 to Search for a Student]")
	print("[Press 4 to Delete a Student]")

	try:
		x = int(input("Enter a choice: "))
	except ValueError:
		exit("\nHandled Exception as Input is not an number!!")
	else:
		print("\n You Selected", x)

	if(x==1):
		print("Student List\n")
		for students in studentlist:
			print("++ {} ++".format(students))

	elif(x==2):
		studentnew = input("Enter New Student: ")
		if(studentnew in studentlist):
			print("\nThis Student {} Already In The Table".format(studentnew))
		else:
			studentlist.append(studentnew)
			print("\n++ {} Added Successfully ++\n".format(studentnew))
			for students in studentlist:
				print("++ {} ++".format(students))

	elif(x==3):
		studentsearching = input("Choose Student Name To Search: ")
		if(studentsearching in studentlist):
			print("\n++ There is a Record Found of this Student {} ++".format(studentsearching))
		else:
			print("\n++ There is No Record Found Of this Student {} ++".format(studentsearching))

	elif(x==4):
		studentdelete = input("Choose a Student Name To Delete: ")
		if(studentdelete in studentlist):
			studentlist.remove(studentdelete)
			print((studentdelete),"was deleted Successfully")
			for students in studentlist:
				print("++ {} ++".format(students))
		else:
			print("\n++ There is No Record Found of the Student {} ++".format(studentdelete))

	elif(x < 1 or x > 4):
		print("Please Enter Valid Choice")

studentmanagement()

def continueAgain():
	runningagain = input("\nWant to continue the process press y/n?: ")
	if(runningagain.lower() == 'y'):
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		studentmanagement()
		continueAgain()
	else:
		quit()

continueAgain()
