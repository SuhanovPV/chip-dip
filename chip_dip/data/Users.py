import dataclasses


@dataclasses.dataclass
class User:
    login: str
    first_name: str
    middle_name: str
    last_name: str
    email: str
    mobile: str

    def __repr__(self):
        return f'User: login: {self.login}; name: {self.first_name} {self.last_name}'


user = User(
    login='ssuxxarr',
    first_name='Павел',
    middle_name='Викторович',
    last_name='Суханов',
    email='ssuxxarr@mail.com',
    mobile='+79030266669'
)
