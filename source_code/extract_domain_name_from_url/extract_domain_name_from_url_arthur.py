# author: Arthur
# date: 2018.12.28

import re


def domain_name(url):
    match = re.match(r"(https?://)?(www\.)?(?P<name>\w+)\.", url)

    return match.group('name') if match else ''


print(domain_name("https://www.cnet.com"))
