from flask import Flask, render_template, request, json
import os

port = int(os.environ.get("PORT", 10000))  # fallback to 10000 if PORT isn't set

app = Flask(__name__)

@app.route("/")
def index():
    tag_query = request.args.get("tags", "")
    selected_tags = tag_query.split(",") if tag_query else []

    with open("repos.json") as f:
        all_repos = json.load(f)

    # Filter repos that contain ALL selected tags
    if selected_tags:
        repos = [
            r for r in all_repos
            if all(tag in r.get("tags", []) for tag in selected_tags)
        ]
    else:
        repos = all_repos

    # Extract all unique tags for the filter bar
    all_tags = sorted({tag for repo in all_repos for tag in repo.get("tags", [])})

    return render_template("index.html", repos=repos, all_tags=all_tags, selected_tags=selected_tags)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
