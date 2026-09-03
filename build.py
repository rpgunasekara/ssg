import markdown

with open("md/test.md", "r") as file:
    text = file.read()

html = markdown.markdown(text)

print(html)
