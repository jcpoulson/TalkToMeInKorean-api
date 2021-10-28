import bcrypt
import os

password = b"brodude"

hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

checked_pw = bcrypt.checkpw(b'brodude', hashed_pw)

lol = password.decode()
lol_encoded = str.encode(lol)

print("Decoded String: " + lol)
print(f"Encoded String: {lol_encoded}")

print('\n\n')

# okay well for some odd reason, when I set environment varaibles for the connection strings
# the os module just can't seem to reach them, just another reason to complain about windows LOL

print(os.getenv('AWS_ACCESS_KEY_ID'))
