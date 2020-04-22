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

STANDARD_FEATURES = """
    number name nameTrans nameAscii name@en type order
    ascii unicode space
    lemma root sp
    pos posx a ax f fx l lx w wx n
    case gn nu definite
    formation voice tense mood ps
    component interjection
""".strip().split()

EXAMPLE_SECTION = f"<code>1:1</code>"
EXAMPLE_SECTION_TEXT = "1:1"

DATA_DISPLAY = dict(
    noneValues={None, "NA", "none", "unknown"},
    sectionSep1=":",
    sectionSep2=None,
    writing="ara",
    writingDir="rtl",
    fontName="AmiriQuran",
    font="AmiriQuran.ttf",
    fontw="AmiriQuran.woff2",
    textFormats={},
    browseNavLevel=1,
    browseContentPretty=False,
)

TYPE_DISPLAY = dict(
    sura=dict(
        template="{otype} {number}",
        children="aya",
        level=3, flow="col", wrap=False, stretch=False,
    ),
    manzil=dict(
        template="{otype} {number}",
        childrenPlain=False,
        children="aya",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    sajda=dict(
        template="{otype} {number}",
        childrenPlain=False,
        children="aya",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    juz=dict(
        template="{otype} {number}",
        childrenPlain=False,
        children="aya",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    ruku=dict(
        template="{otype} {number}",
        childrenPlain=False,
        children="aya",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    hizb=dict(
        template="{otype} {number}",
        childrenPlain=False,
        children="aya",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    page=dict(
        template="{otype} {number}",
        childrenPlain=False,
        children="aya",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    aya=dict(
        template="{otype} {number}",
        children="group",
        condense=True,
        level=2, flow="col", wrap=False, strectch=False,
    ),
    lex=dict(
        template="{lemma}",
        lexTarget="word",
        level=1, flow="col", wrap=False, strectch=False,
    ),
    group=dict(
        template="",
        children="word",
        level=1, flow="row", wrap=True, strectch=False,
    ),
    word=dict(
        template=True,
        featuresBare="pos posx",
        features="lemma root formation tense",
        base=True,
        level=0, flow="col", wrap=False, strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
