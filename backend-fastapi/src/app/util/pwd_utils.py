from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def get_pwd_hash(password: str):
    return pwd_context.hash(password)
