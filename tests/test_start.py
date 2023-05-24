def test_cmd_args(args):
	assert len(args) >= 2, "Didn't find any args"
	assert args[1].isdigit() or args[1] == 'log', "Invalid arg. It must be the number of function or 'log'"
