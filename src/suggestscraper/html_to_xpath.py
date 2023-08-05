from lxml import etree
import re
import html_to_json
import pandas as pd
from collections import deque
from bs4 import BeautifulSoup
import json
import os

### -------------------------------- MAIN ALGORITHM ----------------------------------
class NodeCharacter:
    def __init__(self, value, level, count):
        self.value = value
        self.level = level
        self.count = count

    def __str__(self):
        return f"<{self.value}, {self.level}, {self.count}>"

    def __repr__(self):
        return f"<{self.value}, {self.level}, {self.count}>"
 
def return_nodes_of_latest_common_root_level(list_popped_out_opening_nodes, level_criterium):
    list_common_root_level = []
    i = len(list_popped_out_opening_nodes) - 1
    while i >= 0 and list_popped_out_opening_nodes[i].level != level_criterium:
        list_common_root_level.append(list_popped_out_opening_nodes[i])
        i -= 1
    return list_common_root_level[::-1]

def string_to_arraypath(input_str):
    
    stack = deque([])
    popped_out_stack = deque([])
    levelCount = 1
    for i in range(len(input_str)):
        c = input_str[i]
        
        if c in reversed_opening_tags:
            #print(c)
            # counting how many previous "same level" characters are present in the popped out "opening character"
            popped_out_stack_latest_root = return_nodes_of_latest_common_root_level(popped_out_stack, levelCount - 1 )
            count = sum(map( lambda x : True if x.value == c and x.level == levelCount else False ,  popped_out_stack_latest_root)) 
            # creating the node character with 1) the value itself 2) level count that is tracking the depth 3) the count of the same opening chars as calculated the line before
            node_ = NodeCharacter(c, levelCount, count+1)
            # adding to the final stack
            stack.append(node_)
            # adding one more level down the tree because the char tested as "opening char"
            levelCount += 1
        
        elif c in reversed_closing_tags: # in this case the char is an "opening char"
            #print(c)
            # testing if really the string is correct and new "closing char" closes the previous opening char 
            closing_value = stack[-1].value
            if open_to_closing_econd_map[closing_value] == c:
                # popping out the last opening char + storing it into a stack for popped out chars
                poppedLetter = stack.pop()
                popped_out_stack.append(poppedLetter)
                # decreasing the level count (we are coming up a level)
                levelCount -= 1
        else:
             return ["error"]
        
    return stack
            
def arraypath_to_xpath(array_levels_and_count):
    
    xpath_string = ""
    reveresed_opening_tags = reverse_dict(opening_tags)
    for node_ in array_levels_and_count:
        
        node_string = reveresed_opening_tags[node_.value] + "["+ str(node_.count)+ "]" + "/"
        xpath_string += node_string

    xpath_string = xpath_string.replace("html[1]","/")
    xpath_string = xpath_string[:-1]
    
    return xpath_string

def encodedString_to_xpath(input_string):
    
    return arraypath_to_xpath( string_to_arraypath(input_string) )
### -------------------------------- MAIN ALGORITHM ----------------------------------


## Generic Utility
def reverse_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[value] = key
    return output_dict

def debug_(string_for_debug, Command):
    if Command:
        print(string_for_debug)
        print("--------------------------------------------------------\n")

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read().replace('\n', '')
    return contents


# map tags to chars
tag_map = {'/a': 'A','/b': 'B','/body': 'C','/button': 'D','/div': 'E','/footer': 'F','/form': 'G'
           ,'/g': 'H','/h': 'I','/head': 'J','/header': 'K','/html': 'L','/iframe': 'M','/img': 'N',
           '/input': 'O','/label': 'P','/li': 'Q','/link': 'R','/meta': 'S','/nav': 'T','/next': 'U',
           '/noscript': 'V','/option': 'W','/p': 'X','/path': 'Y','/rect': 'Z',
           '/script': 'a','/select': 'b','/span': 'c','/strong': 'd',
           '/article':"{",'/style': 'e','/svg': 'f','/title': 'g','/ul': 'h',
           '/source':"-" ,'/hr':">",'/section':"]",'/picture':":", "/circle": "(",
           'a': 'i','b': 'j','body': 'k','button': 'l','div': 'm','footer': 'n','form': 'o',
           'g': 'p','h': 'q','head': 'r','header': 's','html': 't','iframe': 'u',
           'img': 'v','input': 'w','label': 'x','li': 'y','link': 'z' ,'rect': '8','script': '9',
           'meta': '1','nav': '2','next': '3','noscript': '4','option': '5','p': '6','path': '7',
           'select': '0','span': '#','strong': '$','style': '%','svg': '&','title': '^','ul': '*','article':"~",
           'section':"`",'hr':"[",'picture':";",'source':"=",'br':"+","circle": ")"
           }

