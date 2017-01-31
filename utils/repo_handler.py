from git import Repo

# TODO: Add support for the user to specify a path to a pre-existing repo.
def get_repo_object(repo_name, target_branch, options):
    """Handles getting the repository object.
    """
    if options.path_to_repo:
        sys.exit("The path option is not yet supported.")
    else:
        print "Cloning from remote repository to ./" + repo_name
        return Repo.clone_from("https://github.com/scality/" + repo_name,
                               "./" + repo_name, branch=target_branch)
