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
    noneValues={None, "NA", "none", "unknown"}, sectionSep1=":", writing="ara",
)

TYPE_DISPLAY = dict(
    manzil=dict(template="{otype} {number}", childrenPlain=False, children="aya",),
    sajda=dict(template="{otype} {number}", childrenPlain=False, children="aya",),
    juz=dict(template="{otype} {number}", childrenPlain=False, children="aya",),
    ruku=dict(children="aya",),
    hizb=dict(template="{otype} {number}", childrenPlain=False, children="aya",),
    page=dict(template="{otype} {number}", childrenPlain=False, children="aya",),
    lex=dict(template="{lemma}", lexTarget="word",),
    group=dict(wrap=False,),
    word=dict(featuresBare="pos posx", features="lemma root formation tense",),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