opening_tags = {'a': 'i','b': 'j','body': 'k','button': 'l','div': 'm','footer': 'n','form': 'o',
                'g': 'p','h': 'q','head': 'r','header': 's','html': 't','iframe': 'u',
                'img': 'v','input': 'w','label': 'x','li': 'y','link': 'z','meta': '1','nav': '2',
                'next': '3','noscript': '4','option': '5','p': '6','path': '7','rect': '8',
                'script': '9','select': '0','span': '#','strong': '$','style': '%','svg': '&',
                'title': '^','ul': '*','article':"~",'section':"`",'hr':"[",'picture':";",
                'source':"=",'br':"+","circle": ")"
                }

closing_tags = {'/a': 'A','/b': 'B','/body': 'C','/button': 'D','/div': 'E','/footer': 'F','/form': 'G','/g': 'H','/h': 'I','/head': 'J','/header': 'K','/html': 'L','/iframe': 'M','/img': 'N',
           '/input': 'O','/label': 'P','/li': 'Q','/link': 'R','/meta': 'S','/nav': 'T','/next': 'U','/noscript': 'V','/option': 'W','/p': 'X','/path': 'Y','/rect': 'Z',
           '/script': 'a','/select': 'b','/span': 'c','/strong': 'd',
           '/article':"{",'/style': 'e','/svg': 'f','/title': 'g','/ul': 'h','/source':"-" ,'/hr':">",'/section':"]",'/picture':":", "/circle": "("
}

reversed_opening_tags =  reverse_dict(opening_tags)

reversed_closing_tags =  reverse_dict(closing_tags)

list_self_closing_tags = ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']

reverse_tag_map = reverse_dict(tag_map)

open_to_closing_econd_map = {}

for key in opening_tags.keys():
    if "/"+key in closing_tags.keys():
        open_to_closing_econd_map[opening_tags[key]] = closing_tags["/"+key]

reverse_open_to_closing_econd_map = reverse_dict(open_to_closing_econd_map)


### HTML Utility
def get_html_tags(html):
    tag_pattern = r'<(\/?[a-zA-Z]+)[^>]*>'
    tags = re.findall(tag_pattern, html)
    return [re.sub(r'\s*[a-zA-Z]+\s*=\s*("[^"]*"|\'[^\']*\')', '', tag) for tag in tags]

def remove_tag_from_html(html):
    remove_non_useful_tags = [ 'script', 'meta','iframe','head','style','path']
    soup = BeautifulSoup(html, 'html.parser')
    for tag_type in remove_non_useful_tags:
        for tag in soup.find_all(tag_type):
            tag.decompose()  # removes the tag and its contents from the HTML
    return str(soup)

def html_to_string(html, tag_map=tag_map):
    """
    Description: This functon encodes the HTML into a string of letters representing opening and closing tags
    Usage: 
        html: the html code to encode
    """
    whbnTxt_CLEAN = get_html_tags(html)

    whbnTxt_CLEAN_2 = [x for x in whbnTxt_CLEAN if x not in list_self_closing_tags]
    
    return u"".join(list(map(lambda x: tag_map[x], whbnTxt_CLEAN_2)))
 
def remove_self_closing_tags(html):
    pattern = re.compile(r'<[^>]+/>')
    return pattern.sub('', html)


### JSONPath Utility
def find_jsonpath(json_data, target_value, path=''):
    """
    A recursive function for finding the JSONPath of the given items
        Usage:
            json_data -> the JSON translated HTML snippet containing the values to extract
            target_value -> the Python Dictionary mapping the title of the content to extract with the value present in the snippet

    This is an example of the target_value:
    target_value = {
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
    """
    result = {}
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            new_path = f"{path}['{key}']"
            if isinstance(value, (dict, list)):
                result.update(find_jsonpath(value, target_value, new_path))
            elif target_value in str(value):
                result[key] = new_path
    elif isinstance(json_data, list):
        for index, value in enumerate(json_data):
            new_path = f"{path}[{index}]"
            if isinstance(value, (dict, list)):
                result.update(find_jsonpath(value, target_value, new_path))
            elif target_value in str(value):
                result[index] = new_path
    return result

def generate_map_title_to_JSON_path(html_file_path, json_file_path ):


    # loading the new example file and generate the extraction JSONPath map

    exampleJsonfied = ""
    with open(html_file_path, "r") as doc:
        exampleHtml = doc.read()
        exampleJsonfied = html_to_json.convert(exampleHtml)
        
    # Open the JSON file for reading
    thingsToFindNewJSONPath = {}
    
    with open(json_file_path, 'r') as file:
        # Load the JSON data into a Python dictionary
        thingsToFindNewJSONPath = json.load(file)

    locations_of_data = {}
    for key, value in  thingsToFindNewJSONPath.items():
        JSONPath_ = find_jsonpath(exampleJsonfied, value)
        keys_to_JSONPath = list(JSONPath_.keys())
        if len(keys_to_JSONPath) > 1 and '_value' in keys_to_JSONPath:
            locations_of_data[key] = JSONPath_['_value']
        else:
            locations_of_data[key] = JSONPath_[keys_to_JSONPath[0]]
    
    return locations_of_data



