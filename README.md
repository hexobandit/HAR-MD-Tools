# 🛠️ HAR and MD Tools 🛠️
A collection of Python scripts for converting HAR files to Mermaid Markdown diagrams and cleaning up busy Mermaid Markdown content.

#### Why Use These Tools?
- Convert Burp Suite's XML to HAR
- Convert HAR files to Mermaid Markdown MD files
- Clean up busy Mermaid diagrams


# burps-xml2har.py 📦📜➡️📂
Transform XML generated by Burp Suite into HAR file

#### Usage
    python3 burps-xml2har.py example.xml 

Example:
- Input: example.xml
- Output: example.har 

# har2md.py 📂🔍➡️📈
Converts a HAR file into a Mermaid sequenceDiagram for visualizing HTTP request flows

#### Usage
    python3 har2md.py example.har

Example:
- Input: example.har
- Output: example.md 

#### Result

    sequenceDiagram
    Client->>example.com: GET https://example.com/api/data
    example.com-->>Client: Response 200

This can however in some cases produce very busy diagrams. For example let's analyze https://trackmytime.net:

<img width="759" alt="image" src="https://github.com/user-attachments/assets/6e975eba-a10e-4b0c-9316-5d2a48291d73" />

In the above screenshot, you can see communication going to fonts and google-analytics endpoints, which might not be relevant for our analysis. If that’s the case, we can simply delete all references that we don’t want in the final diagram. And that’s where the next program comes to save the day:

# mdLineCleaner.py 📈✂️🧹✅
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
