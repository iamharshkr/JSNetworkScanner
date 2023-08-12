# JSNetworkScanner

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

JSNetworkScanner is a command-line tool for analyzing JavaScript files on a website to identify HTTP requests. It helps you understand the network activity and communication happening within JavaScript files, aiding in web development and security analysis.

## Features

- Fetches JavaScript files from a website
- Identifies HTTP GET, POST, PUT, and DELETE requests within JavaScript files
- Excludes common libraries and CDNs by default
- Supports single URL input, URLs from a text file, and output to a text file
- Allows excluding additional libraries using the `-e` or `--exclude` argument

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iamharshkr/JSNetworkScanner.git
2. Navigate to the repository folder:
    ```bash
    cd JSNetworkScanner
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
## Usage
Run the script using the following commands:

For a single URL:

    python JSNetworkScanner.py https://example.com

For URLs from a text file:

    python JSNetworkScanner.py -f urls.txt

For output to a text file:

    python script_name.py -f urls.txt -o output.txt
To exclude additional libraries:

    python script_name.py https://example.com -e jquery,moment,axios
Use the -h or --help flag for detailed usage information:

    python script_name.py -h
Examples
Analyzing a single website:

    python script_name.py https://example.com
Analyzing multiple websites from a text file and saving the output:

    python script_name.py -f websites.txt -o results.txt

Analyzing a website and excluding specific libraries:

    python script_name.py https://example.com -e jquery,moment,axios

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Credits
Beautiful Soup \
jsbeautifier

### Feedback and Contribution
Feedback, bug reports, and contributions are welcome! Feel free to open issues or submit pull requests.

Author \
Harsh Kumar
