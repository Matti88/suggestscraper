from suggestscraper import html_to_xpath as htp
from lxml import etree
import pandas as pd

def test_string_to_arraypath():
    input_str = "m6"
    result = htp.string_to_arraypath(input_str)
    assert len(result) == 2, "Failed test_string_to_arraypath"
    assert result[0].value == "m", "Failed test_string_to_arraypath"
    assert result[0].count == 1, "Failed test_string_to_arraypath"
    assert result[1].value == "6", "Failed test_string_to_arraypath"
    assert result[1].count == 1, "Failed test_string_to_arraypath"


def test_encodedString_to_xpath():

    input_str = "m6"
    result = htp.encodedString_to_xpath(input_str)
    assert result == "div[1]/p[1]", "Failed test_encodedString_to_xpath"


def test_from_html_to_component_section():

    component_html = "<html><head></head><body><div><p></p></div>"
    whole_html_page = "<html><head></head><body><div><p>Hello</p></div></body></html>"
    component_encoded = htp.html_to_string(component_html)
    dom = etree.HTML(whole_html_page)
    result = htp.from_html_to_component_section(component_encoded, dom).replace("\n","")
    assert result == '<p>Hello</p>', "Failed test_from_html_to_component_section"

def test_create_pandas_ds_from_collected_insertions():

    # Mock data
    html_insertion1 = "<div><p>Hello</p></div>"
    html_insertion2 = "<div><p>World</p></div>"
    collection_components_html = [html_insertion1, html_insertion2]
    locations_of_data = {
        "Title": "['div'][0]['p'][0]['_value']",
    }

    result = htp.create_pandas_ds_from_collected_insertions(collection_components_html, locations_of_data)

    # You can perform various assertions on the result dataframe to ensure it's correct.
    assert len(result) == 2, "Failed test_create_pandas_ds_from_collected_insertions"
    assert result["Title"].tolist() == ["Hello", "World"], "Failed test_create_pandas_ds_from_collected_insertions"




def test_Suggestscraper():
 
    # Assuming you have test HTML files for the main_page and component_file.
    main_page_file = "src/suggestscraper/tests/example_main_page.html"
    component_file = "src/suggestscraper/tests/example_component.html"

    scraper = htp.Suggestscraper(main_page_file=main_page_file, component_file=component_file, similarity_tags_count=5)

    assert scraper.html_main_page is not None, "Failed test_Suggestscraper"
    assert scraper.html_component is not None, "Failed test_Suggestscraper"
    assert scraper.lenght_similarity_tags == 5, "Failed test_Suggestscraper"

    scraper.set_similarity_count(10)
    assert scraper.lenght_similarity_tags == 10, "Failed test_Suggestscraper"

    new_html_main_page = "<html><body><h1>New Page</h1></body></html>"
    scraper.set_main_page(new_html_main_page)
    assert scraper.html_main_page == new_html_main_page, "Failed test_Suggestscraper"
