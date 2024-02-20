# Personal Dictionary

## Words to Ignore

This is a word list to ignore to get me to stop using Plover default main.json
way of writing main words and to get me to use [Jeff's phrasing](./jeff-phrasing/README.md)

Since this dictionary is always very near the top of the dictionary stack it's
the perfect place for this.

```yaml
EU: '{null}' # I
U: '{null}' # you
E: '{null}' # he
HE: '{null}' # he
SHAOE: '{null}' # she
SHAO*E: '{null}' # she
SHE: '{null}' # she
(UPDATED) T: 'Derek' #  it
TEUS: '{null}' # it is
EUT: '{null}' # it
THE: '{null}' # they
TH: '{null}' # this
THA: '{null}' # that
WE: '{null}' # we
WAOE: '{null}' # we
THR: '{null}' # there
```

## General Words

```yaml
AUPBTSDZ: updates # This is a practical misstroke
TKPWEG: getting # Shorter version of getting instead of TKPWEGT
HRUFRPB: lunch # Swap with lurch
HRA*UFRPB: lurch # Swap with lunch
TP*FGS: info
STUPG: setting up
HRAOEURBG: library # misstroke for library, nobody wants librarying
PHRAOD: payload # misstoke for blood
KPAOUGS: execution # Replaces excusing with I'll never use
KPAEUP: escape
KWROUFRPB: youch
KWROUFP: youch
TPHREU : fully # Replaces {^}fully
TPHR*EU : {^}fully # Use the star for the suffix version
PAORD : password # replaces board
AO*EUD : {^}ide # suffix, replaces ID
STKPWEUL : {^}zilla # Very important suffix for typing filezilla or stenozilla
PHRAT/PUS : platypus
THER/PHEUPB : theremin
HROUT : layout
```

## Bird Watching

```yaml
KES/TRAL: Kestral
RAP/TOR: raptor
RAP/TER: raptor
```

## Phrases

```yaml
SKWAOERD: it is really weird # Out of order (is + it + weird (WAOERD))
ST*: it is # Reverse of ST (is it)
WRARPBD: work around
TWEUL: it will # Replaces twill which I'll never use
```

## Slang

```yaml
PW*T: BTW
```

## Quick Responses

### Reasons

#### Top reasons why Plover stenography is great!

Quick responses for reasons I use stenography and Plover.

```yaml
STOEUPB/1: Stenography is a dreamland for power users! You control your computer with ease.
STOEUPB/2: Stenography is more ergonomic than a normal keyboard and you never need to look at your hands while typing.
STOEUPB/3: Stenography allows users to reach high speeds of 200 WPM+ without strain.
```

#### Reasons I use Neovim

Quick responses for reasons I use Neovim.

```yaml
SREUPL/1: Neovim is a powerful and extensible text editor that is free and open source (Apache 2.0)
SREUPL/2: Neovim is lighting fast as there is no GUI overhead
SREUPL/3: Neovim is cross platform
```

## Conditional Dictionary Mappings

These could be powerful, but this example is not helpful

```bad
AEU       : {=[AEIOUaeiou]/an/a}  # From Plover example, puts "an" if next word starts with AEIOU upper or lower case otherwise "a"
```

## Names

```yaml
T                 : Derek
T/T         : Derek Lomax
T/T/T : derekthecool
STKPWHR*                : Lomax
HRO*EBG                 : Lomax # Sounds like "Loax"
KAS                     : Cass
AD/TKEU                 : Addie
AD/KWREU                : Addie
AD/HRAOEUPB             : Adaline
PHOEUG                  : {^}Magoo
HRA*EUT/OPB             : Layton
```

## Places

```yaml
HRA*EUT: Layton
HRAEU/TOPB: Layton
```

## Email

```yaml
AOE/PHA*EUL: derekthecool@gmail.com
AOE/PHA*EUL/PHA*EUL: dlomax@freeus.com
```

## My Websites

```yaml
PHEU/SAO*EUT: https://dereklomax.com
```

## Date/Time

See [emily-symbols.py](./emily-symbols.py) for more of my time items.

```yaml
KWRAO*ER : {^}{:time:%Y}{^} # Current year
```

## Briefs

```yaml
KR-Z: crazy
```

## Added by Plover

```yaml
KEUBL: configurable
TKAOEUS: device
SPERPT: separator
KWRO*E: uh oh
PWRUPT: abrupt
PWRUPLT: abruptly
HAEPS: happiness
HROEURT: loiter
HROEURGT: loitering
PWOEUPB: binary
TPRO*EUBGS: Firefox
TPRO*BGS: Firefox
KHRAOUD: conclude
SAEUF: save
SAF: safe
13-S: ps1
A*RPBG: angry
PHA*EUL: email
SRO*E: zero
ROEUF: review
TK*EFGS: destination
```
