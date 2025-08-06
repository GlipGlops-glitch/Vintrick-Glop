# vintrick-backend/app/main.py

import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import vintrace_api
from app.api.routes import harvestloads    # Import harvestloads routes
from app.api.routes import shipments       # Import shipments routes
from app.api.routes import blends          # Import blends routes
from app.api.routes import trans_sum
app = FastAPI(debug=True)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Replace "*" with specific origins for better security
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods
    allow_headers=["*"],      # Allow all headers
)


# Register the routers
app.include_router(harvestloads.router, prefix="/api", tags=["harvestloads"])
app.include_router(shipments.router,   prefix="/api", tags=["shipments"])
app.include_router(blends.router,      prefix="/api", tags=["blends"])
app.include_router(vintrace_api.router, prefix="/api/vintrace_api", tags=["vintrace_api"])
app.include_router(trans_sum.router, prefix="/api", tags=["trans_sum"])



# Exception handler for HTTP exceptions
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc):
    logging.error(f"HTTP Error: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

# Exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc):
    logging.error(f"Validation error: {exc.errors()} Body: {exc.body}")
    return JSONResponse(status_code=422, content={"detail": exc.errors(), "body": exc.body})

# Generic exception handler for unhandled errors
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc):
    logging.error(f"Unhandled error: {exc}", exc_info=True)
    # For debugging, you can optionally add: str(exc)
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
