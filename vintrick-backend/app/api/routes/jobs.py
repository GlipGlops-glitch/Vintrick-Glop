# vintrick-backend/app/routers/jobs.py

from fastapi import APIRouter, Body, Path
import swagger_client.swagger_client as swagger_client

router = APIRouter()

configuration = swagger_client.Configuration()
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))

@router.post("/workorders/assign")
def assign_a_work_order(body: swagger_client.AssignWorkData = Body(...)):
    return api_instance.assign_a_work_order(body=body)

@router.get("/workorders/jobs/{jobId}")
def get_job_details_by_id(jobId: str = Path(...)):
    return api_instance.get_job_details_by_id(jobId=jobId)

@router.get("/workorders/{id}")
def get_work_order_details_by_id_or_code(id: str = Path(...)):
    return api_instance.get_work_order_details_by_id_or_code(id=id)

@router.get("/workorders/list/")
def list_available_work_orders():
    return api_instance.list_available_work_orders()

@router.post("/workorders/jobs/submit")
def submit_job_details(body: swagger_client.SubmitJobRequest = Body(...)):
    return api_instance.submit_job_details(body=body)