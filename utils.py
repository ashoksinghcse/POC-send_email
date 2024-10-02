from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser


def convert_text_from_html(html):
	soup = BeautifulSoup(html, 'html.parser')

	# Extract text from the HTML
	text = soup.get_text()
	return text

def convert_date_from_string(parse_date,format = "YYYY-mm-dd"):
	# Convert to desired format: 'YYYY-MM-DD HH:MM:SS'
	#print(parse_date)
	dt = parser.parse(parse_date)
	cleaned_date = parse_date.split(' (')[0]
	return datetime.strptime(cleaned_date.split("+")[0], '%Y-%m-%d %H:%M:%S')
