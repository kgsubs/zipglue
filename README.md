# ZIP Merge

Extract every `.zip` file in a folder into one output folder, as if they were never split. Useful for multi-part Google Drive and Takeout downloads.

- Keeps each archive's folder structure
- Skips files that already exist instead of overwriting them
- Skips entries whose path would land outside the output folder
- Warns about and skips invalid ZIP files
- Asks for confirmation before extracting

## Requirements

Python 3.9+, standard library only.

## Usage

```bash
python merge_zips.py /path/to/zips /path/to/output
python merge_zips.py /path/to/zips   # output defaults to ./output
```
