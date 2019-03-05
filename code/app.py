from tf.core.helpers import htmlEsc, mdEsc
from tf.applib.helpers import dh
from tf.applib.display import prettyPre, getFeatures
from tf.applib.highlight import hlText, hlRep
from tf.applib.api import setupApi
from tf.applib.links import outLink

PLAIN_LINK = ('http://tanzil.net/#{sura}:{aya}')

SECTION = {'sura', 'aya'}
SURA = 'sura'
AYA = 'aya'
ALT_SECTION = {'manzil', 'sajda', 'juz', 'ruku', 'hizb', 'page'}


class TfApp(object):

  def __init__(*args, **kwargs):
    setupApi(*args, **kwargs)

  def webLink(app, n, text=None, className=None, _asString=False, _noUrl=False):
    api = app.api
    T = api.T
    version = app.version

    (sura, aya) = T.sectionFromNode(n, fillup=True)
    passageText = app.sectionStrFromNode(n)
    href = '#' if _noUrl else PLAIN_LINK.format(
        org=app.org,
        repo=app.repo,
        version=version,
        sura=sura,
        aya=aya,
    )
    if text is None:
      text = passageText
      title = 'show this passage on Tanzil'
    else:
      title = passageText
    if _noUrl:
      title = None
    target = '' if _noUrl else None
    result = outLink(
        text,
        href,
        title=title,
        className=className,
        target=target,
        passage=passageText,
    )
    if _asString:
      return result
    dh(result)

  def _plain(
      app,
      n,
      passage,
      isLinked,
      _asString,
      secLabel,
      **options,
  ):
    display = app.display
    d = display.get(options)

    _asApp = app._asApp
    api = app.api
    L = api.L
    T = api.T
    F = api.F
    otypeRank = api.otypeRank

    nType = F.otype.v(n)
    result = passage
    if _asApp:
      nodeRep = f' <a href="#" class="nd">{n}</a> ' if d.withNodes else ''
    else:
      nodeRep = f' *{n}* ' if d.withNodes else ''

    isText = d.fmt is None or '-orig-' in d.fmt
    if nType == 'word':
      rep = hlText(app, [n], d.highlights, fmt=d.fmt)
    elif nType in SECTION:
      if secLabel:
        label = ('{}' if nType == SURA else '{}:{}')
        rep = label.format(*T.sectionFromNode(n))
      else:
        rep = ''
      isText = False
      rep = mdEsc(htmlEsc(rep))
      rep = hlRep(app, rep, n, d.highlights)
      if nType == AYA:
        if isLinked:
          rep = app.webLink(n, text=rep, className='vn', _asString=True)
        else:
          rep = f'<span class="vn">{rep}</span>'
        rep += hlText(app, L.d(n, otype="word"), d.highlights, fmt=d.fmt)
        isText = True
    elif nType in ALT_SECTION:
      label = f'{F.otype.v(n)} {F.number.v(n)}'
      rep = mdEsc(htmlEsc(label))
      rep = f'<span class="vn">{rep}</span>'
      rep = hlRep(app, rep, n, d.highlights)
      rep = f'{rep}<br/>'
      if d.condenseType is not None and otypeRank[nType] <= otypeRank[d.condenseType]:
        for aya in L.d(n, otype=AYA):
          rep += f'<span class="arb">{app.plain(aya, _asString=True, **options)}</span><br/>'
        # rep += hlText(app, L.d(n, otype='word'), d.highlights, fmt=d.fmt)
    elif nType == 'lex':
      rep = mdEsc(htmlEsc(F.lemma.v(n)))
      rep = hlRep(app, rep, n, d.highlights)
    else:
      rep = hlText(app, L.d(n, otype='word'), d.highlights, fmt=d.fmt)

    if isLinked and nType != AYA:
      rep = app.webLink(n, text=rep, _asString=True)

    tClass = 'arb' if isText else 'trb'
    tClass = display.formatClass[d.fmt] if isText else 'trb'
    rep = f'<span class="{tClass}">{rep}</span>'
    result += f'{rep}{nodeRep}'

    if _asString or _asApp:
      return result
    dh(result)

  def _pretty(
      app,
      n,
      outer,
      html,
      firstSlot,
      lastSlot,
      **options,
  ):
    display = app.display
    d = display.get(options)

    goOn = prettyPre(
        app,
        n,
        firstSlot,
        lastSlot,
        d.withNodes,
        d.highlights,
    )
    if not goOn:
      return
    (
        slotType,
        nType,
        className,
        boundaryClass,
        hlAtt,
        nodePart,
        myStart,
        myEnd,
    ) = goOn

    api = app.api
    F = api.F
    E = api.E
    L = api.L
    T = api.T
    otypeRank = api.otypeRank
    maxSlot = F.otype.maxSlot
    eoslots = E.oslots.data
    isHtml = options.get('fmt', None) in app.textFormats

    bigType = False
    if nType in SECTION | ALT_SECTION:
      if d.condenseType is None or otypeRank[nType] > otypeRank[d.condenseType]:
        bigType = True
    elif d.condenseType is not None and otypeRank[nType] > otypeRank[d.condenseType]:
      bigType = True

    if bigType:
      children = ()
    elif nType in (SECTION | ALT_SECTION) - {AYA}:
      children = L.d(n, otype=AYA)
    elif nType == 'lex':
      children = ()
    elif nType == slotType:
      children = ()
    else:
      children = L.d(n, otype='word')

    (hlClass, hlStyle) = hlAtt

    doOuter = outer and nType in {slotType, 'lex'}
    if doOuter:
      html.append('<div class="outeritem">')

    html.append(f'<div class="{className} {boundaryClass} {hlClass}" {hlStyle}>')

    featurePart = ''

    if nType in SECTION | ALT_SECTION:
      if nType in {AYA, SURA}:
        passage = app.webLink(n, _asString=True)
      else:
        label = f'{F.otype.v(n)} {F.number.v(n)}'
        rep = mdEsc(htmlEsc(label))
        rep = f'<span class="vn">{rep}</span>'
        passage = app.webLink(n, text=rep, _asString=True)
      featurePart = getFeatures(
          app,
          n,
          (),
          **options,
      )
      html.append(
          f'''
    <div class="vl">
        <div class="vrs">{passage}</div>
        {nodePart}
        {featurePart}
    </div>
'''
      )
    else:
      if nodePart:
        html.append(nodePart)

      heading = ''
      occs = ''
      if nType == slotType:
        text = T.text([n], fmt=d.fmt)
        text = text if isHtml else htmlEsc(text)
        tClass = 'ar' if d.fmt is None or '-orig-' in d.fmt else 'tr'
        heading = f'<div class="{tClass}">{text}</div>'
        featurePart = getFeatures(
            app,
            n,
            ('lemma', 'root', 'pos', 'posx', 'formation', 'tense'),
            **options,
        )
      elif nType == 'lex':
        slots = eoslots[n - maxSlot - 1]
        extremeOccs = (slots[0], slots[-1])
        linkOccs = ' - '.join(app.webLink(lo, _asString=True) for lo in extremeOccs)
        heading = f'<div class="h">{htmlEsc(F.lemma.v(n))}</div>'
        occs = f'<div class="occs">{linkOccs}</div>'
        featurePart = getFeatures(
            app,
            n,
            (),
            **options,
        )
      html.append(heading)
      html.append(featurePart)
      html.append(occs)

    for ch in children:
      app._pretty(
          ch,
          False,
          html,
          firstSlot,
          lastSlot,
          **options,
      )
    html.append('''
</div>
''')
    if doOuter:
      html.append('</div>')
