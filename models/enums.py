import enum


class SunlightEnum(str, enum.Enum):
    FULL_SUN = "FULL_SUN"
    PARTIAL_SUN = "PARTIAL_SUN"
    SHADE = "SHADE"


class VentilationEnum(str, enum.Enum):
    GOOD = "GOOD"
    MODERATE = "MODERATE"
    POOR = "POOR"


class TemperatureEnum(str, enum.Enum):
    WARM = "WARM"
    MODERATE = "MODERATE"
    COOL = "COOL"


class HumidityEnum(str, enum.Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class ManagementDifficultyEnum(str, enum.Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class WateringEnum(str, enum.Enum):
    FREQUENT = "FREQUENT"
    MODERATE = "MODERATE"
    INFREQUENT = "INFREQUENT"


class SizeEnum(str, enum.Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"


class AirPurificationEnum(str, enum.Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class PetStabilityEnum(str, enum.Enum):
    SAFE = "SAFE"
    TOXIC = "TOXIC"


class LocationEnum(str, enum.Enum):
    LIVING_ROOM = "LIVING_ROOM"
    BEDROOM = "BEDROOM"
    BATHROOM = "BATHROOM"
    KITCHEN = "KITCHEN"
    OFFICE = "OFFICE"
    BALCONY = "BALCONY"
    OUTDOOR = "OUTDOOR"


class FitEnum(str, enum.Enum):
    OPTIMAL = "optimal"
    POSSIBLE = "possible"
