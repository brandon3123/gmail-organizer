from aenum import Enum


class Filter(Enum):
    """
        Filters for message searching
    """
    FROM = 'from:'
    LABEL = 'label:'
