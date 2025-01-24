import json
import xml.etree.ElementTree as ET
import base64
import sys


def xml_to_har(xml_file, har_file):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Prepare HAR structure
        har_data = {
            "log": {
                "version": "1.2",
                "creator": {
                    "name": "XML-to-HAR Converter",
                    "version": "1.0"
                },
                "entries": []
            }
        }

        # Loop through Burp XML <item> elements
        for item in root.findall('item'):
            request_data = item.find('request').text or ""
            response_data = item.find('response').text or ""

            # Handle Base64 encoded data
            if item.find('request').attrib.get('base64') == "true":
                request_data = base64.b64decode(request_data).decode('utf-8', errors='replace')
            if item.find('response').attrib.get('base64') == "true":
                response_data = base64.b64decode(response_data).decode('utf-8', errors='replace')

            # Build HAR entry
            har_entry = {
                "startedDateTime": item.find('time').text,
                "time": 0,
                "request": {
                    "method": item.find('method').text,
                    "url": item.find('url').text,
                    "httpVersion": "HTTP/1.1",
                    "headers": [],  # Burp doesn't provide headers directly in this format
                    "queryString": [],  # Needs to be parsed from URL if required
                    "postData": {
                        "mimeType": "application/x-www-form-urlencoded",
                        "text": request_data.strip()
                    } if item.find('method').text == "POST" else None,
                },
                "response": {
                    "status": int(item.find('status').text),
                    "statusText": "OK",
                    "httpVersion": "HTTP/1.1",
                    "headers": [],
                    "content": {
                        "size": int(item.find('responselength').text),
                        "mimeType": item.find('mimetype').text,
                        "text": response_data.strip()
                    }
                },
                "cache": {},
                "timings": {
                    "send": 0,
                    "wait": 0,
                    "receive": 0
                }
            }
            har_data["log"]["entries"].append(har_entry)

        # Save HAR data to file
        with open(har_file, 'w', encoding='utf-8') as har_output:
            json.dump(har_data, har_output, indent=4, ensure_ascii=False)

        print(f"Successfully converted {xml_file} to {har_file}.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python xml_to_har.py <input_xml_file> <output_har_file>")
        sys.exit(1)

    input_xml = sys.argv[1]
    output_har = sys.argv[2]

    xml_to_har(input_xml, output_har)