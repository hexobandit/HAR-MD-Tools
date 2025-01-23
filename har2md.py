import json
import os
import sys


# HAR TO MERMAID MD CONVERTER
# USE IT LIKE: python3 har2md.py www.trackmytime.net.har


def har_to_mermaid(har_file):
    try:
        # Ensure the HAR file exists
        if not os.path.isfile(har_file):
            print(f"Error: File '{har_file}' not found.")
            return
        
        # Generate output file name by replacing .har with .md
        output_file = os.path.splitext(har_file)[0] + ".md"

        # Read the HAR file
        with open(har_file, "r", encoding="utf-8") as file:
            har_data = json.load(file)
        
        # Extract entries from the HAR log
        entries = har_data.get("log", {}).get("entries", [])
        if not entries:
            print("No entries found in the HAR file.")
            return
        
        # Start building the Mermaid sequenceDiagram
        mermaid_diagram = ["sequenceDiagram"]
        
        for entry in entries:
            # Extract request and response details
            request = entry.get("request", {})
            response = entry.get("response", {})
            
            # Extract source (client) and destination (server)
            source = "Client"
            destination = request.get("url", "Unknown URL").split("/")[2]  # Extract hostname from URL
            
            # Extract method (GET, POST, etc.)
            method = request.get("method", "UNKNOWN")
            
            # Add the interaction to the Mermaid diagram
            mermaid_diagram.append(f"{source}->>{destination}: {method} {request.get('url')}")
            
            # Optionally, include response status
            status = response.get("status", "No Status")
            mermaid_diagram.append(f"{destination}-->>{source}: Response {status}")
                
        # Write the Mermaid diagram to the output file
        with open(output_file, "w") as out_file:
            out_file.write("\n".join(mermaid_diagram))
        
        print(f"Mermaid sequenceDiagram saved to {output_file}")
    
    except Exception as e:
        print(f"Error processing HAR file: {e}")

if __name__ == "__main__":
    # Check if a filename was provided
    if len(sys.argv) != 2:
        print("Usage: python har2md.py <har_file>")
    else:
        har_file = sys.argv[1]
        har_to_mermaid(har_file)