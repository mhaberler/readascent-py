
FAKE_TIME_STEPS = 30  # assume 30sec update interval
MAX_FLIGHT_DURATION = 3600 * 5  # rather unlikely

# see examples/polyfit.py
# y = 6.31426 * x + -0.00019 * x^2 + -373.12281
ASCENT_RATE = 6.3  # m/s = ca 380m/min

BROTLI_SUMMARY_QUALITY = 11  # 7

# drop ascents older than MAX_ASCENT_AGE_IN_SUMMARY from summary
# the files are kept nevertheless
MAX_DAYS_IN_SUMMARY = 14

# after 3 days move to processed
KEEP_MADIS_PROCESSED_FILES = 86400 * 3

# added to featurecollection.properties.fmt and summary.fmt
FORMAT_VERSION = 5

WWW_DIR = "/var/www/radiosonde.mah.priv.at/"
DATA_DIR = "data/"
STATIC_DIR = "static/"
STATION_TXT = "station_list.txt"
SUMMARY = "summary.geojson.br"

PROCESSED = r"processed"
FAILED = r"failed"
INCOMING = r"incoming"
TS_PROCESSED = ".processed"
TS_FAILED = ".failed"
TS_TIMESTAMP = ".timestamp"
LOCKFILE = "/var/lock/process-radiosonde.pid"
STATION_LIST = WWW_DIR + STATIC_DIR + "station_list.json"
MADIS_DATA = WWW_DIR + DATA_DIR + "madis/"
GISC_DATA = WWW_DIR + DATA_DIR + "gisc/"
CHARSET = "utf-8"
tmpdir = "/tmp"
INDENT = 4
MESSAGE_START_SIGNATURE = b'BUFR'

# added to featurecollection.properties.fmt = FORMAT_VERSION
# 4 - using deep subdirs year/month under station
FORMAT_VERSION = 6


# set in process.py, read-only
known_stations = {}

# for FM-35 files which do not have track info
# not very reliable, so move to client
GENERATE_PATHS = False

# tag samples with the section source of an FM35 report:
# mandatory, sig temp, sig wind, max wind
# aids in debugging strange values
# "mandatory", "sig_temp", "sig_wind", "max_wind"
TAG_FM35 = True


# minimum vertical distance of samples to be repored
# hires BUFR files have a lot of samples
HSTEP = 100

SPOOLDIR = r"/var/spool/"
SPOOLDIR_NOAA_MADIS = SPOOLDIR + f"madis/"
SPOOLDIR_GISC_OFFENBACH = SPOOLDIR + r"gisc-offenbach/"
SPOOLDIR_GISC_TOKYO = SPOOLDIR + r"gisc-tokyo/"
SPOOLDIR_GISC_MOSCOW = SPOOLDIR + r"gisc-moscow/"

channels = {
    "gisc-offenbach": {
        "name":  "GISC Offenbach",
        "spooldir": SPOOLDIR_GISC_OFFENBACH,
        "pattern":  "*.zip",
        "housekeeping": "standard",
    },
    "gisc-moscow": {
        "name":  "GISC Moscow",
        "spooldir": SPOOLDIR_GISC_MOSCOW,
        "housekeeping": "standard",
        "pattern":  "*.bufr",
    },
    "gisc-tokyo": {
        "name":  "GISC Tokyo",
        "spooldir": SPOOLDIR_GISC_TOKYO,
        "housekeeping": "standard",
        "pattern":  "*.bufr",
    },
    "noaa-madis": {
        "name":  "NOAA MADIS",
        "spooldir": SPOOLDIR_NOAA_MADIS,
        "housekeeping": "delayed",
        "pattern":  "*.gz",
    },
}
