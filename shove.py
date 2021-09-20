#!/usr/bin/env python3
import os
print("What is the reason for your update")
reason = input()

cmd = 'cd ~/mycode;git add *;git commit -m "print(reason)";git push origin;'
os.system(cmd)
#print("`(home_dir)/mycode;git add *;git commit -m \"(reason)\",git push origin;`") 

