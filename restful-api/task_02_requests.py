#!/usr/bin/env python3
"""
This module contains 2 functions :
- one that fecth and print response of
an API call with GET method
- another that fetch and save the result
in a csv file
"""
import requests
import csv


def fetch_and_print_posts():
    """
    This function prints a response of a GET
    API call
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    data_json = r.json()
    for element in data_json:
        for key, value in element.items():
            if key == 'title':
                print(value)


def fetch_and_save_posts():
    """
    This function save the response of a GET API call
    in a csv file
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        dict_list = response.json()
        new_list = []
        for element in dict_list:
            new_dict = {}
            for key in element:
                if key == "id" or key == "title" or key == "body":
                    new_dict[key] = element[key]
            new_list.append(new_dict)
        labels = ["id", "title", "body"]
        with open("posts.csv", 'w') as file:
            writer = csv.DictWriter(file, fieldnames=labels)
            writer.writeheader()
            for element in new_list:
                writer.writerow(element)
