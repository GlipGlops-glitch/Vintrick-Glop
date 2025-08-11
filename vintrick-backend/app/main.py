import logging
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware



from app.api.routes.harvestloads import router as harvestloads_router

from app.api.routes.blends import router as blends_router
from app.api.routes.trans_sum import router as trans_sum_router
from app.api.routes.vintrace_pull import router as vintrace_pull_router
from app.api.routes.meta import router as meta_router
from app.api.routes.trans_sum_sync import router as trans_sum_sync_router

app = FastAPI(debug=True)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Replace "*" with specific origins for better security
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods
    allow_headers=["*"],      # Allow all headers
)

# Register all routers
# app.include_router(bulk_wine_router,   prefix="/api", tags=["bulk_wine"])
# app.include_router(harvest_router,     prefix="/api", tags=["harvest"])
# app.include_router(jobs_router,        prefix="/api", tags=["jobs"])
# app.include_router(legacy_router,      prefix="/api", tags=["legacy"])
# app.include_router(sales_router,       prefix="/api", tags=["sales"])
# app.include_router(search_router,      prefix="/api", tags=["search"])
# app.include_router(stock_router,       prefix="/api", tags=["stock"])
# app.include_router(shipments_router,    prefix="/api", tags=["shipments"])

app.include_router(harvestloads_router, prefix="/api", tags=["harvestloads"])
app.include_router(blends_router,       prefix="/api", tags=["blends"])
app.include_router(trans_sum_router,    prefix="/api", tags=["trans_sum"])
app.include_router(vintrace_pull_router, prefix="/api", tags=["vintrace"])
app.include_router(trans_sum_sync_router, prefix="/api", tags=["trans_sum"])
app.include_router(meta_router,          prefix="/api/meta", tags=["meta"])

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
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})