import loguru_logging
from loguru import logger
import sys
from main_funcs import execute_from_command_line


def main():
	loguru_logging.logger_init()
	execute_from_command_line(sys.argv)


if __name__ == "__main__":
	main() if len(sys.argv) > 1 else logger.error("Command line argument wasn't found")
	input()