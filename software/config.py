import dataclasses
from os import getenv


@dataclasses.dataclass
class Env:
    proto: str = 'https://'
    url: str = 'mail.google.com/'
    host: str = getenv('HOST', f'{proto}{url}')
    # ВСЕ данные являются тестовыми. Их не существует, даже, если указано "real"
    login: str = getenv('MAIL_LOGIN', 'fake-mail@gmail.com')
    password: str = getenv('MAIL_PASSWORD', 'non_password_1')
    consumer_1_real: str = getenv('MAIL_CONSUMER_REAL', 'consumer-1@gmail.com')
    consumer_2_fake: str = getenv('MAIL_CONSUMER_REAL_FAKE', 'consumer-2@gmail.com')



