# Forward Port Friend - beta

Get assistance in forward port operations.

Usage: `python forward_port.py scality_repository source_branch target_branch`

This pushes a new forward port branch `forward/source_branch` to
`scality_repository`. If there are conflicting commits in the merge, the program
exits and you get to resolve the conflicts. Then run the command again with the
`--continue` or `-c` option to finish.

By default, the program will clone a new repository to conduct the forward port
in. If you would rather use a pre-existing repository that you have locally, use
the `-p` or `--path` option to specify its location. For example:
`python forward_port.py scality_repository source_branch target_branch -p
~/repos`

Install dependencies with pip: `pip install -r requirements.txt'

## Testing

The testing suite uses [pytest](http://docs.pytest.org/en/latest/contents.html).
Run tests from the root directory: `pytest`
