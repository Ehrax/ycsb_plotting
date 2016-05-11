#!/bin/python
import argparse
import re
import matplotlib.pyplot as plt
import os

CURRENT_DIR = os.getcwd()
one_file = False


def parse_file(str):
    regex = re.compile("([0-9]+)(.)?.sec.\s[0-9]+\s", re.DOTALL)
    ops_regex = re.compile("([0-9]+(\.[0-9]+)?)\scurrent\sops\/sec")

    sec_tuple = regex.findall(str)
    ops_tuple = ops_regex.findall(str)

    sec_list = [x[0] for x in sec_tuple]
    ops_list = ['0'] + [x[0] for x in ops_tuple]

    return sec_list, ops_list


def plot_files(paths):
    regex = re.compile(".+/(.+)\.+")

    for p in paths:
        title = re.match(regex, p).group(1)

        data = open(p).read()
        sec_list, ops_list = parse_file(data)
        draw(sec_list, ops_list, title)

        if not one_file:
            plt.savefig("{}/results/{}".format(CURRENT_DIR, title))
            plt.clf()
        else:
            continue

    if one_file:
        plt.savefig("{}/results/{}".format(CURRENT_DIR, "Test"))


def draw(x, y, title):
    plt.xlabel("sec")
    plt.ylabel("current ops/s")
    plt.title(title)
    plt.plot(x, y)


def plot_recursive(paths, prefix):
    paths_found = []

    for p in paths:
        for root, dirs, files in os.walk(p):
            for file in files:
                if file.startswith(prefix):
                    paths_found.append(os.path.join(root, file))

    plot_files(paths_found)


def main():
    global one_file
    parser = argparse.ArgumentParser(description="YCSB - Plotting Tool")
    parser.add_argument("path", nargs="+", help="path of files")
    parser.add_argument("--o", action="store_true", help="use this if "
                                                         "you want only one "
                                                         "ouput file")
    parser.add_argument("--r", metavar="[prefix]")

    args = parser.parse_args()

    paths = args.path

    if args.o:
        one_file = True

    if not os.path.exists("./results"):
        os.makedirs("./results")

    if args.r is not None:
        prefix = args.r
        plot_recursive(paths, prefix)
    else:
        plot_files(paths)


if __name__ == "__main__":
    main()
