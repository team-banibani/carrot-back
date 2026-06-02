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


class VentilationEnum(str, enum.Enum):
    """환경 유형의 통풍 조건"""
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
    LOW_MEDIUM = "LOW_MEDIUM"
    LOW = "LOW"
    VERY_LOW = "VERY_LOW"


class TemperatureEnum(str, enum.Enum):
    """환경 유형의 온도 조건"""
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    NORMAL = "NORMAL"
    LOW = "LOW"


class HumidityEnum(str, enum.Enum):
    """환경 유형의 습도 조건"""
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    NORMAL = "NORMAL"
    LOW_MEDIUM = "LOW_MEDIUM"
    LOW = "LOW"


class ManagementDifficultyEnum(str, enum.Enum):
    VERY_EASY = "VERY_EASY"
    EASY = "EASY"
    NORMAL = "NORMAL"
    HARD = "HARD"


class SunlightRequirementsEnum(str, enum.Enum):
    """식물의 햇빛 요구량"""
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    MEDIUM = "MEDIUM"
    LOW_MEDIUM = "LOW_MEDIUM"
    LOW = "LOW"


class SizeEnum(str, enum.Enum):
    """플랜테 식물의 크기"""
    SMALL = "SMALL"
    SMALL_MEDIUM = "SMALL_MEDIUM"
    MEDIUM = "MEDIUM"
    MEDIUM_LARGE = "MEDIUM_LARGE"
    LARGE = "LARGE"


class AirPurificationEnum(str, enum.Enum):
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL = "NORMAL"


class PetStabilityEnum(str, enum.Enum):
    SAFE = "SAFE"
    CAUTION = "CAUTION"
    DANGER = "DANGER"


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


class CategoryEnum(str, enum.Enum):
    """키워드 매핑 카테고리"""
    SUNLIGHT = "SUNLIGHT"
    VENTILATION = "VENTILATION"
    TEMPERATURE = "TEMPERATURE"
    HUMIDITY = "HUMIDITY"


class CategoryLevelEnum(str, enum.Enum):
    """유형별 추천 매트릭스 적합도"""
    OPTIMAL = "OPTIMAL"
    POSSIBLE = "POSSIBLE"


class StyleEnum(str, enum.Enum):
    """공간 스타일"""
    MINIMAL = "MINIMAL"
    MODERN = "MODERN"
    NATURAL = "NATURAL"
    BOHO = "BOHO"
    WARM = "WARM"
    VINTAGE = "VINTAGE"
