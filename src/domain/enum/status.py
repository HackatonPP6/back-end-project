from enum import Enum
class Status(Enum):
    DEGRADATION = "degradation",
    RESOLVED = "resolved",
    INFORMATIONAL = "informational"