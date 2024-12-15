import dataclasses


@dataclasses.dataclass
class User:
    login: str
    first_name: str
    middle_name: str
    last_name: str
    email: str
    mobile: str


user = User(
    login='ssuxxarr',
    first_name='Павел',
    middle_name='Викторович',
    last_name='Суханов',
    email='ssuxxarr@mail.com',
    mobile='+79030266669'
)
