from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from api import user_login,customer_request, order, quotation,sample,parameter,department,employee,order_parameter
from database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_login.router, prefix="/auth", tags=["Customer"])
app.include_router(customer_request.router, prefix="/customer_request", tags=["Customer"])
app.include_router(order.router, prefix="/order", tags=["Order"])
app.include_router(order_parameter.router, prefix="/order_parameters",tags=["Order Parameters"])
app.include_router(quotation.router, prefix="/quotations", tags=["Quotations"])
app.include_router(sample.router, prefix="/samples", tags=["Samples"])
app.include_router(parameter.router, prefix="/parameter", tags=["Parameter"])
app.include_router(department.router, prefix="/department", tags=["department"])
app.include_router(employee.router, prefix="/employee", tags=["employee"])
app.mount("/static", StaticFiles(directory="static"), name="static")

