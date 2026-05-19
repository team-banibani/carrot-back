from fastapi import APIRouter, UploadFile, File, HTTPException

from schemas.image_analysis import ImageAnalysisResponse
from services.image_analysis_service import ImageAnalysisService

router = APIRouter()
service = ImageAnalysisService()


@router.post("/analyze-image", response_model=ImageAnalysisResponse)
async def analyze_image(file: UploadFile = File(...)) -> ImageAnalysisResponse:
    """
    사진 분석을 통해 스타일, 햇빛, 크기, 장소 정보를 추출합니다.
    
    - **file**: 이미지 파일 (JPEG, PNG, WEBP, GIF)
    
    Returns:
    - **style**: 공간 스타일
    - **sunlight**: 햇빛 조건
    - **size**: 공간 크기
    - **place**: 공간 장소
    """
    
    # 이미지 형식 검증
    supported_types = {"image/jpeg", "image/png", "image/webp"}
    if file.content_type not in supported_types:
        raise HTTPException(status_code=400, detail="지원하지 않는 이미지 형식입니다.")
    
    try:
        # 파일 읽기
        file_content = await file.read()
        
        # 서비스에서 분석 처리
        analysis_data = service.analyze_image(file_content, file.content_type)
        
        # 응답 데이터 검증
        validated_data = service.validate_response(analysis_data)
        
        return ImageAnalysisResponse(**validated_data)
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API 호출 오류: {str(e)}")



