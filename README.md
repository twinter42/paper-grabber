# paper-grabber

A simple python script to scrape and sort papers from different journals given a weighted keyword list. This way, important papers might be recognized faster.

## Currently supported journals
- [Optica](https://opg.optica.org/optica/home.cfm), [Applied Optics](https://opg.optica.org/ao/home.cfm), [JOSA A](https://opg.optica.org/josaa/home.cfm), [Optics Letters](https://opg.optica.org/ol/browse.cfm), [AOP](https://opg.optica.org/aop/browse.cfm)
- [Nature Protocols](https://www.nature.com/nprot/), [Photonics](https://www.nature.com/nphoton/), [Physics](https://www.nature.com/nphys/), [Cell Biology](https://www.nature.com/ncb/)
- [Review of Scientific Instruments](https://aip.scitation.org/journal/rsi)

See [Steps to implement a new journal](#steps-to-implement-a-new-journal) to implement a new journal.

## Requirements
- `beautifulsoup4==4.11.2`
- `requests==2.28.2`

Older versions might work too. After cloning the repository
```bash
$ git clone https://github.com/twinter42/paper-grabber.git
```
install the dependencies with 
```bash
$ pip install -r requirements.txt
```


## Usage example
In this example, all articles from Applied Optics are sorted by keyword score and printed to the console:
```python
from journals.optica_applied_optics import AppliedOptics

my_journal = AppliedOptics()
articles = my_journal.get_article_list(no_issues=7) # return the list of articles sorted by keyword score

for a in articles:
    print(a.score, a.href, a.title)
```
The output might look like this (depending on the kewyords set in `relevance_scores.txt`):
```
10 https://opg.optica.org/ao/abstract.cfm?uri=ao-62-4-1035 Optical trapping force on a stratified chiral particle by high-order Bessel beam
10 https://opg.optica.org/ao/abstract.cfm?uri=ao-62-1-255 Bessel acoustic-beam acoustic lens for extending the depth of field of detection in optical-resolution photoacoustic microscopy
7 https://opg.optica.org/ao/abstract.cfm?uri=ao-62-7-1865 Scattering characteristics of a terahertz Bessel vortex beam by 3D dielectric-coated targets
7 https://opg.optica.org/ao/abstract.cfm?uri=ao-62-5-1328 Modeling of the effects of intrapulse Raman scattering on dissipative solitons in a mode-locked fiber laser
5 https://opg.optica.org/ao/abstract.cfm?uri=ao-62-10-D39 Adapting a Blu-ray optical pickup unit as a point source for digital lensless holographic microscopy
...
0 https://opg.optica.org/ao/abstract.cfm?uri=ao-62-1-27 Nanoscale and ultra-high extinction ratio optical memristive switch based on plasmonic waveguide with square cavity
0 https://opg.optica.org/ao/abstract.cfm?uri=ao-62-1-102 Structure of 4  ×  2 optical encoder based on hybrid plasmonic waveguides
```

Keyword weights can be setup in `relevance_scores.txt`. For someone interested in adaptive optics and less interested in giraffes, the file might look like this:
```csv
adaptive,10
giraffe,-5
```
One can add as many keywords as necessary.

## Usage for multi-journal publishing groups
Larger publishing groups like Nature can be reduced to a single class with arguments (see `nature.py` for example). Usage is similar:
```python
from journals.nature import Nature

my_journal = Nature(journal='nphoton')
articles = my_journal.get_article_list(no_issues=3) # return the list of articles sorted by keyword score

for a in articles:
    print(a.score, a.href, a.title)
```
Currently supported multi-journal publishing groups: [Nature](https://www.nature.com/), [Optica](https://opg.optica.org/).

## Steps to implement a new journal
- Subclass the `Journal` class (see examples of already implemented journals)
- Use DevTools to find HTML elements corresponding to paper title, author and DOI
- Overwrite methods `get_newest_issues()` and `get_articles()`
