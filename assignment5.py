# # Exercise 1: (score : 1)
# # Write a Python program to read a file and display its contents

# file=open("C:\\Users\\ktomj\\OneDrive\\Desktop\\File handling\\hello2.txt",'r')
# read=file.read()
# print(read)
# file.close()
#-#-#-#-#-#-#-#-#-#-#-#-#-#  OR   #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# file_path = input("Enter the path to the file: ")
# file = open(file_path, 'r')
# contents = file.read()
# print(contents)
# file.close()

#************************************************************************************************************#
# # Exercise 2: (score : 1)
# # Write a Python program to copy the contents of one file to another file


# with open("C:\\Users\\ktomj\\OneDrive\\Desktop\\File handling\\hello2.txt",'r') as det:
#     with open("C:\\Users\\ktomj\\OneDrive\\Desktop\\File handling\\hello.txt",'w') as cop:
#         contents=det.read()
#         cop.write(contents)
# print(f' this is :{cop}')
#
#______to check__________________________________________#
# with open("C:\\Users\\ktomj\\OneDrive\\Desktop\\File handling\\hello.txt",'r') as cop:
#     data = cop.read()
#     print(data)
#-----------****************-------------************OR**************-----------------****************--------------#
# source_file = input("Enter the path to the source file: ")
# destination_file = input("Enter the path to the destination file: ")
# with open(source_file, 'r') as src:
#     with open(destination_file, 'w') as dest:
#         contents = src.read()
#         dest.write(contents)
# print(f"Contents copied from {source_file} to {destination_file}")
# #__________________________TO CHECK_______________________________________________________________#
# with open(destination_file,'r') as edited:
#     x=edited.read()
#     print(x)


# print(f"Contents copied from {source_file} to {destination_file}")

#**************************************************************************************************************#

# # Exercise 3: (score : 2)
# # Write a Python program to read the content of a file and count the total number of words in that file.
# file_path = input("Enter the path to the file: ")
# with open(file_path, 'r') as file:
#     contents = file.read()
#     words = contents.split()
#     word_count = len(words)
#     print(word_count)
#
# print(f"The total number of words in the file is: {word_count}")


#**************************************************************************************************************************************************



# # Exercise 4: (score : 1)
# # Write a Python program that prompts the user to input a string and converts it to an integer.
# # Use try-except blocks to handle any exceptions that might occur

# user_input = input("Enter a string to convert to an integer: ")
# print(type(user_input))
#
# try:
#     integer_value = int(user_input)
#     print(f"The integer value is: {integer_value}")
#     print(type(integer_value))
# except ValueError:
#     print("Error: The input is not a valid integer.")


#**********************************************************************************************************************************************



# Exercise 5: (score : 1)
# Write a Python program that prompts the user to input a list of integers
# and raises an exception if any of the integers in the list are negative.
# def list_int():
#     ip = input('enter list values:')
#     try:
#         l1=[int(num) for num in ip.split()]
#         #print(l1)
#
#         for num in l1:
#             if num<0:
#                 raise ValueError('cant be negative')
#         return l1
#     except ValueError as e:
#         print(f"Error: {e}")
#
# int_list = list_int()
# if int_list:
#     print("You entered a valid list of integers:", int_list)


#**************************************************************************************************************************************************#


# # Exercise 6: (score : 2)
# # Write a Python program that prompts the user to input a list of integers and computes the average of those integers.
# # Use try-except blocks to handle any exceptions that might occur.
# # use the finally clause to print a message indicating that the program has finished running.
#
# def average_list():
#     ip2=input('Enter the number:')
#     try:
#         l1=[int(num) for num in ip2.split()]
#
#         average=sum(l1)/len(l1)
#         print(average)
#
#     except ValueError:
#         print('Cant divide')
#     except ZeroDivisionError:
#         print('zero division error')
#     finally:
#         print('pgm has finished')
# average_list()
#*******************************************************************************************************************************************#
# # Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename and writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.

# filename = input("Enter the filename to write to: ")
# content = input("Enter the content to write to the file: ")
#
# try:
#     with open(filename, 'w') as file:
#         file.write(content)
#     print("File written successfully! Welcome!")
# except IOError:
#     print("Error: An error occurred while trying to write to the file.")
# except Exception as e:
#     print(f"Error: {e}")
# #_________________________________TO READ______________________________________________________________________________________________________________________________________#
# with open("C:\\Users\\ktomj\\OneDrive\\Desktop\\File handling\\hello3.txt",'r') as read:
#     data=read.read()
#     print(data)
