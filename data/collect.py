from lxml import html,etree
import requests

ARCHIVE_CALENDAR_URL='http://archives.cn.ffcorientation.fr/calendrier.php'

def parse_archive_calendar(tree):
    # brute force : get all tr - check if td with link to competition.php inside
    for tr in tree.find_element("tr"):
        td = tr.find_element("td")
        if

def collect_archive():
    calendar = html.fromstring(requests.get(ARCHIVE_CALENDAR_URL).content)
