import os
from utils.repo_handler import get_repo_object
from utils.parser import parse_args

def test_get_repo_object():
    (options, args) = parse_args([])
    repo = get_repo_object("utapi", "master", options)
    # The current working directory is the root of this project.
    assert os.path.isdir("./utapi"), "Repository not cloned to project root."
