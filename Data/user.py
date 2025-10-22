from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    address: str
    birthdate: tuple[str, str, str]  # (year, month, day)
    subject: str
    hobby: list[str]
    file: str
    state: str
    city: str


test_user = User(
    first_name='Test',
    last_name='User',
    email='test@gmail.com',
    gender='Male',
    phone='7999999999',
    address='Test Street 123',
    birthdate=('2003', 'March', '23'),
    subject='English',
    hobby=['Sports', 'Reading', 'Music'],
    file='examplePhoto.png',
    state='Rajasthan',
    city='Jaipur'
)
