# vintrick-backend/app/main.py
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware  # ✅ Import CORS middleware

from app.api.routes import harvestloads  # ✅ Import your routes

app = FastAPI(debug=True)

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# ✅ Register the router
app.include_router(harvestloads.router, prefix="/api", tags=["harvestloads"])

# ✅ Exception handler for HTTP exceptions
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc):
    logging.error(f"HTTP Error: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

# ✅ Exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc):
    logging.error(f"Validation error: {exc.errors()} Body: {exc.body}")
    return JSONResponse(status_code=422, content={"detail": exc.errors(), "body": exc.body})

# ✅ Generic exception handler for unhandled errors
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc):
    logging.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})