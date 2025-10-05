#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def seriealize_to_xml(dict, filename):
    p


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for index in root:
        print(root[index].attrib)
