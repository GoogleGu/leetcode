# author: Arthur
# date: 2018.12.28

import re
import time


def domain_name(url):
    match = re.match(r"(https?://)?(www\.)?(?P<name>((\w+)\.?)+)\.", url)
    time.sleep(1)
    return match.group('name') if match else ''


print(domain_name("www.baidu.com"))
