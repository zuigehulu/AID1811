from sys import argv

script,user_name = argv
prompt = ">"

print"hi %r, i'm %r"%(user_name,script)
print"are you like me? %r"%(user_name)
likes = raw_input(prompt)
print"likes"