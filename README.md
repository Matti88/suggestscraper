# SuggestScraper
A Python library that works with the developer suggestions. Suggestions because they are inputs from the user but the rest is automatic

<!-- Adjust the width and height attributes as per your desired scale -->
<div style="display: flex; justify-content: center;">
<img src="asset/suggestScraper.jpg" alt="Mental Suggestion" width="55%" height=auto>
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

With the help of this JSON file, SuggestScraper efficiently handles the post-processing aspect, eliminating the need for manual assignment of new names to the "discovered" JSON paths. 

## What SuggestScraper does?
SuggestScraper's scope extends beyond the example component, as it performs a comprehensive comparison against the entire encoded page, effortlessly identifying multiple instances through simple string search. 

SuggestScrape has the objective to work also when the developers of the source webpage (the one scraped) decide either to rebuild the webpage structure by nesting or un-nesting the target components or to change class structure and naming; invalidating previously collected XPath 

