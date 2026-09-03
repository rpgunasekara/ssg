import sys
import os
import markdown

# get filepath info
website = sys.argv[1]
md_dir = os.path.join(website, "markdown")
html_dir = os.path.join(website, "html")

# convert .md to .html
for filename in os.listdir(md_dir):
    if filename.endswith(".md"):
        md_file = os.path.join(md_dir, filename)

        with open(md_file, "r") as file:
            text = file.read()

        html = markdown.markdown(text)
        html_filename = filename[:-3] + ".html"
        html_file = os.path.join(html_dir, html_filename)

        with open(html_file, "w") as file:
            file.write(html)
