from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from ..database import get_db
from ..models.railway_forms import WheelSpecification, BogieChecksheet
from ..schemas.railway_forms import (
    WheelSpecificationCreate,
    WheelSpecificationResponse,
    WheelSpecificationListResponse,
    BogieChecksheetCreate,
    BogieChecksheetResponse
)

router = APIRouter(prefix="/api/forms", tags=["KPA Form Data"])


@router.post("/wheel-specifications", 
    response_model=WheelSpecificationResponse, 
    status_code=201,
    summary="Submit Wheel Specification",
    description="Submit a new wheel specification form with detailed technical measurements and specifications for railway maintenance",
    response_description="Wheel specification form submitted successfully"
)
async def submit_wheel_specification(
    wheel_data: WheelSpecificationCreate,
    db: AsyncSession = Depends(get_db)
):

    existing_form = await db.execute(
        select(WheelSpecification).where(WheelSpecification.form_number == wheel_data.formNumber)
    )
    if existing_form.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Form number already exists"
        )
    

    wheel_spec = WheelSpecification(
        form_number=wheel_data.formNumber,
        submitted_by=wheel_data.submittedBy,
        submitted_date=wheel_data.submittedDate,
        fields=wheel_data.fields.dict()
    )
    
    db.add(wheel_spec)
    await db.commit()
    await db.refresh(wheel_spec)
    
    return WheelSpecificationResponse(
        success=True,
        message="Wheel specification submitted successfully.",
        data={
            "formNumber": wheel_spec.form_number,
            "submittedBy": wheel_spec.submitted_by,
            "submittedDate": wheel_spec.submitted_date,
            "status": wheel_spec.status
        }
    )


@router.get("/wheel-specifications", 
    response_model=WheelSpecificationListResponse,
    summary="Get Wheel Specifications",
    description="Retrieve wheel specification forms with optional filtering capabilities for railway maintenance records",
    response_description="List of wheel specification forms matching the criteria"
)
async def get_wheel_specifications(
    formNumber: Optional[str] = Query(None, description="Filter by specific form number (e.g., WHEEL-2025-001)"),
    submittedBy: Optional[str] = Query(None, description="Filter by user who submitted the form"),
    submittedDate: Optional[str] = Query(None, description="Filter by submission date (YYYY-MM-DD format)"),
    db: AsyncSession = Depends(get_db)
):
    
    query = select(WheelSpecification)
    
    if formNumber:
        query = query.where(WheelSpecification.form_number == formNumber)
    if submittedBy:
        query = query.where(WheelSpecification.submitted_by == submittedBy)
    if submittedDate:
        query = query.where(WheelSpecification.submitted_date == submittedDate)
    
    result = await db.execute(query)
    wheel_specs = result.scalars().all()
    
    data = []
    for spec in wheel_specs:
        data.append({
            "formNumber": spec.form_number,
            "submittedBy": spec.submitted_by,
            "submittedDate": spec.submitted_date,
            "fields": spec.fields
        })
    
    return WheelSpecificationListResponse(
        success=True,
        message="Filtered wheel specification forms fetched successfully.",
        data=data
    )


@router.post("/bogie-checksheet", 
    response_model=BogieChecksheetResponse, 
    status_code=201,
    summary="Submit Bogie Checksheet",
    description="Submit a new bogie checksheet form with inspection details and condition assessments for railway maintenance",
    response_description="Bogie checksheet form submitted successfully"
)
async def submit_bogie_checksheet(
    bogie_data: BogieChecksheetCreate,
    db: AsyncSession = Depends(get_db)
):
   
    existing_form = await db.execute(
        select(BogieChecksheet).where(BogieChecksheet.form_number == bogie_data.formNumber)
    )
    if existing_form.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Form number already exists"
        )
    

    bogie_check = BogieChecksheet(
        form_number=bogie_data.formNumber,
        inspection_by=bogie_data.inspectionBy,
        inspection_date=bogie_data.inspectionDate,
        bogie_details=bogie_data.bogieDetails.dict(),
        bogie_checksheet=bogie_data.bogieChecksheet.dict(),
        bmbc_checksheet=bogie_data.bmbcChecksheet.dict()
    )
    
    db.add(bogie_check)
    await db.commit()
    await db.refresh(bogie_check)
    
    return BogieChecksheetResponse(
        success=True,
        message="Bogie checksheet submitted successfully.",
        data={
            "formNumber": bogie_check.form_number,
            "inspectionBy": bogie_check.inspection_by,
            "inspectionDate": bogie_check.inspection_date,
            "status": bogie_check.status
        }
    ) 