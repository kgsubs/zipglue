# ZipGlue

Some services send a big download as several separate ZIP files. This tool unpacks all of them into one folder, so you get back a single complete copy with the original folders intact.

## Good for

- **Google Drive**: large folder downloads that arrive as several ZIPs
- **Google Takeout**: multi-part exports of Gmail, Photos, Drive, and more
- **Apple Data & Privacy (iCloud)**: exports split into parts like `iCloud_Drive_Part_1_of_6.zip`
- **Facebook and Instagram**: "Download your information" archives split across several ZIPs
- **X (Twitter)**: account archives that arrive as multiple ZIPs
- **Box and OneDrive**: huge folders you had to download in smaller batches

Each ZIP must open on its own. Archives that only open together (files ending in `.z01`, `.z02`, or `.001`) need a regular unzip program such as 7-Zip instead.

## What it does

- Keeps each archive's folder structure
- Never overwrites: if a file already exists, it is skipped
- Skips any entry whose path would land outside the output folder
- Warns about and skips damaged or invalid ZIP files
- Lists what it found and asks for confirmation before extracting

## Requirements

Python 3.9+, standard library only. Nothing to install.

## Usage

```bash
python zipglue.py /path/to/zips /path/to/output
python zipglue.py /path/to/zips   # output defaults to ./output
```

Put all the ZIP parts in one folder, point the tool at it, and type `y` to confirm.

## License

MIT
