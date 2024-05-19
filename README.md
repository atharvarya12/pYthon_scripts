# Automation Scripts

## Description
A collection of scripts to automate various tasks. Each script is designed to handle a specific type of automation.

## Prerequisites
- Python 3.x
- Required libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/automation-scripts.git
    cd automation-scripts
    ```

2. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## Scripts

### Download Automation

#### Description
This script automatically sorts files in your download folder into specific subfolders based on file type.

#### Configuration
Edit the script to set your download and destination folders:
```python
download_folder = "/path/to/download/folder"
destination_folders = {
    'images': "/path/to/images/folder",
    'documents': "/path/to/documents/folder",
    'videos': "/path/to/videos/folder",
    'music': "/path/to/music/folder",
    'others': "/path/to/others/folder"
}


