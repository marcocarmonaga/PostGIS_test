#!/usr/bin/python
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # creating a parser
    parser = ConfigParser()
    # reading config file
    parser.read(filename)

    # getting section
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        print(db)
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db