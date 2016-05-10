#!/bin/python
import argparse
import re
import matplotlib.pyplot as plt
import os


def parse_data(str):
    regex = re.compile("([0-9]+)(.)?.sec.\s[0-9]+\s", re.DOTALL)
    ops_regex = re.compile("([0-9]+(\.[0-9]+)?)\scurrent\sops\/sec")

    sec_tuple = regex.findall(str)
    ops_tuple = ops_regex.findall(str)

    sec_list = [x[0] for x in sec_tuple]
    ops_list = ['0'] + [x[0] for x in ops_tuple]

    return sec_list, ops_list


def plot_data(paths):
    regex = re.compile("(.+)\.+")

    for p in paths:
        title = re.match(regex, p).group(1)

        data = open(p).read()
        sec_list, ops_list = parse_data(data)
        draw(sec_list, ops_list, title)


def draw(x, y, title):
    plt.xlabel("sec")
    plt.ylabel("current ops/s")
    plt.title(title)
    plt.plot(x, y)
    plt.savefig("./results/{}".format(title))
    plt.clf()


def main():
    parser = argparse.ArgumentParser(description="YCSB - Plotting Tool")
    parser.add_argument("file", nargs="+", help="path of files")
    parser.add_argument("--o", action="store_true", help="use this if "
                                                         "you want only one "
                                                         "ouput file")

    args = parser.parse_args()

    paths = args.file

    if not os.path.exists("./results"):
        os.makedirs("./results")

    plot_data(paths)


if __name__ == "__main__":
    main()
