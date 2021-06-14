Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hours challenge")
30 days 30 hours challenge
>>> print('30 days 30 hours challenge')
30 days 30 hours challenge
>>> hours="thirty"
>>> hours
'thirty'
>>> hours[1:
      ]
'hirty'
>>> hours[1:6]
'hirty'
>>> hours[0:]
'thirty'
>>> hours[:6]
'thirty'
>>> print(hours)
thirty
>>> days="thirty days"
>>> days
'thirty days'
>>> print(days)
thirty days
>>> print(days[0])
t
>>> print(days[1:])
hirty days
>>> print(days.lowers())
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(days.lowers())
AttributeError: 'str' object has no attribute 'lowers'
>>> printy(days.lower())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    printy(days.lower())
NameError: name 'printy' is not defined
>>> print(days.lower())
thirty days
>>> print(days.upper())
THIRTY DAYS
>>> challenges="i will win"
>>> challenges
'i will win'
>>> print(len(challenge))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(len(challenge))
NameError: name 'challenge' is not defined
>>> print(len(challenges))
10
>>> print(challenges.upper())
I WILL WIN
>>> 'string concatination'
'string concatination'
>>> a="30 days"
>>> b="20 days"
>>> c=a+""+b
>>> print(c)
30 days20 days
>>> a= 20
>>> b=30
>>> a+b
50
>>> c=a+b
>>> c
50
>>> print(c)
50
>>> name1="vandana"
>>> name2="yashu"
>>> name1 + " " +name2
'vandana yashu'
>>> a="30 days"
>>> b="20 days"
>>> c=a+" " +b
>>> print(c)
30 days 20 days
>>> "casefold"
'casefold'
>>> text="thirty days and thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> x=text.capitalize()
>>> print(x)
Thirty days and thirty hours
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x=text.find(r)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x=text.find(r)
NameError: name 'r' is not defined
>>> x=text.find("r")
>>> print(x)
3
>>> x=text.isalpha()
>>> x=text.isalnum()
>>> print(x)
False
>>> x=text.isalpha()
>>> print(x)
False
>>> 