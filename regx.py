# Regular Expression
# =================

# it is a special patter or an expression wich is used
# to extrat,search,find,replae the data from a 
# colltion of string


# How the expression ??

# -----------------------

# r'\d\c' --------- > sample regular expression

# re ------- > re module to perform the regular expression function

# This module exports the following functions:
# =====================================================
# match     Match a regular expression pattern to the beginning of a string.
# fullmatch Match a regular expression pattern to all of a string.
# search    Search a string for the presence of a pattern.
# sub       Substitute occurrences of a pattern found in a string.
# subn      Same as sub, but also return the number of substitutions made.
# split     Split a string by the occurrences of a pattern.
# findall   Find all occurrences of a pattern in a string.
# finditer  Return an iterator yielding a match object for each match.
# compile   Compile a pattern into a RegexObject.
# purge     Clear the regular expression cache.
# escape    Backslash all non-alphanumerics in a string.



# Used to search the charchteres
# -----------------------------------------------------------------------------------
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)

# # r'^$'
# # --------------------------------------------------------------------------------
# # Boundary and anchors
# # ------------------------------------------------------------
# # \ ------ > search single charchtere
# # \b      - Word Boundary
# # \B      - Not a Word Boundary
# # ^       - Beginning of a String
# # $       - End of a String

# shivam.vku@gmail.com


# [\w\.\w\]@[\w\.\w]

# ------------------------------------------------------------------
# search gropu of charchteres
# ---__________________________________________________
# []      - Matches Characters in brackets
# [^]    - Matches Characters NOT in brackets

# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
# range of charchteres
# -----------------------------------------
# ( )     - Group


 


# Quantifiers:
# =======================================================
# *       - 0 or More
# +       - 1 or More------------------> exends



# ?       - 0 or One


# # Flags
# # --------------------------------------------------
# #   |       - Either Or
# A  -------- ASCII

data = '''[11:00 PM, 8/13/2018] +91 80084 10482: sonamthapa.dl@gmail.com
[11:19 PM, 8/13/2018] +1 (647) 877-5143: madhusrichandu@gmail.com
[11:23 PM, 8/13/2018] +971 58 973 2576: kanagalasravya@yahoo.com
[11:24 PM, 8/13/2018] +91 80198 64264: bachimanchiajay@gmail.com
[11:24 PM, 8/13/2018] +91 96001 09750: avinash1097.dl@gmail.com
[11:24 PM, 8/13/2018] +91 95022 93612: surendra.funny@gmail.com
[11:24 PM, 8/13/2018] +91 96520 21971: poojadncla2514@gmail.com
[11:25 PM, 8/13/2018] +91 99851 91436: nanda.pvnk@gmail.com
[11:25 PM, 8/13/2018] +91 96001 09750: Sir has arranged interview for python completed students this Saturday....
[11:25 PM, 8/13/2018] +91 96001 09750: So
[11:25 PM, 8/13/2018] +91 96001 09750: Be prepared for that
[11:41 PM, 8/13/2018] +91 81253 64265: surya.irukulla@gmail.com
[12:04 AM, 8/14/2018] +91 99511 58249: pavan24.dl@gmail.com
[12:14 AM, 8/14/2018] +91 75699 61518: saikiranreddy.dl@gmail.com
[6:21 AM, 8/14/2018] +91 97009 37058: satishparida111@gmail.com
[6:48 AM, 8/14/2018] +91 80193 96040: sharan.santosh.ss@gmail.com
[6:58 AM, 8/14/2018] +91 96667 55505: vineethchinthala0505@gmail.com
[7:02 AM, 8/14/2018] +91 90528 51769: avinash34.dl@gmail.com
suresh9406@gmail.com
1. Whetting Your Appetite
2. Using the Python Interpreter
2.1. Invoking the Interpreter
2.1.1. Argument Passing
2.1.2. Interactive Mode
2.2. The Interpreter and Its Environment
2.2.1. Source Code Encoding
3. An Informal Introduction to Python
3.1. Using Python as a Calculator
3.1.1. Numbers
3.1.2. Strings



Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560-555-5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com

Jennifer Martin-White
714-555-7405
212 Cedar St., Sunnydale CT 74983
jenniferwhite@bogusemail.com

Erick Davis
800-555-6771
519 Washington St., Olympus TN 32425
tomdavis@bogusemail.com

Neil Patterson
783,555,4799
625 Oak St., Dawnstar IL 61914
neilpatterson@bogusemail.com

Laura Jefferson
516.555.4615
890 Main St., Pythonville LA 29947
laurajefferson@bogusemail.com

Maria Johnson
127-555-1867
884 High St., Braavos‎ME 43597
mariajohnson@bogusemail.com

Michael Arnold
608*555*4938
249 Elm St., Quahog OR 90938
michaelarnold@bogusemail.com '''

import re 
from re import *

# var  = compile(r'\.')
# print(var)

# mat = var.finditer(data)
# print(mat)
# # print(next(mat))
# for a in mat :
# 	print(a)




# var  = compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
# mat = var.finditer(data)
# for a in mat :
# 	print(a)



# var  = compile(r'[\w\.]+\@[\w\.\w]+')
# mat = var.finditer(data)
# for a in mat :
# 	print(a)







# var  = compile(r'([\w\.]+)(\@[\w\.\w]+)')


# var = search(r'([\w\.]+)(\@[\w\.\w]+)',data)
# print(var)
# print(type(var))


# s = sub(r'([\w\.]+)(\@[\w\.\w]+)',r'\1@digitallync.com',data)
# print(s)