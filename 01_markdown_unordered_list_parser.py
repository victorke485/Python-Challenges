# Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-07
"""
Given the string of a valid unordered list in Markdown, return the equivalent HTML string.

An unordered list consists of one or more list items. A valid list item appears on its own line and:

Starts with a dash ("-"), followed by
At least one space, and then
The list item text.
The list is given as a single string with new lines separated by the newline character ("\n"). Do not include the newline characters in the item text.

Wrap each list item in HTML li tags, and the whole list of items in ul tags.

For example, given "- Item A\n- Item B", return "<ul><li>Item A</li><li>Item B</li></ul>".
"""

def parse_unordered_list(string_list):
    string_list = string_list.split("\n")
    markdown = str()
    for i in string_list:
        markdown += f"<li>{i.removeprefix('-').strip()}</li>"
    markdown = f"<ul>{markdown}</ul>"

    return markdown

# Tests
print(parse_unordered_list("- Item A\n- Item B"))
print(parse_unordered_list("-  JavaScript\n-  Python"))
print(parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla"))
print(parse_unordered_list("- A-1\n- A-2\n- B-1"))
