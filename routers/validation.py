from flask import session


def validate_session():
    return "user" in session


def validate_text_field(text: str):
    return text.strip()
