from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.environment_diagnosis import EnvironmentDiagnosisRequest, EnvironmentDiagnosisResponse
from services.environment_diagnosis_convert_service import EnvironmentDiagnosisConvertService
from services.environment_diagnosis_service import EnvironmentDiagnosisService
from db.session import get_db

router = APIRouter()
convert_service = EnvironmentDiagnosisConvertService()
diagnosis_service = EnvironmentDiagnosisService()


@router.post("/diagnose", response_model=EnvironmentDiagnosisResponse)
async def diagnose_environment(
    request: EnvironmentDiagnosisRequest,
    session: AsyncSession = Depends(get_db)
) -> EnvironmentDiagnosisResponse:
    """
    사용자가 선택한 조건에 따른 플렌테리어 유형 진단

    - **sunlight**: 햇빛 조건 (SunlightEnum)
    - **temperature**: 온도 (숫자, 예: 24.6)
    - **humidity**: 습도 (예: 60%)
    """
    try:
        # API 레이어는 입력값을 Enum으로 변환해서 서비스에 전달
        humidity_value = convert_service.parse_humidity(request.humidity)
        temperature_enum = convert_service.convert_temperature(request.temperature)
        humidity_enum = convert_service.convert_humidity(humidity_value)

        environment_id = await diagnosis_service.diagnose_environment_id(
            session=session,
            sunlight=request.sunlight,
            temperature=temperature_enum,
            humidity=humidity_enum,
        )

        return EnvironmentDiagnosisResponse(environment_id=environment_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"환경 진단 오류: {str(e)}")
