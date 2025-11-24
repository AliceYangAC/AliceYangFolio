from flask import Flask, render_template, request, json
import os

# Get port from environment variable or default to 10000 (for Render)
port = int(os.environ.get("PORT", 10000))  

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "dev")  # Needed for flash messages

# Define route to handle requests to the root URL ('/')
@app.route("/")
def index():
    # Get selected tags from query parameters when user selects tags in the filter
    tag_query = request.args.get("tags", "")
    selected_tags = tag_query.split(",") if tag_query else []

    # Load repository data from repos.JSON file
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

    # Extract all unique tags for the filter bar, ordered alphabetically
    all_tags = sorted({tag for repo in all_repos for tag in repo.get("tags", [])})

    return render_template("index.html", repos=repos, all_tags=all_tags, selected_tags=selected_tags)

# Define route to handle requests to the /art URL
@app.route("/art")
def art():
    # Define the path to the static folder
    static_folder = os.path.join(app.root_path, 'static')
    
    # Get all files starting with "image" and ending with ".png"
    image_files = [f for f in os.listdir(static_folder) if f.startswith('image') and f.endswith('.png')]
    
    # Sort them naturally so image2 comes before image10
    try:
        image_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    except:
        image_files.sort() # Fallback if naming is inconsistent

    # Pass this list to your template
    return render_template('art.html', image_files=image_files)

# Define route to handle requests to the contact page; POST method handled by Formspree
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
