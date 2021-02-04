s = '123sa'
for i, c in enumerate(s):
     if not c.isdigit():
         break
 
s[:i] + s[i:].capitalize()
