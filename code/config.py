from os.path import dirname, abspath

API_VERSION = 1

PROVENANCE_SPEC = dict(
    org="q-ran",
    repo="quran",
    version="0.4",
    doi="10.5281/zenodo.2532177",
    corpus="Quran",
    webBase="http://tanzil.net",
    webUrl="/#<1>:<2>",
    webHint="show this passage on Tanzil",
)

DOCS = dict(docPage="features", featureBase="{docBase}/features{docExt}")

DATA_DISPLAY = dict(
    noneValues={None, "NA", "none", "unknown"}, sectionSep1=":", writing="ara",
)

TYPE_DISPLAY = dict(
    manzil=dict(template="{otype} {number}", childrenPlain=False, children="aya"),
    sajda=dict(template="{otype} {number}", childrenPlain=False, children="aya"),
    juz=dict(template="{otype} {number}", childrenPlain=False, children="aya"),
    ruku=dict(children="aya"),
    hizb=dict(template="{otype} {number}", childrenPlain=False, children="aya"),
    page=dict(template="{otype} {number}", childrenPlain=False, children="aya"),
    lex=dict(template="{lemma}", lexOcc="word"),
    group=dict(wrap=False),
    word=dict(featuresBare="pos posx", features="lemma root formation tense"),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
