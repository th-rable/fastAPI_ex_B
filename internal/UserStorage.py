users = {'admin':{'psword':'admin', 'name':'admin'}}

from pydantic import BaseModel
class LoginItem(BaseModel):
    id: str
    psword: str

class RigisterItem(BaseModel):
    id: str
    psword: str
    name: str


def Login(item: LoginItem):
    if item.id not in users:
        return {'status':False, 'message':'ID Wrong'}
    if item.psword != users[item.id]['psword']:
        return {'status':False, 'message':'PW Wrong'}
    return {'status':True, 'message':'Hello '+users[item.id]['name']}

def Register(item: RigisterItem):
    if item.id in users:
        return {'status':False, 'message':'Same ID Exist'}
    users[item.id]={'psword':item.psword,'name':item.name}
    return {'status':True, 'message':'OK'}