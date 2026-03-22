### data dictionary: label mappings across models

to prevent confusion, here is the official mapping of numeric labels to their text meanings for all models in this project:

**model a (sentiment analysis)**
* `0` = negative (source: imdb)
* `1` = positive (source: imdb)
* `2` = neutral (source: goemotions, original label 27)

**model b (emotion classification - multi-label)**
* binary `0` (absent) or `1` (present) for 9 classes:
  `sadness`, `anger`, `fear`, `disgust`, `anticipation`, `joy`, `surprise`, `gratitude`, `love`

**model c (style classification)**
* `0` = informal / colloquial / slang
* `1` = formal / polite / business