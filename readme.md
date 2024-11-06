# Caption Root Creator

A simple Python script that creates paired text files for image datasets, useful for AI training data preparation. The script creates a text file for each image in a directory, with each text file containing a user-specified caption root phrase.

## Purpose

When preparing image datasets for AI training, it's often necessary to have text files paired with images containing specific caption formats. This script automates the process by:

1. Creating a .txt file for each image in a directory
2. Using matching filenames (e.g., image1.jpg → image1.txt)
3. Writing a user-specified caption root phrase to each text file

## Features

- Supports PNG and JPG image formats
- Preserves exact whitespace and punctuation in caption roots
- Processes all images in the current directory
- Provides progress feedback and completion summary
- Includes error handling

## Installation

1. Ensure you have Python installed on your system
2. Download all files from this repository:
   - `caption-root-creator.py` (main script)
   - `run_caption_root.bat` (Windows batch file)

## Usage

### Method 1: Using the Batch File (Windows)

1. Place both script files in the directory containing your images
- or use > git clone https://github.com/MushroomFleet/CaptionRoot
- while inside your dataset folder.
2. Double-click `run_caption_root.bat`
- or type > run_caption_root.bat
- while in terminal.
3. Enter your desired caption root phrase when prompted
4. Wait for completion message
- check the caption root has been created
- if correct, delete my .bat, .py and readme.md
- dataset is ready to be "appended with Vision/auto tagger" (separately)

### Method 2: Using Python Directly

1. Open a terminal/command prompt
2. Navigate to the directory containing your images and the script
3. Run: `python caption-root-creator.py`
4. Enter your desired caption root phrase when prompted

## Example

If your directory contains:
```
image1.jpg
image2.png
```

And you enter the caption root:
```
photo of xjx style, 
```

The script will create:
- `image1.txt` containing "photo of xjx style, "
- `image2.txt` containing "photo of xjx style, "

## Requirements

- Python 3.6 or higher
- No additional packages required (uses only standard library)

## Directory Structure

```
your-image-folder/
├── caption-root-creator.py
├── run_caption_root.bat
├── image1.jpg
├── image2.png
└── ... (other image files)
```

## Limitations

- Only processes .jpg, .jpeg, and .png files
- Creates text files in the same directory as images
- Overwrites existing text files with matching names

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature requests.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Author's Note

This script was created to simplify the process of preparing image datasets for AI training. If you find it useful or have suggestions for improvements, please let me know through Github issues.
