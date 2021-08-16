import argparse
import os
import subprocess
import sys

import yaml

arg_parser = argparse.ArgumentParser(
    description="T5 Summarisation Using Pytorch Lightning", prog="t5s"
)
# Command choice
command_subparser = arg_parser.add_subparsers(
    dest="command", help="command (refer commands section in documentation)"
)

parser_req = command_subparser.add_parser(
    "requirements", help="Install Python Dependencies."
)

parser_start = command_subparser.add_parser("start", help="Define parameters")
parser_start.add_argument(
    "-d",
    "--dataset",
    default="cnn_dailymail",
    help="Enter the name of the dataset to be used",
)

parser_start.add_argument("--split", default=0.001, help="Enter the split required")

parser_start.add_argument(
    "-n", "--name", default="summarsiation", help="Enter the name of the model"
)
parser_start.add_argument(
    "-mt", "--model_type", default="t5", help="Enter the model type"
)
parser_start.add_argument(
    "-m",
    "--model_name",
    default="t5-base",
    help="Enter the model to be used eg t5-base",
)
parser_start.add_argument(
    "-e", "--epochs", default=5, help="Enter the number of epochs"
)
parser_start.add_argument(
    "-lr", "--learning-rate", default=0.0001, help="Enter the number of epochs"
)
parser_start.add_argument(
    "-b", "--batch-size", default=2, help="Enter the number of batches"
)

parser_dirs = command_subparser.add_parser(
    "dirs",
    help="Create directories that are ignored by git but required for the project",
)

parser_push = command_subparser.add_parser(
    "push", help="Upload Data to default DVC remote"
)

parser_pull = command_subparser.add_parser(
    "pull", help="Download Data from default DVC remote"
)

parser_run = command_subparser.add_parser(
    "run",
    help="run the DVC pipeline - recompute any modified outputs such as "
    "processed data or trained models",
)

parser_visualize = command_subparser.add_parser(
    "visualize", help="run the visualization using Streamlit"
)

parser_upload = command_subparser.add_parser(
    "upload", help="push the trained model to HF model hub"
)

parser_lint = command_subparser.add_parser("lint", help=" Lint using flake8")

parser_clone = command_subparser.add_parser(
    "clone", help="Clone the T5 summarisation repo"
)


class Run(object):
    def __init__(self, arguments: dict):
        self.arguments = arguments

    def execute(self):
        arguments = self.arguments
        print(f"arguments passed: {arguments['command']}")
        # os.chdir('../')
        cmd = [
            "requirements",
            "dirs",
            "push",
            "pull",
            "run",
            "visualize",
            "upload",
            "lint",
        ]
        if arguments["command"] == "clone":
            list_files = subprocess.run(
                ["git", "clone", "https://dagshub.com/gagan3012/summarization.git"]
            )
            os.chdir("./summarization/")
            retval = os.getcwd()
            print(retval)
            return list_files.returncode
        elif arguments["command"] == "start":
            start(arguments=arguments)
        elif arguments["command"] in cmd:
            list_files = subprocess.run(["make", arguments["command"]])
            return list_files.returncode
        else:
            print("Command not supported")
            raise Exception


def start(arguments):
    data_params = {"data": arguments["dataset"], "split": arguments["split"]}
    model_params = {
        "name": arguments["name"],
        "model_type": arguments["model_type"],
        "model_name": arguments["model_name"],
        "epochs": arguments["epochs"],
        "learning_rate": arguments["learning_rate"],
def parse_args(args):
    arguments = vars(arg_parser.parse_args(args=args or ["--help"]))
    return arguments


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = parse_args(args=args)
    try:
        result = Run(arguments=parsed_args).execute()
    except Exception as e:
        print(str(e))
        result = 1
    sys.exit(result)


if __name__ == "__main__":
    main()
