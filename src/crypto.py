from typing import TypeAlias


from argon2 import PasswordHasher


password_hasher = PasswordHasher()
HashedPassword: TypeAlias = str


def hash_password(plaintext_password: str) -> HashedPassword:
    return password_hasher.hash(plaintext_password)


def is_password_valid(plaintext_password: str, hashed_password: HashedPassword) -> bool:
    return password_hasher.hash(plaintext_password) == hashed_password
