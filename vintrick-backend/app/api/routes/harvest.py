# vintrick-backend/app/routers/harvest.py

from fastapi import APIRouter, Body, Query
import swagger_client.swagger_client as swagger_client

router = APIRouter()

configuration = swagger_client.Configuration()
api_instance = swagger_client.HarvestApi(swagger_client.ApiClient(configuration))

@router.post("/block-assessments/create")
def create_a_block_assessment(body: swagger_client.FullBlockAssessmentRequest = Body(...)):
    return api_instance.create_a_block_assessment(body=body)

@router.get("/intake-operations/search")
def fruit_intake_operation_search(
    firstResult: int = Query(0),
    maxResult: int = Query(20)
):
    return api_instance.fruit_intake_operation_search(firstResult=firstResult, maxResult=maxResult)

@router.get("/sample-operations/search")
def maturity_samples_search(
    firstResult: int = Query(0),
    maxResult: int = Query(20)
):
    return api_instance.maturity_samples_search(firstResult=firstResult, maxResult=maxResult)