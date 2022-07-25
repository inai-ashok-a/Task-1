from pydantic import BaseModel
import re   #importing regular matching from the inbuild class


class User(BaseModel):
    name:str
    age:int
    email:str

def check_email(s):
   pat = "^[a-z0-9-_.]+@[a-z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

