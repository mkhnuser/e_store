from argon2 import PasswordHasher
import argon2.exceptions


password_hasher = PasswordHasher()


def hash_password(plaintext_password: str) -> str:
    try:
        return password_hasher.hash(plaintext_password)
    except argon2.exceptions.Argon2Error as e:
        # TODO: SOMETHING REALLY BAD HAS HAPPENED.
        print(e)
        raise
    except Exception as e:
        print(e)
        raise


def is_password_valid(hashed_password: str, plaintext_password: str) -> bool:
    try:
        return password_hasher.verify(hashed_password, plaintext_password)
    except argon2.exceptions.Argon2Error as e:
        # TODO: SOMETHING REALLY BAD HAS HAPPENED.
        print(e)
        raise
    except Exception as e:
        print(e)
        raise
