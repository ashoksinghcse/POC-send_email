from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser


def convert_text_from_html(html):
	soup = BeautifulSoup(html, 'html.parser')

	# Extract text from the HTML
	text = soup.get_text()
	return text

def convert_date_from_string(parse_date,format = "YYYY-mm-dd"):
	s = "2016-03-26T09:25:55.000Z"
	f = "%Y-%m-%dT%H:%M:%S.%fZ"
	out = datetime.strptime(s, f)

	return out
