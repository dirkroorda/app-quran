from os.path import dirname, abspath

API_VERSION = 1

PROTOCOL = "http://"
HOST = "localhost"
PORT = dict(kernel=18985, web=8105)

ORG = "q-ran"
REPO = "quran"
CORPUS = "Quran"
VERSION = "0.4"
RELATIVE = "tf"

DOI_TEXT = "10.5281/zenodo.2532177"
DOI_URL = "https://doi.org/10.5281/zenodo.2532177"

DOC_URL = f"https://github.com/{ORG}/{REPO}/blob/master/docs"
DOC_INTRO = "features.md"
CHAR_URL = "{tfDoc}/Writing/Arabic"
CHAR_TEXT = ("Arabic characters and transcriptions",)

FEATURE_URL = f"{DOC_URL}/features.md#{{feature}}"

MODULE_SPECS = ()

ZIP = [REPO]

BASE_TYPE = "word"
CONDENSE_TYPE = "aya"

NONE_VALUES = {None, "NA", "none", "unknown"}

STANDARD_FEATURES = """
    number name nameTrans nameAscii name@en type order
    ascii unicode space
    lemma root sp
    pos posx a ax f fx l lx w wx n
    case gn nu definite
    formation voice tense mood ps
    component interjection
""".strip().split()

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {"lex"}

EXAMPLE_SECTION = f"<code>1:1</code>"
EXAMPLE_SECTION_TEXT = "1:1"

SECTION_SEP1 = ":"
SECTION_SEP2 = None

WRITING = "ara"
WRITING_DIR = "rtl"

FONT_NAME = "AmiriQuran"
FONT = "AmiriQuran.ttf"
FONTW = "AmiriQuran.woff2"

TEXT_FORMATS = {}

BROWSE_NAV_LEVEL = 1
BROWSE_CONTENT_PRETTY = False

VERSE_TYPES = None

LEX = dict(typ="lex", feat="lemma", cls="lex", target="word")

TRANSFORM = None

CHILD_TYPE = dict(
    sura="aya",
    manzil="aya",
    sajda="aya",
    juz="aya",
    ruku="aya",
    hizb="aya",
    page="aya",
    aya="group",
    group="word",
)

SUPER_TYPE = None

TYPE_DISPLAY = dict(
    sura=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        level=3, flow="col", wrap=False, stretch=False,
    ),
    manzil=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        childrenPlain=False,
        level=3, flow="col", wrap=False, strectch=False,
    ),
    sajda=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        childrenPlain=False,
        level=3, flow="col", wrap=False, strectch=False,
    ),
    juz=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        childrenPlain=False,
        level=3, flow="col", wrap=False, strectch=False,
    ),
    ruku=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        childrenPlain=False,
        level=3, flow="col", wrap=False, strectch=False,
    ),
    hizb=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        childrenPlain=False,
        level=3, flow="col", wrap=False, strectch=False,
    ),
    page=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        childrenPlain=False,
        level=3, flow="col", wrap=False, strectch=False,
    ),
    aya=dict(
        template="{otype} {number}",
        bareFeatures="",
        features="",
        level=2, flow="col", wrap=False, strectch=False,
    ),
    lex=dict(
        template=True,
        bareFeatures="",
        features="",
        level=1, flow="col", wrap=False, strectch=False,
    ),
    word=dict(
        template=True,
        bareFeatures="pos posx",
        features="lemma root formation tense",
        level=0, flow="col", wrap=False, strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
