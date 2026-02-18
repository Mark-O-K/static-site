import os
from block_markdown import markdown_to_html_node

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for path in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, path)):
            from_path = os.path.join(dir_path_content, path)
            dest_path = os.path.join(dest_dir_path, path.replace(".md", ".html"))
            generate_page(from_path, template_path, dest_path)
        else:
            generate_page_recursive(os.path.join(dir_path_content, path), template_path, os.path.join(dest_dir_path, path))

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page form {from_path} to {dest_path} using template {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("invalid markdown, no title found")