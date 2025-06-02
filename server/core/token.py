import uuid

def generate_email_token() -> str:
    return str(uuid.uuid4())
