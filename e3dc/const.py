from enum import Enum


class Const:
    def __init__(self):
        pass

    REMOTE_ADDRESS = 'https://s10.e3dc.com/s10/phpcmd/cmd.php'  # type: str
    REQUEST_INTERVAL_SEC = 10  # type: int

    class Info(Enum):
        TIME = 'INFO_REQ_UTC_TIME'  # type: str
        STATE = 'EMS_REQ_BAT_SOC'  # type: str

    class Consumption(Enum):
        BATTERY = 'EMS_REQ_POWER_BAT'  # type: str
        HOUSE = 'EMS_REQ_POWER_HOME'  # type: str
        WALLBOX = 'EMS_REQ_POWER_WB_ALL'  # type: str

    class Production(Enum):
        PV = 'EMS_REQ_POWER_PV'  # type: str
        GRID = 'EMS_REQ_POWER_GRID'  # type: str
