#!/usr/bin/env python3
import os
#get the reason for update from user. This is a string catch of what an updated is being pushed
print("What is the reason for your update")
reason = input()

pre = 'git status'
#cmd = 'cd ~/mycode;git add *;git commit -m "print(reason)";git push origin main;'
#cmd = 'cd ~/mycode;git add *;git commit -m "+ reason";git push origin main;'
#cmd = 'cd ~/mycode;git add *;git commit -m "{0.reason}";git push origin main;'
#cmd = 'cd ~/mycode;git add *;git commit -m "+ reason +";git push origin main;'
cmd = 'cd ~/mycode;git add *;git commit -m "' + reason + '";git push origin main;'
post = 'git status'

#os commands for system. Take variables from commands pre cmd and post
os.system(pre)
os.system(cmd)
os.system(post)
