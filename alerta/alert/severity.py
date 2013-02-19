""" Possible alert severity codes.

See ITU-T perceived severity model M.3100 and CCITT Rec X.736
http://www.itu.int/rec/T-REC-M.3100
http://www.itu.int/rec/T-REC-X.736-199201-I
"""

CRITICAL_SEV_CODE = 1
MAJOR_SEV_CODE = 2
MINOR_SEV_CODE = 3
WARNING_SEV_CODE = 4
NORMAL_SEV_CODE = 5
CLEAR_SEV_CODE = 5
INFORM_SEV_CODE = 6
DEBUG_SEV_CODE = 7
AUTH_SEV_CODE = 8
UNKNOWN_SEV_CODE = 9
INDETER_SEV_CODE = 9

CRITICAL = 'Critical'
MAJOR = 'Major'
MINOR = 'Minor'
WARNING = 'Warning'
NORMAL = 'Normal'
CLEAR = 'Clear'
INFORM = 'Informational'
DEBUG = 'Debug'
AUTH = 'Security'
UNKNOWN = 'Unknown'
INDETERMINATE = 'Indeterminate'

ALL = [CRITICAL, MAJOR, MINOR, WARNING, NORMAL, CLEAR, INFORM, DEBUG, AUTH, UNKNOWN, INDETERMINATE]

_NAME_TO_CODE = {
    CRITICAL: CRITICAL_SEV_CODE,
    MAJOR: MAJOR_SEV_CODE,
    MINOR: MINOR_SEV_CODE,
    WARNING: WARNING_SEV_CODE,
    NORMAL: NORMAL_SEV_CODE,
    CLEAR: CLEAR_SEV_CODE,
    INFORM: INFORM_SEV_CODE,
    DEBUG: DEBUG_SEV_CODE,
    AUTH: AUTH_SEV_CODE,
    UNKNOWN: UNKNOWN_SEV_CODE,
    INDETERMINATE: INDETER_SEV_CODE,
}


def name_to_code(name):
    return _NAME_TO_CODE.get(name, UNKNOWN_CODE)
