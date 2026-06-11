import json
import os

def on_post_page(output, page, config):
    if page.file.src_path != "index.md":
        return output

    json_path = os.path.join(config["docs_dir"], "connoss_metadata.json")

    with open(json_path, "r", encoding="utf-8") as f:
        jsonld = json.load(f)

    script_tag = f'<script type="application/ld+json">\n{json.dumps(jsonld, indent=2)}\n</script>'

    return output.replace("</head>", f"{script_tag}\n</head>", 1)