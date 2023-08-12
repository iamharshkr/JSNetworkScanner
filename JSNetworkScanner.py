import requests
from bs4 import BeautifulSoup
import re
import argparse
import jsbeautifier
from urllib.parse import urljoin

def fetch_js_files(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        js_files = []

        for script in soup.find_all('script', {'src': re.compile(r'\.js$')}):
            js_url = script.get('src')
            if js_url:
                js_files.append(js_url)

        return js_files
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return []

def find_requests(js_content):
    request_methods = re.findall(r'\.(get|post|put|delete)\s*\(\s*[\'"](.*?)[\'"]', js_content)
    return request_methods

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch JavaScript files from a website and find HTTP requests.")
    parser.add_argument("url", help="URL of the website to fetch JavaScript files from")
    parser.add_argument("-f", "--file", help="Path to a text file containing URLs (one per line)")
    parser.add_argument("-o", "--output", help="Path to the output text file")
    parser.add_argument("-e", "--exclude", help="Comma-separated list of additional library names to exclude")
    parser.add_argument("-v", "--version", action="version", version="1.1", help="Show program's version number and exit")
    args = parser.parse_args()

    base_url = args.url
    if not base_url.startswith("http"):
        base_url = "https://" + base_url

    if args.file:
        with open(args.file, "r") as file:
            urls = [line.strip() for line in file]
    else:
        urls = [args.url]

    excluded_libraries = ["jquery", "bootstrap", "cloudflare", "datatables"]  # Default exclusions
    if args.exclude:
        excluded_libraries.extend(args.exclude.lower().split(','))  # Extend with additional exclusions

    for url in urls:
        js_files = fetch_js_files(url)

        if js_files:
            print(f"JavaScript files found for {url}:")
            for js_file in js_files:
                if any(library in js_file.lower() for library in excluded_libraries):
                    continue  # Skip processing known library files
                full_js_url = urljoin(base_url, js_file)
                print(full_js_url)
                response = requests.get(full_js_url)
                if response.status_code == 200:
                    js_content = response.text
                    js_content = jsbeautifier.beautify(js_content)
                    request_methods = find_requests(js_content)
                    if request_methods:
                        print("HTTP requests found:")
                        for method, req_url in request_methods:
                            print(f"{method.upper()} request: {req_url}")
                else:
                    print(f"Failed to fetch {full_js_url}. Status code: {response.status_code}")
        else:
            print(f"No JavaScript files found for {url}.")

        if args.output:
            output_filename = f"{url.replace('/', '_')}_output.txt"
            with open(args.output, "a") as output_file:
                output_file.write(f"JavaScript files found for {url}:\n")
                for js_file in js_files:
                    if any(library in js_file.lower() for library in excluded_libraries):
                        continue
                    full_js_url = urljoin(base_url, js_file)
                    output_file.write(f"{full_js_url}\n")
                    response = requests.get(full_js_url)
                    if response.status_code == 200:
                        js_content = response.text
                        js_content = jsbeautifier.beautify(js_content)
                        request_methods = find_requests(js_content)
                        if request_methods:
                            output_file.write("HTTP requests found:\n")
                            for method, req_url in request_methods:
                                output_file.write(f"{method.upper()} request: {req_url}\n")
                    else:
                        output_file.write(f"Failed to fetch {full_js_url}. Status code: {response.status_code}\n")
