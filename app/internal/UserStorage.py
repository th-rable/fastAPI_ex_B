import random
import string

users = {'admin':{'psword':'admin', 'name':'어드민', 'grade':2025}}
sessionKey = {}

from pydantic import BaseModel
class LoginItem(BaseModel):
    id: str
    psword: str

class RigisterItem(BaseModel):
    id: str
    psword: str
    name: str
    grade: int

class CheckLoginItem(BaseModel):
    id: str
    key: str
    
class CheckIdItem(BaseModel):
    id: str



def MakeSessionKey(n: int):
    rand_str=''
    for i in range(n):
        rand_str += str(random.choice(string.ascii_letters+string.digits))
    return rand_str

def Login(item: LoginItem):
    if item.id not in users:
        return {'ok':True,'status':False, 'message':'ID Wrong'}
    if item.psword != users[item.id]['psword']:
        return {'ok':True,'status':False, 'message':'PW Wrong'}
    key=MakeSessionKey(30)
    sessionKey[item.id]=key
    return {'ok':True,'status':True, 'message':'Hello '+users[item.id]['name'], 'key':key}

def Register(item: RigisterItem):
    if item.id in users:
        return {'ok':False, 'message':'Same ID Exist'}
    grade = 2025-item.grade
    if item.grade == 10000: grade = 10000
    if item.grade == -10000: grade = -10000
    users[item.id]={'psword':item.psword,'name':item.name,'grade':grade}
    return {'ok':True, 'message':'OK'}

def CheckLogin(item: CheckLoginItem):
    if item.id not in sessionKey:
        return {'status':False, 'message':'Auth Failed'}
    if sessionKey[item.id]!=item.key:
        return {'status':False, 'message':'Auth Failed'}
    return {'status':True, 'message':'OK'}

def CheckId(item: CheckIdItem):
    if item.id in users:
        return {'result': True}
    return {'result': False}

def Getname(item: CheckIdItem):
    if item.id not in users:
        return {'result': None}
    return {'result': users[item.id]['name']}

def Logout(item: CheckLoginItem):
    islogin=CheckLogin(item)
    if(islogin['status']):
        del(sessionKey[item.id])
        return {'result':True}
    return {'result':False}