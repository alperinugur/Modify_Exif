# EXIF UserComment Modifier

A user-friendly Python tool designed to effortlessly extract, modify, and overwrite the 'UserComment' EXIF field in JPG files.

## Why use this code?

Stable Diffusion puts generation data of the generated image in the JPG or PNG generated file. 

Sometimes you want to tweak on the EXIF data. (i.e. you just run an upscaler, and you want to preserve the original txt-to-image generation info)
Then you can use this to put original (or any other) generation info in the JPG file.

## Features
* **Automated Extraction**: Effortlessly extracts 'UserComment' EXIF data from JPG files.
* **Interactive Editing**: Allows users to edit the EXIF data in a familiar environment - Notepad.
* **Preservation**: Saves the modified EXIF data back to the image, appending '**_EXIF**' for clarity.

## Requirements
* Python 3.x
* Pillow
* Piexif

## Getting Started
### **Installation**
1. **Clone this Repository:**

```
git clone https://github.com/alperinugur/Modify_Exif.git
cd Modify_Exif
```

2. **Create Environment:**    (OPTIONAL)

```
pyton -m venv venv
venv/scripts/activate      # for Linux
venv\scripts\activate.bat  # for Windows
```

3. **Install Dependencies:**

```
pip install -r requirements.txt
```

## Usage

1. Make sure you place your target '**.jpg**' files inside the '**files**' directory.

2. **Run the Script**:
```
venv/scripts/activate      # for Linux
venv\scripts\activate.bat  # for Windows
python main.py
```

**or in Windows**:
```
run.bat
```

3. Follow the prompts: The script extracts 'UserComment', allows for editing in Notepad, then saves changes back into the image.

## Contributing

We're open to enhancements & bug-fixes. Here's how you can contribute:

1. **Report Bugs or Request Features**: Open an issue detailing your suggestion or the bug.
2. **Develop**: Fork this repo and make your contribution.
3. **Pull Request**: Submit a PR with your changes.

## License

Licensed under the MIT License. Check out the  [MIT License](https://opensource.org/licenses/MIT). file for more information.
