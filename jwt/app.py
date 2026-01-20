import jwt_handler
from datetime import datetime,timedelta

SECRET_KEY = "mysecretkey"

payload = {
    "user_id": 101,
    "exp": datetime.utcnow() + timedelta(minutes=30)
}
token = jwt_handler.encode(payload, SECRET_KEY, algorithm="HS256")

print(token)

decoded = jwt_handler.decode(token, SECRET_KEY, algorithms=["HS256"])

print(decoded)