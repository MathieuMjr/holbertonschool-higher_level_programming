#!/usr/bin/env python3
import re


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error message: invalid template content")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    if not isinstance(attendees, list):
        print("Error message: invalid attendees format")
        return
    for element in attendees:
        if not isinstance(element, dict):
            print("Error message: invalid attendees format")
            return
        if not element:
            print("No data provided, no output files generated")
            return

    placeholders = re.findall(r"\{(\w+)\}", template)

    for i, element in enumerate(attendees, start=1):
        content = template
        for placeholder in placeholders:
            value = element.get(placeholder)
            if not value:
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))
        with open(f'output_{i}.txt', 'w', encoding='utf-8') as f:
            f.write(content)
