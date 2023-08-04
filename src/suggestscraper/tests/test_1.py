import pytest
from suggestscraper import html_to_xpath as htp

### Data
simpleHtml_page_1 = """
<html>
<body>
	<div class="container">
			<div class="image"></div>
			<div class="image"></div>
			<div class="image"></div>
			<div class="image">
				
"""

simpleHtml_page_2 = """
<html>
<body>
	<div class="container">
			<div class="image"></div>
			<div class="image">

				
"""

simpleHtml_page_3= """
<html>
<body>
	<div class="container">
			<div class="image"></div>
			<div class="image"></div>
			<div class="image">
    <div class="image">
    </div>
"""

simpleHtml_page_4= """
<html>
<body>
	<div class="container">
			<div class="image"></div>
			<div class="image"></div>
    </div>        
	<div class="image">
        <div class="image">
			<p>
			</p>
"""

### Testing
test_data = {
    '//body[1]/div[1]/div[4]': simpleHtml_page_1,
    '//body[1]/div[1]/div[2]': simpleHtml_page_2,
    '//body[1]/div[1]/div[3]/div[1]': simpleHtml_page_3,
    '//body[1]/div[2]/div[1]/p[1]': simpleHtml_page_4,
}

@pytest.mark.parametrize("xpath, html", test_data.items())
def test_html_to_xpath(xpath, html):
    encoded_html_into_string = htp.html_to_string(html)
    encoded_html_into_string_wo_closing_tags_in_the_end = htp.remove_last_closing_encoded_tags(encoded_html_into_string)
    result_xpath_translation = htp.encodedString_to_xpath(encoded_html_into_string_wo_closing_tags_in_the_end) 

    assert xpath == result_xpath_translation, f"Test failed for {xpath} and {html}"

