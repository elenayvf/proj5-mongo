"""test_suite.py"""
import arrow

from test_humanize import humanize_arrow_date

now = arrow.utcnow().naive
tz = arrow.utcnow().replace(hour = 16, minute =40).naive
tom = arrow.utcnow().replace(hour =+ 21).naive

def test_suite():
	#time zone issue 
	assert humanize_arrow_date(now) == "Today"
	assert humanize_arrow_date(tz) == "Today"
	

	#close to tomorrow (doesn't say "3 hrs", says "tomorrow")
	assert humanize_arrow_date(tom) == "Tomorrow"




test_suite()


