#!/usr/bin/env python
# coding: utf-8

# # Day_2

# ## Comments, Escape Sequences & Print Statement

# In[1]:


print("Hey i am a Good Boy")


# # Python Comments:
# - Comments can be used to explain Python code.
# - Comments can be used to make the code more readable.
# - Comments can be used to prevent execution when testing code.
# ## Creating a Comment
# - Comments starts with a #, and Python will ignore them:
# * Example:

# In[2]:


# Hey Sam, Pleas Dont remove this line
print("Hey i am a Good Boy")


# ## Multiline Comments
# * To add Multiline Comments you can add a triple quotes('''Comment''' or """"Comment""") in your code, and place your comment inside it:
# * Example: 

# In[3]:


"""Hey Sam, 
Pleas Dont remove this line
This line is important"""
print("Hey i am a Good Boy")


# # Python Escape Character:
# * To insert characters that are illegal in a string, use an escape character.
# * An escape character is a backslash \ followed by the character you want to insert.
# * An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# In[4]:


print("Hey i am a Good Boy and "Sam" is also a good boy/girl")
#You will get an error if you use double quotes inside a string that are surrounded by double quotes:


# ### To fix this problem, 
#      use the escape character  \" :

# In[5]:


print("Hey i am a Good Boy and \"Sam\" is also a good boy/girl")


# ### Other escape characters used in Python:
1 \' or \"	Single or  Quote	
2 \\	Backslash	
3 \n	New Line	
4 \r	Carriage Return	
5 \t	Tab	
6 \b	Backspace	
# In[7]:


#1 \'	Single Quote
#To Represents a Single or Double quote character.
print('It\'s allright.')


# In[8]:


#2 \\	Backslash
# To include a backslash in a string, you would use \\: 
print("This string contains a backslash \\")       


# In[9]:


#3 \n	New Line
#To Represents a newline character, moving the cursor to the beginning of the next line.
print("Hello, Samarth!\nWelcome to Python.")


# In[10]:


#4 \r	Carriage Return
#The \r escape character moves the cursor to the beginning of the line. It can overwrite the existing text.
print("Hello, Samarth!\rHi")


# In[11]:


#5 \t	Tab
#The \t escape character inserts a tab space between words or characters.
print("Hello\tSamarth\tMore")


# In[14]:


#6 \b	Backspace
#The \b escape character moves the cursor one character back, effectively deleting the last character.
print("Hello Samarth\b")


# In[ ]:





# # Python print() Function
# * The print() function prints the specified message to the screen
# * Syntax:
#     print(object(s), sep=separator, end=end, file=file, flush=flush)

# In[15]:


#Any object
print('This is Object')


# In[16]:


#sep(separator) 	Separate the object
print('Welcome','to','Samarth','tech', sep="--")


# In[17]:


#end 	Specify what to print at the end. Default is '\n' (line feed)
print('Welcome','to')
print('Samarth','tech')


# In[18]:


print('Welcome','to', end=' ')
print('Samarth','tech')


# In[19]:


print('Welcome','to', end='\t') #\t escape character inserts a tab space between words
print('Samarth','tech')


# In[20]:


print('Welcome','to', end='\r') #\r overwrite the existing text
print('Samarth','tech')


# In[21]:


#File: This will create a new file and writing the data in the print() function to the that text file
sourcefile = open('python.txt','w')
print('Welcome to Samarth tech!', file=sourcefile)
sourcefile.close()


# In[22]:


pwd #My Directory 


# In[23]:


#Flush: flushes the stream/file explicitly if set to true
for i in range(10):
    print(i)


# In[24]:


for i in range(10):
    print(i, flush=True)
    
#The flush() function can also be used with the print() function to immediately display output to the console, especially when the default buffering behavior might delay it.
#Without flush=True, the output might be buffered and displayed all at once after the loop completes.


# In[ ]:





# In[ ]:




