from ddtrace import patch_all
patch_all()

import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    version = None
    with open(os.path.join(os.path.dirname(__file__), '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__'):
                version = line.split('=')[1].strip().strip('"')
    if version is None:
        return "Unable to read version"

    repo = Repo('.')
    latest_tag = str(repo.git.describe("--tags", "--abbrev=0", "--match", "v*"))

    # compare the application version with the latest tag
    if latest_tag == version:
        new_version = None  # assign None to the new version variable
        # do something if the version matches the latest tag
    else:
        new_version = version  # assign the current version to a new variable
        # do something if the version does not match the latest tag

    return f"The new version is {new_version}"  # return the new version variable as the response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
