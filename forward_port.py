import sys
import git
from utils.parser import parse_args
from utils.repo_handler import get_repo_object

(options, args) = parse_args(sys.argv[1:])

# Ensure that all positional arguments are given.
if len(args) != 3:
    parser.print_help()

repo_name = args[0]
source_branch = args[1]
target_branch = args[2]

try:
    repo = get_repo_object(repo_name, target_branch, options)
except git.exc.GitCommandError as e:
    # Get the git error message from stderr and output the message without
    # extraneous characters.
    message = e.stderr.find("fatal:")
    sys.exit(e.stderr[message:-2])

forward_branch = "forward/" + source_branch
git = repo.git

# We do not want to use any pre-existing branch.
try:
    git.branch('-D', forward_branch)
except:
    pass

git.checkout('HEAD', b=forward_branch)

# If using a local repository we want to fetch from the remote.
if options.path_to_repo:
    print "Fetching from remote repository."
    git.fetch()

# TODO: Add merging behavior, see:
# http://gitpython.readthedocs.io/en/stable/tutorial.html#using-git-directly

# TODO: Add continue option. This should be used after conflicts are resolved.
# This will commit and push the changes.
if options.continue_fp:
    sys.exit("The continue option is not yet supported.")
    # TODO: It would be nice to then view the diff here (or be provided with a
    # link of the diff) and then enable one to open a pull request locally. PR
    # should be named something like 'Fwdport forward/rel/6.2.5 to 6.3'. It
    # should be opened against the target branch.

# TODO: Cleanup any cloned repository.

# TODO: FT: use curl command to run an end-to-end and output the build URL.
