# Literary Corpora

This directory contains raw literary texts for atomization analysis.

## Directory Structure

```
corpora/
├── odyssey_excerpt.txt           # Homer's Odyssey excerpts
├── metamorphoses_book1.txt       # Ovid's Metamorphoses
├── beowulf_grendel.txt           # Beowulf excerpts
├── divine_comedy_inferno.txt     # Dante's Divine Comedy
├── canterbury_tales.txt          # Chaucer's Canterbury Tales
└── finnegans_wake.txt            # Joyce's Finnegans Wake
```

## File Format

- **Encoding**: UTF-8
- **Format**: Plain text (.txt)
- **Line breaks**: Preserve original formatting where possible
- **Metadata**: Include translator/edition info in filename or companion `.meta.json`

## Example Metadata File

For `odyssey_excerpt.txt`, create `odyssey_excerpt.meta.json`:

```json
{
  "title": "The Odyssey",
  "author": "Homer",
  "translator": "Robert Fagles",
  "edition": "Penguin Classics, 1996",
  "language": "English (from Ancient Greek)",
  "excerpt": "Book 1, Lines 1-100",
  "genre": "Epic Poetry",
  "tradition": "Greek"
}
```

## Recommended Sources

### Public Domain Texts
- [Project Gutenberg](https://www.gutenberg.org/)
- [Perseus Digital Library](http://www.perseus.tufts.edu/) (Classical texts)
- [Internet Archive](https://archive.org/details/texts)

### Academic Repositories
- [Oxford Text Archive](https://ota.bodleian.ox.ac.uk/)
- [CELT: Corpus of Electronic Texts](https://celt.ucc.ie/)

## Copyright Notice

Ensure all texts comply with copyright law:
- **Public domain**: Works published >95 years ago (US)
- **Fair use**: Small excerpts for scholarly analysis
- **Licensed**: Check Creative Commons or similar licenses

**Do not commit copyrighted material without permission.**

## Data Privacy

This directory is **git-ignored** to prevent accidental commits of copyrighted texts.

To track specific files, use:
```bash
git add -f data/raw/corpora/public_domain_text.txt
```

## Sample Text

A small sample Odyssey excerpt is included in the atomization notebook for demonstration purposes.

To add your own texts:
1. Place `.txt` file in this directory
2. Optionally add `.meta.json` with metadata
3. Update atomization notebooks to reference new file
