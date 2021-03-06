"""
Regular expressions go here
"""
import re
# Morpheme-parsing regexps
morphology = [
    # ni allomorph
    (re.compile(r"^ni([ly][aeiou])\1"),
        r"`in`-RED-\1"),
    (re.compile(r"^ni([ly][aeiou]\w)"),
        r"`in`-\1"),
    (re.compile(r"^ini([lyh]?[aeiou])\1"),
        r"i-`in`-RED-\1"),
    (re.compile(r"^ini([lyh]?[aeiou]\w)"),
        r"i-`in`-\1"),
    # Reduplication + Infixation
    (re.compile(r"(\w?)(um|in)([aeiou])\1\3"),
        r"`\2`-RED-\1\3"),
    # Infixation
    (re.compile(r"^([^aeiou]?)(um|in)([aeiou]\w)"),
        r"`\2`-\1\3"),
    # Mag/Pag + RED
    (re.compile(r"(^|\W)([mpn]ag)(\w{2})\3"),
        r"\1\2-RED-\3"),
    (re.compile(r"(^|\W)([mpn]ag)-([aeiou])\3"),
        r"\1\2-RED-\3"),
    # Mag/Pag (Vowel-initial stems don't need changing)
    (re.compile(r"(\W|^)([mpn]ag)([^aeiou-])"),
        r"\1\2-\3"),
    # MaN/PaN/NaN + RED
    (re.compile(r"(\W|^)([mpn]a)(ng?|m)(\w{2})\4"),
        r"\1\2N-RED-\4"),
    (re.compile(r"(\W|^)([mpn]a)(ng)-([aeiou])\4"),
        r"\1\2N-RED-\4"),
    # MaN/PaN/NaN
    (re.compile(r"(\W|^)([mpn]a)(ng?|m)([^aeiou])"),
        r"\1\2N-\4"),
    # M-initial with RED
    (re.compile(r"^(ma|na|maka|naka)(\w{1,2})\2"),
        r"\1-RED-\2"),
    # Reduplication only
    (re.compile(r"^([^aeiou]?[aeiou])\1"),
        r"RED-\1"),
    # M-initial Prefixes
    (re.compile(r"^(maka|naka|nakaka|makaka|napaka|ma|na)(\w{2})"),
        r"\1-\2"),
    # Recent Perfective
    (re.compile(r"^ka(\w{2})\1"),
        r"kaRED-\1"),
    (re.compile(r"^kaka(\w)"),
        r"kaRED-\1"),
    # Linker
    (re.compile(r"(\w{2})ng$"),
        r"\1=na"),
    # Linker Update
    (re.compile(r"=na"),
        r"n=na"),
    # PV/LV suffix
    (re.compile(r"(\w{3})(in|an)$"),
        r"\1-@\2"),
    # PV Update
    (re.compile(r"(`in`|na|ma)-(\S+)$"),
        r"\1-\2-(in)"),
]

# Glosses (IN PROGRESS)
"""
( |=)na( )
$1Lk$2

# PV Forms
na-([^(\s]+)-\(in\)
Nvol.Inch-$1-Pv
`in`-([^(\s]+)-\(in\)
`Inch`-$1-Pv

\bako(=|\s)
1sg.Nom$1
\b(ka|ikaw)(=|\s)
2sg.Nom$1
\bsiya(=|\s)
3sg.Nom$1
\bkami(=|\s)
1pl.Excl.Nom$1
\btayo(=|\s)
1pl.Incl.Nom$1
\bkayo(=|\s)
2pl.Nom$1
\bsila(=|\s)
3pl.Nom$1

\bko(=|\s)
1sg.Gen$1
\bmo(=|\s)
2sg.Gen$1
\bniya(=|\s)
3sg.Gen$1
\bnamin(=|\s)
1pl.Excl.Gen$1
\bnatin(=|\s)
1pl.Incl.Gen$1
\bnin?yo(=|\s)
2pl.Gen$1
\bnila(=|\s)
3pl.Gen$1

\bakin(=|\s)
1sg.Obl$1
\bi?yo(=|\s)
2sg.Obl$1
\bkani?ya(=|\s)
3sg.Obl$1
\bamin(=|\s)
1pl.Excl.Obl$1
\batin(=|\s)
1pl.Incl.Obl$1
\binyo(=|\s)
2pl.Obl$1
\bkanila(=|\s)
3pl.Obl$1
"""
