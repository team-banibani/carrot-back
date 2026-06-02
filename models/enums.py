import enum


class SunlightEnum(str, enum.Enum):
    """환경 유형의 햇빛 조건"""
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    NORMAL = "NORMAL"
    LOW_MEDIUM = "LOW_MEDIUM"
    LOW = "LOW"
    VERY_LOW = "VERY_LOW"

    @property
    def label(self) -> str:
        return {
            "VERY_HIGH": "매우 높음", "HIGH": "보통~높음", "MEDIUM": "중간",
            "NORMAL": "보통", "LOW_MEDIUM": "보통~낮음", "LOW": "낮음", "VERY_LOW": "매우 낮음",
        }[self.value]


class VentilationEnum(str, enum.Enum):
    """환경 유형의 통풍 조건"""
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
    LOW_MEDIUM = "LOW_MEDIUM"
    LOW = "LOW"
    VERY_LOW = "VERY_LOW"

    @property
    def label(self) -> str:
        return {
            "VERY_HIGH": "매우 높음", "HIGH": "높음", "NORMAL": "보통",
            "LOW_MEDIUM": "보통~낮음", "LOW": "낮음", "VERY_LOW": "매우 낮음",
        }[self.value]


class TemperatureEnum(str, enum.Enum):
    """환경 유형의 온도 조건"""
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    NORMAL = "NORMAL"
    LOW = "LOW"

    @property
    def label(self) -> str:
        return {"HIGH": "높음", "HIGH_MEDIUM": "보통~높음", "NORMAL": "보통", "LOW": "낮음"}[self.value]


class HumidityEnum(str, enum.Enum):
    """환경 유형의 습도 조건"""
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    NORMAL = "NORMAL"
    LOW_MEDIUM = "LOW_MEDIUM"
    LOW = "LOW"

    @property
    def label(self) -> str:
        return {
            "HIGH": "높음", "HIGH_MEDIUM": "보통~높음", "NORMAL": "보통",
            "LOW_MEDIUM": "보통~낮음", "LOW": "낮음",
        }[self.value]


class ManagementDifficultyEnum(str, enum.Enum):
    VERY_EASY = "VERY_EASY"
    EASY = "EASY"
    NORMAL = "NORMAL"
    HARD = "HARD"

    @property
    def label(self) -> str:
        return {"VERY_EASY": "매우 쉬움", "EASY": "쉬움", "NORMAL": "보통", "HARD": "어려움"}[self.value]


class SunlightRequirementsEnum(str, enum.Enum):
    """식물의 햇빛 요구량"""
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    MEDIUM = "MEDIUM"
    LOW_MEDIUM = "LOW_MEDIUM"
    LOW = "LOW"

    @property
    def label(self) -> str:
        return {
            "VERY_HIGH": "매우 높음", "HIGH": "높음", "HIGH_MEDIUM": "높음~중간",
            "MEDIUM": "중간", "LOW_MEDIUM": "낮음~중간", "LOW": "낮음",
        }[self.value]


class SizeEnum(str, enum.Enum):
    """플랜테 식물의 크기"""
    SMALL = "SMALL"
    SMALL_MEDIUM = "SMALL_MEDIUM"
    MEDIUM = "MEDIUM"
    MEDIUM_LARGE = "MEDIUM_LARGE"
    LARGE = "LARGE"

    @property
    def label(self) -> str:
        return {
            "SMALL": "소형", "SMALL_MEDIUM": "소형~중형", "MEDIUM": "중형",
            "MEDIUM_LARGE": "중형~대형", "LARGE": "대형",
        }[self.value]


class AirPurificationEnum(str, enum.Enum):
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL = "NORMAL"

    @property
    def label(self) -> str:
        return {"VERY_HIGH": "매우 높음", "HIGH": "높음", "NORMAL": "보통"}[self.value]


class PetStabilityEnum(str, enum.Enum):
    SAFE = "SAFE"
    CAUTION = "CAUTION"
    DANGER = "DANGER"

    @property
    def label(self) -> str:
        return {"SAFE": "안전", "CAUTION": "주의", "DANGER": "위험"}[self.value]


class LocationEnum(str, enum.Enum):
    SOUTH_WINDOW = "SOUTH_WINDOW"
    BALCONY = "BALCONY"
    LIVING_ROOM_WINDOW = "LIVING_ROOM_WINDOW"
    WINDOW = "WINDOW"
    LIVING_ROOM = "LIVING_ROOM"
    WINDOW_SILL = "WINDOW_SILL"
    SHELF = "SHELF"
    HANGING = "HANGING"
    DESK = "DESK"
    BEDROOM = "BEDROOM"
    HALLWAY = "HALLWAY"
    INDOOR_INNER = "INDOOR_INNER"
    OFFICE = "OFFICE"
    STUDY = "STUDY"
    BATHROOM = "BATHROOM"
    KITCHEN = "KITCHEN"
    WORK_DESK = "WORK_DESK"
    LOBBY = "LOBBY"
    VERANDA = "VERANDA"
    ENTRANCE = "ENTRANCE"

    @property
    def label(self) -> str:
        return {
            "SOUTH_WINDOW": "남향 창가", "BALCONY": "발코니", "LIVING_ROOM_WINDOW": "거실 창가",
            "WINDOW": "창가", "LIVING_ROOM": "거실", "WINDOW_SILL": "창턱",
            "SHELF": "선반", "HANGING": "행잉", "DESK": "책상", "BEDROOM": "침실",
            "HALLWAY": "복도", "INDOOR_INNER": "실내 안쪽", "OFFICE": "사무실",
            "STUDY": "서재", "BATHROOM": "욕실", "KITCHEN": "주방",
            "WORK_DESK": "데스크", "LOBBY": "로비", "VERANDA": "베란다", "ENTRANCE": "현관",
        }[self.value]


class CategoryEnum(str, enum.Enum):
    """키워드 매핑 카테고리"""
    SUNLIGHT = "SUNLIGHT"
    VENTILATION = "VENTILATION"
    TEMPERATURE = "TEMPERATURE"
    HUMIDITY = "HUMIDITY"

    @property
    def label(self) -> str:
        return {"SUNLIGHT": "햇빛", "VENTILATION": "통풍", "TEMPERATURE": "온도", "HUMIDITY": "습도"}[self.value]


class CategoryLevelEnum(str, enum.Enum):
    """유형별 추천 매트릭스 적합도"""
    OPTIMAL = "OPTIMAL"
    POSSIBLE = "POSSIBLE"

    @property
    def label(self) -> str:
        return {"OPTIMAL": "O", "POSSIBLE": "△"}[self.value]


class StyleEnum(str, enum.Enum):
    """공간 스타일"""
    MINIMAL = "MINIMAL"
    MODERN = "MODERN"
    NATURAL = "NATURAL"
    BOHO = "BOHO"
    WARM = "WARM"
    VINTAGE = "VINTAGE"

    @property
    def label(self) -> str:
        return {
            "MINIMAL": "미니멀", "MODERN": "모던", "NATURAL": "내추럴",
            "BOHO": "보헤미안", "WARM": "웜톤", "VINTAGE": "빈티지",
        }[self.value]
