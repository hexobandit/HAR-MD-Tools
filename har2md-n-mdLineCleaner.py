import os
import sys
import json

def clean_md_file(md_file, keywords):
    """
    Cleans lines in a Markdown file that contain specified keywords.
    """
    try:
        # Ensure the input file exists
        if not os.path.isfile(md_file):
            print(f"Error: File '{md_file}' not found.")
            return

        # Generate output file name
        output_file = os.path.splitext(md_file)[0] + "-cleaned.md"
        deleted_file = os.path.splitext(md_file)[0] + "-deleted.md"

        # Open the files for reading and writing
        with open(md_file, "r") as infile, \
             open(output_file, "w") as outfile, \
             open(deleted_file, "w") as del_file:
            
            for line in infile:
                # Check if any keyword matches the line
                if any(keyword in line for keyword in keywords):
                    del_file.write(line)  # Write the matching line to the deleted lines file
                    print(f"Deleted: {line.strip()}")
                else:
                    outfile.write(line)  # Write the non-matching line to the cleaned file

        print(f"Processing complete.")
        print(f"Cleaned lines saved to: {output_file}")
        print(f"Deleted lines saved to: {deleted_file}")

    except Exception as e:
        print(f"Error processing file: {e}")


def har_to_mermaid(har_file):
    """
    Converts a HAR file to a Mermaid sequenceDiagram file.
    """
    try:
        # Ensure the HAR file exists
        if not os.path.isfile(har_file):
            print(f"Error: File '{har_file}' not found.")
            return
        
        # Generate output file name by replacing .har with .md
        output_file = os.path.splitext(har_file)[0] + ".md"

        # Read the HAR file
        with open(har_file, "r") as file:
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
    # Command-line interface
    if len(sys.argv) < 2:
        print("Usage:")
        print("  To clean a Markdown file: python fileTools.py clean <md_file> <keyword1> [keyword2] ...")
        print("  To convert a HAR file: python fileTools.py convert <har_file>")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "clean":
        if len(sys.argv) < 4:
            print("Usage: python fileTools.py clean <md_file> <keyword1> [keyword2] ...")
        else:
            md_file = sys.argv[2]
            keywords = sys.argv[3:]
            clean_md_file(md_file, keywords)

    elif command == "convert":
        if len(sys.argv) != 3:
            print("Usage: python fileTools.py convert <har_file>")
        else:
            har_file = sys.argv[2]
            har_to_mermaid(har_file)

    else:
        print("Unknown command. Use 'clean' or 'convert'.")