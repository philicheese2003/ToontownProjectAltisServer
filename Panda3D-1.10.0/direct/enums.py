from enum import IntEnum

class ComponentStatus(IntEnum):
    "STATUS"
    operational = 1
    performanceIssues = 2
    partialOutage = 3
    majorOutage = 4