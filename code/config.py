from os.path import dirname, abspath

PROTOCOL = 'http://'
HOST = 'localhost'
PORT = dict(
    kernel=18985,
    web=8105,
)

OPTIONS = ()

ORG = 'q-ran'
REPO = 'quran'
CORPUS = 'Quran'
VERSION = '0.4'
RELATIVE = 'tf'

DOI_TEXT = '10.5281/zenodo.2532177'
DOI_URL = 'https://doi.org/10.5281/zenodo.2532177'

DOC_URL = f'https://github.com/{ORG}/{REPO}/blob/master/docs'
DOC_INTRO = 'features.md'
CHAR_URL = '{tfDoc}/Writing/Arabic'
CHAR_TEXT = 'Arabic characters and transcriptions',

FEATURE_URL = f'{DOC_URL}/features.md#{{feature}}'

MODULE_SPECS = ()

ZIP = [REPO]

CONDENSE_TYPE = 'aya'

NONE_VALUES = {None, 'NA', 'none', 'unknown'}

STANDARD_FEATURES = '''
    number name nameTrans nameAscii name@en type order
    ascii unicode space
    lemma root sp
    pos posx a ax f fx l lx w wx n
    case gn nu definite
    formation voice tense mood ps
    component interjection
'''.strip().split()

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {'lex'}

EXAMPLE_SECTION = (
    f'<code>1:1</code>'
)
EXAMPLE_SECTION_TEXT = '1:1'

SECTION_SEP1 = ':'
SECTION_SEP2 = None

DEFAULT_CLS = 'trb'
DEFAULT_CLS_ORIG = 'arb'
FORMAT_CSS = dict(
    orig=DEFAULT_CLS_ORIG,
    trans=DEFAULT_CLS,
)

CLASS_NAMES = dict(
    aya='aya',
    word='word',
    lex='lextp',
)

FONT_NAME = 'AmiriQuran'
FONT = 'AmiriQuran.ttf'
FONTW = 'AmiriQuran.woff2'

TEXT_FORMATS = {}

BROWSE_NAV_LEVEL = 1
BROWSE_CONTENT_PRETTY = False


def deliver():
    return (globals(), dirname(abspath(__file__)))
