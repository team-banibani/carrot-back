import enum


class SunlightEnum(str, enum.Enum):
    """환경 유형의 햇빛 조건"""
    VERY_HIGH = "매우 높음"   # ENV-01 직사광선 4시간+
    HIGH = "보통~높음"        # ENV-04, ENV-08
    MEDIUM = "중간"           # ENV-03 간접광
    NORMAL = "보통"           # ENV-05, ENV-06
    LOW_MEDIUM = "보통~낮음"  # ENV-07
    LOW = "낮음"              # ENV-09
    VERY_LOW = "매우 낮음"    # ENV-02


class VentilationEnum(str, enum.Enum):
    """환경 유형의 통풍 조건"""
    VERY_HIGH = "매우 높음"   # ENV-08 자연 환기 양호
    HIGH = "높음"             # ENV-06
    NORMAL = "보통"           # ENV-01~03, ENV-05
    LOW_MEDIUM = "보통~낮음"  # ENV-04
    LOW = "낮음"              # ENV-07
    VERY_LOW = "매우 낮음"    # ENV-09 환기 어려움


class TemperatureEnum(str, enum.Enum):
    """환경 유형의 온도 조건"""
    HIGH = "높음"             # ENV-04 25°C+
    HIGH_MEDIUM = "보통~높음" # ENV-01, ENV-09
    NORMAL = "보통"           # ENV-02, ENV-03, ENV-06, ENV-07, ENV-08
    LOW = "낮음"              # ENV-05 15°C-


class HumidityEnum(str, enum.Enum):
    """환경 유형의 습도 조건"""
    HIGH = "높음"             # ENV-07 60%+
    HIGH_MEDIUM = "보통~높음" # ENV-09
    NORMAL = "보통"           # ENV-01, ENV-02, ENV-03, ENV-05, ENV-08
    LOW_MEDIUM = "보통~낮음"  # ENV-04
    LOW = "낮음"              # ENV-06 40%-


class ManagementDifficultyEnum(str, enum.Enum):
    VERY_EASY = "매우 쉬움"
    EASY = "쉬움"
    NORMAL = "보통"
    HARD = "어려움"


class SunlightRequirementsEnum(str, enum.Enum):
    """식물의 햇빛 요구량"""
    VERY_HIGH = "매우 높음"   # 선인장
    HIGH = "높음"             # 스투키, 고무나무 등
    HIGH_MEDIUM = "높음~중간" # 금전수
    MEDIUM = "중간"           # 스파티필름, 보스턴 고사리 등
    LOW_MEDIUM = "낮음~중간"  # 산세베리아, 필로덴드론 등
    LOW = "낮음"              # 스킨답서스, 아글라오네마 등


class SizeEnum(str, enum.Enum):
    SMALL = "소형"
    SMALL_MEDIUM = "소형~중형"
    MEDIUM = "중형"
    MEDIUM_LARGE = "중형~대형"
    LARGE = "대형"


class AirPurificationEnum(str, enum.Enum):
    VERY_HIGH = "매우 높음"
    HIGH = "높음"
    NORMAL = "보통"


class PetStabilityEnum(str, enum.Enum):
    SAFE = "안전"
    CAUTION = "주의"
    DANGER = "위험"


class LocationEnum(str, enum.Enum):
    SOUTH_WINDOW = "남향 창가"
    BALCONY = "발코니"
    LIVING_ROOM_WINDOW = "거실 창가"
    WINDOW = "창가"
    LIVING_ROOM = "거실"
    WINDOW_SILL = "창턱"
    SHELF = "선반"
    HANGING = "행잉"
    DESK = "책상"
    BEDROOM = "침실"
    HALLWAY = "복도"
    INDOOR_INNER = "실내 안쪽"
    OFFICE = "사무실"
    STUDY = "서재"
    BATHROOM = "욕실"
    KITCHEN = "주방"
    WORK_DESK = "데스크"
    LOBBY = "로비"
    VERANDA = "베란다"
    ENTRANCE = "현관"


class CategoryEnum(str, enum.Enum):
    """키워드 매핑 카테고리"""
    SUNLIGHT = "햇빛"
    VENTILATION = "통풍"
    TEMPERATURE = "온도"
    HUMIDITY = "습도"


class CategoryLevelEnum(str, enum.Enum):
    """유형별 추천 매트릭스 적합도"""
    OPTIMAL = "O"    # 최적
    POSSIBLE = "△"   # 가능
