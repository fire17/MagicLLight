from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
options = Options() 
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
lang="iw"
url = 'https://www.google.com/search?q=%D7%9E%D7%96%D7%92+%D7%90%D7%95%D7%95%D7%99%D7%A8+%D7%94%D7%A8%D7%A6%D7%9C%D7%99%D7%94'
url = 'https://www.google.com/search?q=is+it+going+to+rain+tomorrow+&hl=iw'
url = 'https://www.google.com/search?q=is+it+going+to+rain+tomorrow+&hl=iw'
url = 'https://www.google.com/search?q=what+is+mount+everest&hl=iw'
url = 'https://www.google.com/search?q=what+is+a+dog&oq=what+is+a+dog&h1=iw'
url = 'https://www.google.com/search?q=what+is+a+dog&h1=iw'
url = 'https://www.google.com/search?q=cat&h1=iw'


driver.get(url)

# Wait for page to fully render
driver.implicitly_wait(.8)  

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the results div
results_div = soup.find('div', {'id': 'rso'})
#weather = soup.find('div', {'id': 'rso'})
weather = soup.find('div', {'data-ve-view': True})

forcast = []


def extract_last_div_with_attributes():
    # Find the last <div> element with attributes aria-level="2" and role="heading"
    last_div_element = None
    for div in reversed(soup.find_all('div', {'aria-level': '2', 'role': 'heading'})):
        last_div_element = div
        break
    c = 0
    if last_div_element:
        parent = last_div_element.parent
        while len(parent.find_all(recursive=False)) == 1 or c < 3:
            c+=1
            print(":::::::::::::",c)
            parent = parent.parent
        print(":::::::::::::xxx",c)

        return parent
        # Strip empty texts and combine all texts with "\n"
        text = "\n".join(filter(None, (x.strip() for x in parent.stripped_strings)))

        return text

    return None
    
extracted_text = extract_last_div_with_attributes()

if extracted_text:
    # Save the extracted text as 'info_v2.html'
    with open('info_v2.html', 'w', encoding='utf-8') as file:
        file.write(extracted_text.prettify())
    print("Saved 'info_v2.html' with extracted text.")
else:
    print("No suitable element found with the specified attributes.")    

print("DONE!")
exit()

def extract_info_from_html():
    result = {}

    # Parse the HTML content
    #soup = BeautifulSoup(html_content, 'html.parser')

    # Find the element with attribute data-attrid="title"
    title_element = soup.find('h2', {'data-attrid': 'title'})
    if title_element:
        result['title'] = title_element.text

    # Find the index of the last <h3> element on the page
    h3_elements = soup.find_all('h3')
    if h3_elements:
        last_h3_index = len(h3_elements) - 1

        # Find the text values of the next two <span> elements
        span_elements = soup.find_all('span')
        next_span_texts = []
        for i in range(last_h3_index + 1, last_h3_index + 3):
            if i < len(span_elements):
                next_span_texts.append(span_elements[i].text)

        if len(next_span_texts) == 2:
            result['description'] = next_span_texts[0]
            result['link'] = next_span_texts[1]

        # Find the index of the next <span> element
        next_span_index = last_h3_index + 3
        if next_span_index < len(span_elements):

            # Find the text content of all <div> elements between the two <span> elements and the span after them
            div_elements_between_spans = []
            for i in range(next_span_index, len(span_elements)):
                if span_elements[i].name == 'span':
                    break
                elif span_elements[i].name == 'div':
                    div_elements_between_spans.append(span_elements[i].text)

            result['extraInfoList'] = div_elements_between_spans

    return result