### calculating the xpath and returnng the path from encoded broken html
def remove_last_closing_encoded_tags(encoded_html, closing_tags=closing_tags):
    for num in range(len(encoded_html), 0 , -1):
        if not( encoded_html[num-1] in closing_tags.values()):
            return encoded_html[0:num]

def from_html_to_component_section(encoded_substring_to_first_component, dom_):
 
    encoded_html_into_string_wo_closing_tags_in_the_end =  remove_last_closing_encoded_tags(encoded_substring_to_first_component)
    result_xpath_translation = encodedString_to_xpath(encoded_html_into_string_wo_closing_tags_in_the_end) 
    returned_component_by_xpath =  dom_.xpath(result_xpath_translation)
    section_of_page = etree.tostring(returned_component_by_xpath[0], pretty_print = True, encoding = str)

    return section_of_page

def html_to_Json_remap(html_page, item_location_map, debugMode=False):
    output_json = html_to_json.convert(html_page)
    if debugMode:
        print(output_json)
    values_of_the_insertions = {}
    exceptions = []
    exception_count = 0
    for k, v in item_location_map.items():
        try: 
            values_of_the_insertions[k] =  eval("output_json" + v)
        except:
            exceptions.append(f"probably the value is not pesesent for {k} for exception # {exception_count}")
            #print( f"probably the value is not pesesent for {k}" )
            exception_count += 0

    if exception_count > 0:
        print(exception_count)
        
    return values_of_the_insertions

def create_pandas_ds_from_collected_insertions( collection_components_html, locations_of_data):
    collection_of_houseInsertions = []

    for html_insertion in collection_components_html:
        c =   html_to_Json_remap(html_insertion, locations_of_data )
        collection_of_houseInsertions.append(c)

    return pd.DataFrame(collection_of_houseInsertions)

### Suggestscraper Class
class Suggestscraper:
    def __init__(self, main_page_file, component_file, similarity_tags_count = 5):
        """
        This classe initialize the suggestscraper Suggestscraper.
        Usage:
            main_page_file : is either the HTML string or the address of the file's location of the Page to be Scraped
            component_file : is either the HTML string or the address of the file's location of the Example component file to be scraped
            similarity_tags_count : is the matching substring lenght. The code will transform the HTML files into long strings and this 
                                    value indicated how long the substring of the example component has to be
        """
        
        self.main_page_file = main_page_file # file name of the whole webpage to download
        self.component_file = component_file # file name of the whole 

        self.html_main_page = None
        self.html_component = None

        self.encoded_main_page = None
        self.encoded_component = None
        
        
        self.starting_of_codes_similar_not_the_ending = None
        self.indexes_starting_points_component = []
        self.lenght_similarity_tags = similarity_tags_count  

        #dom tree as rendered by etree
        self.dom  = None

        # extracting finding the points where objects may be found        
        if main_page_file != "":
            self.load_main_page()
        if component_file != "":
            self.load_component()
        
    def load_main_page(self):
        with open(self.main_page_file, "r") as f:
            self.html_main_page = f.read()
            self.encoded_main_page = html_to_string(self.html_main_page)
            page_soup = BeautifulSoup(self.html_main_page, 'html.parser')
            self.dom = etree.HTML(str(page_soup))


    def load_component(self):
        with open(self.component_file, "r") as f:
            self.html_component = f.read()
            self.encoded_component = html_to_string(self.html_component)
            self.starting_of_codes_similar_not_the_ending = self.encoded_component[0:self.lenght_similarity_tags]

    def findAllsubstringIndexes(self, string, substring):
        indexes = []
        index = string.find(substring)
        while index != -1:
            indexes.append(index)
            index = string.find(substring, index + 1)
        return  indexes

    def find_component_sections(self):
        self.indexes_starting_points_component = self.findAllsubstringIndexes(self.encoded_main_page, self.starting_of_codes_similar_not_the_ending)

    def list_found_html_sections(self):
        self.find_component_sections()
        list_of_matched_components = []
 
        for found_component in range(len(self.indexes_starting_points_component)):
            encoded_substring_to_first_component = self.encoded_main_page[0:self.indexes_starting_points_component[found_component]+1]
            g = from_html_to_component_section(encoded_substring_to_first_component, self.dom)
            list_of_matched_components.append(g)
        return list_of_matched_components


    def set_similarity_count(self, similarity_count):
        self.lenght_similarity_tags = similarity_count
 
 
