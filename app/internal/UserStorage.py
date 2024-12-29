import random
import string

users = {'admin':{'psword':'admin', 'name':'admin'}}
sessionKey = {}

from pydantic import BaseModel
class LoginItem(BaseModel):
    id: str
    psword: str

class RigisterItem(BaseModel):
    id: str
    psword: str
    name: str

class CheckLoginItem(BaseModel):
    id: str
    key: str

def MakeSessionKey(n: int):
    rand_str=''
    for i in range(n):
        rand_str += str(random.choice(string.ascii_letters+string.digits))
    return rand_str

def Login(item: LoginItem):
    if item.id not in users:
        return {'status':False, 'message':'ID Wrong'}
    if item.psword != users[item.id]['psword']:
        return {'status':False, 'message':'PW Wrong'}
    key=MakeSessionKey(30)
    sessionKey[item.id]=key
    return {'status':True, 'message':'Hello '+users[item.id]['name'], 'key':key}

def Register(item: RigisterItem):
    if item.id in users:
        return {'status':False, 'message':'Same ID Exist'}
    users[item.id]={'psword':item.psword,'name':item.name}
    return {'status':True, 'message':'OK'}

def CheckLogin(item: CheckLoginItem):
    if item.id not in sessionKey:
        return {'status':False, 'message':'Auth Failed'}
    if sessionKey[item.id]!=item.key:
        return {'status':False, 'message':'Auth Failed'}
    return {'status':True, 'message':'OK'}
