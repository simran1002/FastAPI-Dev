from pydantic import BaseModel
from typing import Dict, Any, Optional, List
from datetime import datetime



class WheelSpecificationFields(BaseModel):
    
    treadDiameterNew: str = "915 (900-1000)"
    lastShopIssueSize: str = "837 (800-900)"
    condemningDia: str = "825 (800-900)"
    wheelGauge: str = "1600 (+2,-1)"
    variationSameAxle: str = "0.5"
    variationSameBogie: str = "5"
    variationSameCoach: str = "13"
    wheelProfile: str = "29.4 Flange Thickness"
    intermediateWWP: str = "20 TO 28"
    bearingSeatDiameter: str = "130.043 TO 130.068"
    rollerBearingOuterDia: str = "280 (+0.0/-0.035)"
    rollerBearingBoreDia: str = "130 (+0.0/-0.025)"
    rollerBearingWidth: str = "93 (+0/-0.250)"
    axleBoxHousingBoreDia: str = "280 (+0.030/+0.052)"
    wheelDiscWidth: str = "127 (+4/-0)"

    class Config:
        schema_extra = {
            "example": {
                "treadDiameterNew": "915 (900-1000)",
                "lastShopIssueSize": "837 (800-900)",
                "condemningDia": "825 (800-900)",
                "wheelGauge": "1600 (+2,-1)",
                "variationSameAxle": "0.5",
                "variationSameBogie": "5",
                "variationSameCoach": "13",
                "wheelProfile": "29.4 Flange Thickness",
                "intermediateWWP": "20 TO 28",
                "bearingSeatDiameter": "130.043 TO 130.068",
                "rollerBearingOuterDia": "280 (+0.0/-0.035)",
                "rollerBearingBoreDia": "130 (+0.0/-0.025)",
                "rollerBearingWidth": "93 (+0/-0.250)",
                "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
                "wheelDiscWidth": "127 (+4/-0)"
            }
        }


class WheelSpecificationCreate(BaseModel):
    """
    Request model for creating a new wheel specification form.
    """
    formNumber: str = "WHEEL-2025-001"
    submittedBy: str = "user_id_123"
    submittedDate: str = "2025-07-13"
    fields: WheelSpecificationFields

    class Config:
        schema_extra = {
            "example": {
                "formNumber": "WHEEL-2025-001",
                "submittedBy": "user_id_123",
                "submittedDate": "2025-07-13",
                "fields": {
                    "treadDiameterNew": "915 (900-1000)",
                    "lastShopIssueSize": "837 (800-900)",
                    "condemningDia": "825 (800-900)",
                    "wheelGauge": "1600 (+2,-1)",
                    "variationSameAxle": "0.5",
                    "variationSameBogie": "5",
                    "variationSameCoach": "13",
                    "wheelProfile": "29.4 Flange Thickness",
                    "intermediateWWP": "20 TO 28",
                    "bearingSeatDiameter": "130.043 TO 130.068",
                    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
                    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
                    "rollerBearingWidth": "93 (+0/-0.250)",
                    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
                    "wheelDiscWidth": "127 (+4/-0)"
                }
            }
        }


class WheelSpecificationResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, Any]


class WheelSpecificationListResponse(BaseModel):
    success: bool
    message: str
    data: List[Dict[str, Any]]



class BogieDetails(BaseModel):
    bogieNo: str
    makerYearBuilt: str
    incomingDivAndDate: str
    deficitComponents: str
    dateOfIOH: str


class BogieChecksheetData(BaseModel):
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str
    axleGuide: str


class BmbcChecksheetData(BaseModel):
    cylinderBody: str
    pistonTrunnion: str
    adjustingTube: str
    plungerSpring: str


class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheetData
    bmbcChecksheet: BmbcChecksheetData


class BogieChecksheetResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, Any] 