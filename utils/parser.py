from optparse import OptionParser

def parse_args(args):
    usage = "usage: %prog scality_repository source_branch target_branch"
    parser = OptionParser(usage=usage)
    parser.add_option("-c", "--continue", action="store_true", dest="continue_fp",
                      help="continue forward porting after resolved conflicts")
    parser.add_option("-p", "--path", dest="path_to_repo",
                      help="specify the path to a pre-existing repository to use")
    return parser.parse_args()
