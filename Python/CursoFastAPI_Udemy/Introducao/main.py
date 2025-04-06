from pydantic import BaseModel,field_validator

def f(name:str):
    pass

user = {
    "name":"Rafael",
    "age":12,
    "Email":"fasdfa@asdfasd.com"
}


class User(BaseModel):
    name:str
    age:int
    email:str

    @field_validator("email")
    def validate_email(cls,value):
        if "@" not in value:
            raise ValueError("Invalid Email")
        return value

def f(user:User):
    print(user.age)
    pass

user = User(name='Rafael',age=20,email="afsdasfdasd.com")
f(user)
print(user)