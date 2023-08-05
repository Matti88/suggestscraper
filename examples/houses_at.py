
import os
import sys
# Add the parent directory of the project to the PYTHONPATH - useful for importing the suggestscraper 
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)
from src.suggestscraper import html_to_xpath as htp


# Get the absolute path of the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))


# files needed for the exercise
page_url =  '../tests/example_main_page.html'
component_url = "../tests/example_component.html"
items_to_extract = "../tests/itemsToExtract.json"

page_url_ = os.path.join(script_dir, page_url)
component_url_ = os.path.join(script_dir, component_url)
items_to_extract_ = os.path.join(script_dir, items_to_extract)

# From JSON map we generate a new map for finding the values in the HTML code
jsonPath_data_location = htp.generate_map_title_to_JSON_path(component_url_, items_to_extract_ )

# Setting SuggestScraper object
suggestScraper_ = htp.Suggestscraper(
                                main_page_file= page_url_,
                                component_file=component_url_
                                )

# List of the all the HTML sections that were found with the suggescraper object
collection_different_components_html = suggestScraper_.list_found_html_sections()

# tranform all the HTML insertion into dataframe also thanks to the jsonPath_data_location
dataframe_collected_items = htp.create_pandas_ds_from_collected_insertions(
                                    collection_different_components_html, 
                                    jsonPath_data_location
                                    )

# printing the collected data from the multiple insertions present in the page
print(dataframe_collected_items)

