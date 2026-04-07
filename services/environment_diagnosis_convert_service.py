from models.enums import TemperatureEnum, HumidityEnum


class EnvironmentDiagnosisConvertService:
    """환경 진단 입력값 변환 로직"""

    def convert_temperature(self, temp: float) -> TemperatureEnum:
        """온도 값을 TemperatureEnum으로 변환"""
        if temp >= 25:
            return TemperatureEnum.HIGH
        if temp >= 20:
            return TemperatureEnum.HIGH_MEDIUM
        if temp >= 15:
            return TemperatureEnum.NORMAL
        return TemperatureEnum.LOW

    def parse_humidity(self, humidity_str: str) -> float:
        """습도 문자열 파싱 (예: "60%")"""
        try:
            return float(humidity_str.replace("%", "").strip())
        except ValueError as exc:
            raise ValueError(f"습도 형식이 올바르지 않습니다: {humidity_str}") from exc

    def convert_humidity(self, humidity_value: float) -> HumidityEnum:
        """습도 값을 HumidityEnum으로 변환"""
        if humidity_value >= 60:
            return HumidityEnum.HIGH
        if humidity_value >= 50:
            return HumidityEnum.HIGH_MEDIUM
        if humidity_value >= 40:
            return HumidityEnum.NORMAL
        if humidity_value >= 30:
            return HumidityEnum.LOW_MEDIUM
        return HumidityEnum.LOW

