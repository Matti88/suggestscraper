# SuggestScraper
A Python library that works with the developer suggestions. Suggestions because they are inputs from the user but the rest is automatic

<!-- Adjust the width and height attributes as per your desired scale -->
<div style="display: flex; justify-content: center;">
<img src="https://raw.githubusercontent.com/Matti88/suggestscraper/main/.github/images/suggestScraper.jpg" alt="Mental Suggestion" width="55%" height=auto>
</div>

## What is SuggestScraper
Introducing "SuggestScraper" – an innovative Python library inspired by the acclaimed [Autoscraper](https://github.com/alirezamika/autoscraper). Unlike Autoscraper, SuggestScraper brings a fresh approach to web scraping, requiring the programmer to provide two crucial files for optimal performance. 

The first file holds an HTML representation of the example component, which serves as the target for discovery on the desired web page. 

#### Example - Component HTML
```html
<div class="Box-1234 class1">
  <div
    id="698277247"
    class="Box-1234 ResultListAdRowLayout___StyledBox-sc-1rmys2w-0 kzgkLz bwfFNS"
  >
    <a
      href="/iad/immobilien/d/eigentumswohnung/wien/wien-1190-doebling/privat-und-provisionfrei-sehr-schoene-balkon-wohnung-698277247/"
      id="search-result-entry-header-698277247"
      aria-labelledby="search-result-entry-header-698277247"
      class="AnchorLink__StyledAnchor-sc-1ep83ox-0 eSwjrX ResultListAdRowLayout___StyledClientRoutingAnchorLink-sc-1rmys2w-1 bSvKBv"
      data-testid="search-result-entry-header-698277247"
      ><div class="Box-1234 iRETEm">
        <div
          class="Box-1234 AspectRatioBox__Container-sc-pw812s-0 vppAv dSwaIP"
        >
          <img ...
...
```

The second file houses a JSON object acting as a powerful map, linking the "Title" of the extracted value (ideal for seamless integration with Pandas) to its corresponding actual value present in the example component.

#### JSON - Component HTML
```JSON
{    
    "insertionPage": "/iad/immobilien/d/eigentumswohnung/wien/wien-1190-doebling/privat-und-provisionfrei-sehr-schoene-balkon-wohnung-698277247/",
    "Agency": "Privat",
    "thumbnail_image": "https://cache.willhaben.at/mmo/7/698/277/247_40030140_hoved.jpg",
    "sqm": "70",
    "Title": "Privat und Provisionfrei, sehr schöne Balkon Wohnung",
    "Address": "1190 Wien, 19. Bezirk, Döbling, Pyrkergasse 1190 Wien",
    "feature1" : "2",
    "feature2" : "Balkon, Loggia" ,   
    "price": "€ 330.000"
}        
```

### Usage
The usage of the SuggestScraper is very simple. First we need to get the path to the files for 

  1. The Example Component that is the target for the download
  2. The Map of the Title of the values and the example values that are in the Example Component File 

```py

# files needed for the exercise
component_url = "../tests/example_component.html"
items_to_extract = "../tests/itemsToExtract.json"

# From JSON map we generate a new map for finding the values in the HTML code
jsonPath_data_location = htp.generate_map_title_to_JSON_path(component_url_, items_to_extract_ )

# Setting SuggestScraper object
suggestScraper_ = htp.Suggestscraper(
                                main_page_file= {{accessed by Selenium }},
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

```

If you run the example in the example folder:
```bash
$ python examples/houses_at.py
                                       insertionPage                              Agency                                    thumbnail_image  ... feature1        price                feature2
0  /iad/immobilien/d/eigentumswohnung/wien/wien-1...                      KOI Immobilien  https://cache.willhaben.at/mmo/3/691/616/723_-...  ...        1    € 279.000                     NaN
1  /iad/immobilien/d/eigentumswohnung/wien/wien-1...                      NEW Immobilien  https://cache.willhaben.at/mmo/1/700/412/031_-...  ...        3    € 320.000                     NaN
2  /iad/immobilien/d/eigentumswohnung/wien/wien-1...  PlanetHome Immobilien Austria GmbH  https://cache.willhaben.at/mmo/3/647/027/243_-...  ...        2    € 890.000                Terrasse
3  /iad/immobilien/d/eigentumswohnung/wien/wien-1...  PlanetHome Immobilien Austria GmbH  https://cache.willhaben.at/mmo/7/574/722/427_2...  ...        4  € 2.350.000  Terrasse, Dachterrasse
4  /iad/immobilien/d/eigentumswohnung/wien/wien-1...                     3SI Makler GmbH  https://cache.willhaben.at/mmo/4/694/163/244_6...  ...        1    € 219.000            Dachterrasse
```


With the help of this JSON file, SuggestScraper efficiently handles the post-processing aspect, eliminating the need for manual assignment of new names to the "discovered" JSON paths. 

## What SuggestScraper does?
SuggestScraper's scope extends beyond the example component, as it performs a comprehensive comparison against the entire encoded page, effortlessly identifying multiple instances through simple string search. 

SuggestScrape has the objective to work also when the developers of the source webpage (the one scraped) decide either to rebuild the webpage structure by nesting or un-nesting the target components or to change class structure and naming; invalidating previously collected XPath 

