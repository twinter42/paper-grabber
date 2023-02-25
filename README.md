# paper-grabber

A simple python script to scrape and sort papers from different journals given a weighted keyword list. This way, important papers might be recognized faster.

## Currently supported journals
- [Applied Optics](https://opg.optica.org/ao/home.cfm)
- [Review of Scientific Instruments](https://aip.scitation.org/journal/rsi)

## Requirements
- `beautifulsoup4==4.11.2`
- `requests==2.28.2`

Older versions might work too. Install with 
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
10 https://opg.optica.org/ao//ao/abstract.cfm?uri=ao-62-4-1035 Optical trapping force on a stratified chiral particle by high-order Bessel beam
10 https://opg.optica.org/ao//ao/abstract.cfm?uri=ao-62-1-255 Bessel acoustic-beam acoustic lens for extending the depth of field of detection in optical-resolution photoacoustic microscopy
7 https://opg.optica.org/ao//abstract.cfm?uri=ao-62-7-1865 Scattering characteristics of a terahertz Bessel vortex beam by 3D dielectric-coated targets
7 https://opg.optica.org/ao//ao/abstract.cfm?uri=ao-62-5-1328 Modeling of the effects of intrapulse Raman scattering on dissipative solitons in a mode-locked fiber laser
5 https://opg.optica.org/ao//abstract.cfm?uri=ao-62-10-D39 Adapting a Blu-ray optical pickup unit as a point source for digital lensless holographic microscopy
...
0 https://opg.optica.org/ao//ao/abstract.cfm?uri=ao-62-1-27 Nanoscale and ultra-high extinction ratio optical memristive switch based on plasmonic waveguide with square cavity
0 https://opg.optica.org/ao//ao/abstract.cfm?uri=ao-62-1-102 Structure of 4  ×  2 optical encoder based on hybrid plasmonic waveguides
```

Keyword weights can be setup in `relevance_scores.txt`. For someone interested in adaptive optics and less interested in giraffes, the file might look like this:
```csv
adaptive,10
giraffe,-5
```
One can add as many keywords as necessary.

## Steps to implement a new journal
- Subclass the `Journal` class (see examples of already implemented journals)
- Use DevTools to find HTML elements corresponding to paper title, author and DOI
- Overwrite methods `get_newest_issues()` and `get_articles()`
