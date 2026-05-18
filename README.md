# emoji-counter

A tiny Python utility that counts how many emoji characters appear in a given text file or from standard input.

## Usage

```bash
# Count emojis in a file
python3 emoji_counter.py path/to/file.txt

# Or pipe text into it
cat somefile.txt | python3 emoji_counter.py
```

The script prints the total number of emojis found and a breakdown of each unique emoji with its occurrence count.

## How it works

The script uses a regular expression that matches the most common Unicode emoji ranges (emoticons, pictographs, transport & map symbols, miscellaneous symbols, dingbats, and supplemental symbols). It reads the entire input, finds all emojis, and reports the statistics.

## No external dependencies

The utility only relies on Python's standard library, so you can run it with any recent Python 3 installation.
