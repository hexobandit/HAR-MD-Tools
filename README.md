# 🛠️ HAR and MD Tools 🛠️
A collection of Python scripts for converting HAR files to Mermaid diagrams and cleaning up Markdown files. 

#### Why Use These Tools?
- Simplify workflows: Convert HAR files or clean Markdown files in seconds.
- Clean up busy Mermaid diagrams: Easy-to-read Mermaid diagrams and cleaned Markdown.
- Single-tool option: Use the combined tool for all-in-one functionality.

## Programs Overview

### 1. har2md.py 📂🔍➡️📈
Converts a HAR file into a Mermaid sequenceDiagram for visualizing HTTP request flows

#### Usage
    python3 har2md.py example.har

Example:
- Input: example.har
- Output: example.md (contains the Mermaid diagram)

#### Result

    sequenceDiagram
    Client->>example.com: GET https://example.com/api/data
    example.com-->>Client: Response 200

This can however in some cases produce very busy diagrams. For example let's analyze https://trackmytime.net:

<img width="759" alt="image" src="https://github.com/user-attachments/assets/6e975eba-a10e-4b0c-9316-5d2a48291d73" />

In the above screenshot, you can see communication going to fonts and google-analytics endpoints, which might not be relevant for our analysis. If that’s the case, we can simply delete all references that we don’t want in the final diagram. And that’s where the next program comes to save the day:

### 2. mdLineCleaner.py ✂️📄🧹✅
Cleans a Markdown file by removing lines that contain specific keywords. Saves the cleaned file and logs deleted lines.

#### Usage
    python3 mdLineCleaner.py example.md keyword1 keyword2

Example:
- Input: example.md, keywords: cookielaw, google
- Outputs:
  - example-cleaned.md (cleaned Markdown)
  - example-deleted.md (deleted lines)

If we take previous trackmytime.net example, by running ```python3 mdLineCleaner.py trackmytime.net.md fonts google``` we would get back much leaner results that would loook something like this:

<img width="754" alt="image" src="https://github.com/user-attachments/assets/fb410b28-ce8f-4bb4-bcd4-2684715985b9" />

Too much hassle? No worries — just use the all-in-one tool below

### 3. har2md-n-mdLineCleaner.py 🦸🚀
The ultimate tool — combines the functionality of both har2md.py and mdLineCleaner.py! 
Use it for converting HAR files or cleaning Markdown.

#### Usage: 
Convert HAR to MD: 📂🔍➡️📈

    python3 har2md-n-mdLineCleaner.py convert example.har

Output: example.md

#### Usage: 
Clean Markdown: ✂️📄🧹✅

    python3 har2md-n-mdLineCleaner.py clean example.md keyword1 keyword2

Outputs:
- example-cleaned.md
- example-deleted.md



## 🧐 How to Obtain a .HAR File:
You can obtain .har files using a variety of tools:

- Browser Developer Tools:
  - Open Developer Tools (F12) in your browser (Chrome, Firefox, Edge, etc.).
  - Go to the Network tab.
  - Load the website you want to analyze.
  - Choose Save all as HAR or Export HAR.

- Burp Suite:
  - Launch Burp Suite and set it up as a proxy.
  - Capture the website traffic.
  - In the HTTP history tab, right-click the requests and choose Save Items to export them as a .har file.