def find_last_h2_parent():
    # Parse the HTML content
    #soup = BeautifulSoup(html_content, 'html.parser')

    # Find the last <h2> element on the page and its index
    h2_elements = soup.find_all('h2')
    if h2_elements:
        last_h2_index = len(h2_elements) - 1
        last_h2_element = h2_elements[last_h2_index]

        # Walk backward through parent elements
        parent = last_h2_element
        skip = 6 + 2 #(+2 for margin, can be up to 4 or more)
        layers = 0
        lookfor = "גובה"
        while parent:
            if len(parent.find_all(recursive=False)) > 1 and (skip == 0):# or lookfor in parent.text):
                # If the parent has more than one child, return it prettified
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FOUND")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FOUND")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FOUND")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FOUND")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FOUND",layers,skip)
                return parent
            elif skip>0:
                layers += 1
                skip-=1
            parent = parent.parent

    return None  # Return None if no suitable parent is found

if weather:
    #results_html = results_div.prettify()
    results_html = weather.prettify()

    # Extract data here
    #print(results_html)
    results_html = weather.prettify()

    # Create a complete HTML document with head and body tags
    full_html = f"<!DOCTYPE html>\n<html>\n<head>\n"

    # Extract and include CSS links from the original HTML
    css_links = soup.find_all('link', rel='stylesheet')
    for link in css_links:
        css_url = link.get('href')
        if css_url and not css_url.startswith(('http:', 'https:')):
            # Make the CSS URL absolute by joining it with the base URL of the page
            base_url = 'https://www.google.com'  # Replace with the actual base URL
            css_url = urljoin(base_url, css_url)
            ##css_url = urljoin(url, css_url)


        # Fetch the CSS content
        css_response = requests.get(css_url)
        if css_response.status_code == 200:
            css_content = css_response.text

            # Include the CSS content in the HTML document
            #full_html += "<style>.boxx{width:400;height:400;positon:absolute;}"+f"{css_content}</style>"

    full_html += f"\n</head>\n<body><div class='boxx'>\n{results_html}\n</div></body>\n</html>"
    # Extract all aria-label attributes and print their values
    aria_label_values = [element.get('aria-label') for element in soup.find_all(attrs={'aria-label': True})]
    
    for value in aria_label_values:
        if value and "°" in value and value.split(" ")>1:
            print(value)
            forcast.append(value)
    # Save the HTML to a file
    with open('weather2.html', 'w', encoding='utf-8') as file:
        file.write(full_html)
    print("DONE!")


info = extract_info_from_html()

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n",info)
res = find_last_h2_parent()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n",res)
prettified_element=res
if prettified_element:
 # Get the original CSS styles by extracting and including CSS links in the head
    #css_links = soup.find_all('link', rel='stylesheet')
    #css_styles = [link.get('href') for link in css_links if link.get('href')]

    # Include the CSS links in the head of the prettified element
    head = soup.new_tag('head')
    #for css_style in css_styles:
        #link_tag = soup.new_tag('link', href=css_style, rel='stylesheet')
        #head.append(link_tag)
        
    prettified_element.insert_before(head)

    # Create a complete HTML document with html and body tags
    full_html = f"<!DOCTYPE html>\n<html>\n{prettified_element}\n</html>"

    # Save the HTML to a file
    with open('info.html', 'w', encoding='utf-8') as file:
        file.write(full_html)
    print("Saved 'info.html' with original CSS styles.")
    
    # Trim 'info.html' by removing content below the first element with aria-level
    soup = BeautifulSoup(full_html, 'html.parser')
    first_aria_level_element = soup.find(attrs={'aria-level': True})
    if first_aria_level_element:
        for tag in first_aria_level_element.find_all_next():
            tag.decompose()
            

    # Save the trimmed HTML to 'info.html'
    with open('info.htmlD', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print("Trimmed 'info.html' by removing content below the first element with aria-level.")

        
    # Filter out empty or whitespace-only <div> elements
    for div_element in soup.find_all('div'):
        if not div_element.text.strip():
            div_element.extract()

    # Save the trimmed HTML to 'info.html'
    with open('info_raw_dataD.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print("saved raw content")



print("FORCAST:")
for f in  forcast:
    print(f)



driver.quit()
