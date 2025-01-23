import os
import sys

def clean_md_file(md_file, keywords):
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

if __name__ == "__main__":
    # Check for proper arguments
    if len(sys.argv) < 3:
        print("Usage: python mdLineCleaner.py <md_file> <keyword1> [keyword2] [keyword3] ...")
    else:
        md_file = sys.argv[1]  # First argument: markdown file
        keywords = sys.argv[2:]  # Remaining arguments: keywords
        clean_md_file(md_file, keywords)