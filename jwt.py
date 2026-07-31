from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import jwt
import datetime

app = FastAPI()

SECRET_KEY = "my_super_secret_key_123"
ALGORITHM = "HS256"

@app.get("/accessTojwt")
def convert_access_to_jwt(access_token: str = None):
    # ১. যদি access_token পাস না করা হয়
    if not access_token:
        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "access_token parameter is required",
                "credit": "@RFG_GAMER"
            }
        )
    
    try:
        # পে-লোড তৈরি
        payload = {
            "access_token": access_token,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        }
        
        # JWT তৈরি করা
        generated_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        
        # সফল হলে রেসপন্স
        return {
            "status": "success",
            "token": generated_jwt,
            "credit": "@RFG_GAMER"
        }
        
    except Exception as e:
        # ২. যদি কোনো কারণে JWT তৈরি করতে ব্যর্থ (Fail) হয়
        return JSONResponse(
            status_code=500,
            content={
                "status": "failed",
                "message": f"JWT generation failed: {str(e)}",
                "credit": "@RFG_GAMER"
            }
        )