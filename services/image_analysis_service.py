import base64
import json
import re

from openai import OpenAI

from core.config import settings
from models.enums import LocationEnum, SizeEnum, SunlightEnum, StyleEnum


class ImageAnalysisService:
    """사진 분석 비즈니스 로직"""

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def analyze_image(self, file_content: bytes, media_type: str) -> dict:
        """OpenAI Vision API를 사용하여 이미지 분석"""
        base64_image = base64.b64encode(file_content).decode("utf-8")

        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": self._get_analysis_prompt()},
                        {
                            "type": "input_image",
                            "image_url": f"data:{media_type};base64,{base64_image}",
                        },
                    ],
                }
            ],
            max_output_tokens=500,
        )

        response_text = self._extract_text(response)
        normalized_text = self._strip_json_fence(response_text)
        return json.loads(normalized_text)

    def _get_analysis_prompt(self) -> str:
        return (
            "플렌테리어 전문가처럼 실내 공간을 분석하세요. "
            "아래 형식의 JSON 객체만 반환하세요. 설명/마크다운/코드블록은 금지합니다.\n"
            "{\n"
            '  "style": "MINIMAL|MODERN|NATURAL|BOHO|WARM|VINTAGE",\n'
            '  "sunlight": "매우 높음|보통~높음|중간|보통|보통~낮음|낮음|매우 낮음",\n'
            '  "size": "소형|소형~중형|중형|중형~대형|대형",\n'
            '  "place": "거실|침실|서재|주방|욕실|복도|현관|베란다|발코니|로비|선반|책상|행잉|사무실|실내 안쪽"\n'
            "}"
        )

    def _extract_text(self, response) -> str:
        # SDK에서 제공되는 output_text를 우선 사용
        output_text = getattr(response, "output_text", None)
        if output_text:
            return output_text.strip()

        # fallback: output 배열에서 텍스트 조각 수집
        chunks: list[str] = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                text = getattr(content, "text", None)
                if text:
                    chunks.append(text)

        if not chunks:
            raise ValueError("OpenAI 응답에서 텍스트를 추출하지 못했습니다")
        return "\n".join(chunks).strip()

    def _strip_json_fence(self, text: str) -> str:
        match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
        return match.group(1).strip() if match else text.strip()

    def validate_response(self, data: dict) -> dict:
        """응답 데이터 유효성 검증"""
        try:
            style_enum = StyleEnum(data["style"])
            sunlight_enum = SunlightEnum(data["sunlight"])
            size_enum = SizeEnum(data["size"])
            place_enum = LocationEnum(data["place"])

            return {
                "style": style_enum,
                "sunlight": sunlight_enum,
                "size": size_enum,
                "place": place_enum,
            }
        except KeyError as e:
            raise ValueError(f"필수 필드 누락: {str(e)}")
        except ValueError as e:
            raise ValueError(f"유효하지 않은 분석 결과: {str(e)}")
