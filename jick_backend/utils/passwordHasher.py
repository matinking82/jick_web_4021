from passlib.hash import pbkdf2_sha256

def hashPass(password:str):
    return pbkdf2_sha256.hash(password)

def verifyPass(password:str, hash:str):
    return pbkdf2_sha256.verify(password, hash)