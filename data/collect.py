from lxml import html,etree
import requests

ARCHIVE_CALENDAR_URL='http://archives.cn.ffcorientation.fr/calendrier.php'

def parse_archive_calendar(tree):
    # brute force : get all tr - check if td with link to competition.php inside
    tree.find_attribute

def collect_archive():
    calendar = html.fromstring(requests.get(ARCHIVE_CALENDAR_URL).content)
