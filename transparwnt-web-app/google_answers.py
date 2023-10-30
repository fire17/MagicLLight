from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
### IMPORTS Done

options = Options() 
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
lang="en"

import time

### DATA FALLBACK

def find_time(soup):
    # with rso first div inside
    return None


# how tall is mount everest <block-component>
# extra - check dates, pie, more quick questions,
# what is the size of the earth wa:/description, 
    
# implement    
find_block_component, find_wa_desc, find_extra = (lambda soup: None for _ in range(3))


# find title
#~~~~~~~~~
def getTitle(soup):
    title_element = soup.find('h2', {'data-attrid': 'title'})
    if title_element:
        print("TTTTTTTTTTTTTTTTTTTT",title_element.text)
        return title_element.text
    else:
        print("NNNNNNNN NO TITLE found using h2")
        return None

#title = getTitle()

# how tall is mount everest <block-component>
# extra - check dates, pie, more quick questions,
# what is the size of the earth wa:/description, 



# find top info
#url = 'https://www.google.com/search?q=cat&h1=iw'
def find_top(soup, saveFile=False):
    # Find the last <div> element with attributes aria-level="2" and role="heading"
    last_div_element = None
    for div in reversed(soup.find_all('div', {'aria-level': '2', 'role': 'heading'})):
        last_div_element = div
        break
    c = 0
    foundParent = None
    if last_div_element:
        parent = last_div_element.parent
        while len(parent.find_all(recursive=False)) == 1 or c < 3:
            c+=1
            #print(":::::::::::::",c)
            parent = parent.parent
        #print(":::::::::::::xxx",c)

        if parent:
            foundParent = parent
        ## Strip empty texts and combine all texts with "\n"
        #text = "\n".join(filter(None, (x.strip() for x in parent.stripped_strings)))
        #
        #return text
    if saveFile:    
        if foundParent:
            # Save the extracted text as 'info_v2.html'
            with open('info_v2.html', 'w', encoding='utf-8') as file:
                file.write(foundParent.prettify())
            print("Saved 'info_v2.html' with extracted text.")
        else:
            print("No suitable element found with the specified attributes.")    
    data = {}

    # Find description - first <div> under file-attachment-contents
    title = [div for div in soup.find_all('div', {'data-attrid': "title"})][0].stripped_strings
    title = '\n'.join(title)
    print("XXXX")
    print(title)
    print("XXXX")
    data["title"]=title
    #data['description'] = description 
    #desc_div = "\n".join(list(soup.find('div', {'data-md': "50"})[0]).stripped_strings[:-1])
    #print("XXXXXXXXXXXXXXX")
    #print(desc_div)
    #print("XXXXXXXXXXXXXXX")
    divs_with_data = [div for div in soup.find_all('div', {'style': "clear:none"})]
    # Print the list of <div> elements with the "lang" attribute
    final = []
    print("----------------",len(divs_with_data))
    c = 0
    stop = False
    #data = {}
    got_data = False
    got_desc = False
    for div in divs_with_data[::-1]:
        c+=1
        #print("!!!",div.prettify())
        #final.append(div.prettify())
        #print("!!!",div.text)
        #final.append(div.text)
        multi_line_text = '\n'.join(div.stripped_strings)
        print("_ _ _", multi_line_text,"_ _ _")
        stripped = list(div.stripped_strings)
        if len(stripped) >= 2 and ":" in stripped[1] and not got_desc:
            #data[stripped[0]]='\n'.join(stripped[2:])
            final.append((stripped[0],' '.join(stripped[2:]).replace("\xa0"," ")))
            got_data = True
        elif got_data and len(stripped)>2 and not got_desc:
            data["description"]=stripped[1]
            got_desc = True
    for pack in final[::-1]:
        data[pack[0]]=pack[1]
    
    
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%","\n".join(list(data.keys())),"\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%","\n".join(list((data[k] for k in data.keys()))),"\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    return data        
    
    # Find fact rows - <div> elements under <div> elements 
    rows = soup.find('file-attachment-contents').find_all('div')
    for row in rows:
        label = row.find('a').text
        value = row.find('span').text
        print("xxxxxxxxxxxxxxxxx",label,value)
        data[label] = value

    print(data)
    print("DONE DOG/CAT!")
    
    time.sleep(10)
    return foundParent
    
#extracted_text = find_top()


        

# find left info
#url = 'https://www.google.com/search?q=everest&h1=iw'

############ Left with pictures
def find_left(soup, saveFile=False):
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
    if result and saveFile:
        info = result
        head = soup.new_tag('head')
        
        info.insert_before(head)

        # Create a complete HTML document with html and body tags
        full_html = f"<!DOCTYPE html>\n<html>\n{info}\n</html>"

        # Save the HTML to a file
        with open('info.html', 'w', encoding='utf-8') as file:
            file.write(full_html)
        print("Saved 'info.html' with original CSS styles.")
        
    return result

#info = find_left()
    
    
############ RAW TEXT
def find_left_raw(soup):
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

        return None 
    res = find_last_h2_parent()
    #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n",res)
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
        
        # get all divs with lang
        divs_with_lang = [div for div in soup.find_all('div', {'lang': True})]
        # Print the list of <div> elements with the "lang" attribute
        final = []
        c = 0
        stop = False
        data = {}
        for div in divs_with_lang:
            c+=1
            #print("!!!",div.prettify())
            #final.append(div.prettify())
            #print("!!!",div.text)
            #final.append(div.text)
            multi_line_text = '\n'.join(div.stripped_strings)
            #!!!print("!!!", multi_line_text)
            if c==1:
                multi_line_text = multi_line_text.split("\n")[:3]
                final.append(multi_line_text)
                
            if c==2:
                pass # skipp bullshit
                
            
            if c==3:
                if len(multi_line_text.split("\n")) == 3:
                    final.append(multi_line_text).split("\n")[1].replace("\xa0"," ")
                else:
                    final.append(multi_line_text.replace("\xa0"," "))
            if c>=4:
                if len(multi_line_text.split("\n"))>1:
                    if ":" not in multi_line_text.split("\n")[1]:
                        stop = True
                if not stop:
                    m = multi_line_text.replace("\xa0"," ")
                    print("OOO",m)
                    print(":::",[m])
                    print("!!!!!",m.split("\n:\n"))
                    print("KEY",m.split("\n:\n")[0])
                    print("VAL",m.split("\n:\n")[1])
                    KEY, VAL = m.split("\n:\n")[0], m.split("\n:\n")[1]
                    print("XXXXXXXXXX",[KEY])
                    print("XXXXXXXXXX",[VAL])
                    data[KEY] = VAL
                    #final.append([KEY,VAL])
                    #final.append([multi_line_text[0],multi_line_text[1]])
                    #final.append(multi_line_text.replace("\n"," "))
        for res in final:
            print("!!!@@@@@@@@@@@!!!!!!!!!", [res])  
        for key in data:
            print(key,"vvvvvvvvv", data[key])
        data["title"] = final[0][0]
        data["short_desc"] = final[0][-1]
        data["description"] = final[1]
        return data
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
        return {"title":final[0][0],"short_desc":final[0][-1],"description":final[1],"data":data}
        
        return final
        return soup.prettify()
    return None
################ DONE LEFT


# find weather
def get_weather_forcast(soup, saveFile=True, savePath='weather3.html'):
	weather = soup.find('div', {'data-ve-view': True})
	forcast = []
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
		days = {}
		#started = False
		lastDay = False, ""
		#createdNextWeek = False
		#gettingPerc = False
		delemeter = "°"
		week = {}
		post = ""
		changeOnce = False
		for value in aria_label_values:
        
			if value and "°" in value and len(value.split(" "))>1:
				#if "°" not in value and not gettingPerc:
				#	gettingPerc = True
				#	lastDay = False, ""
				#	delemeter = "%"
				#	lastDay = False, ""
				#	createdNextWeek=False
                #    week = {}

				print("")
				print("---",value)
				#started = True
				#print(value)
				#forcast.append(value)
				d, val = " ".join(value.split(" ")[1:]).strip(),value.split(" ")[0]
				ds = d.split(" ")
				day, hour = " ".join(ds[:-1]),ds[-1]
				KEY, VAL = val.split(delemeter)[1] if delemeter == "°" else "precipitation",val.split(delemeter)[0]
				
				if lastDay[0] and day != lastDay[1]:
					post = " (Next Week)"
					print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",day+post)
					#finalDay=day
                
				week[day+post] = {}
				if len(week.keys()) <= 10:			
					if day+post not in days:
						days[day+post] = {}
						                        
					if hour in days[day+post]:
						days[day+post][hour][KEY] = VAL
					else:
						days[day+post][hour]={KEY:VAL}
					#time.sleep(0.1)
					print("DAY\n",day+post,"\nHOUR",hour,"\nKEY",KEY,"\n","VAL",VAL)
				if not lastDay[0] and len(week.keys())==7:
					lastDay = True, day
					print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",days.keys())
					
				
			elif value and "%" in value and len(value.split(" "))>1:
				print("SSSSSSSSSS",value)
				if not changeOnce:
					changeOnce = True
					delemeter = "%"
					lastDay = False, ""
					week={}		
					post=''		
				
				d, val = " ".join(value.split(" ")[1:]).strip(),value.split(" ")[0]
				ds = d.split(" ")
				day, hour = " ".join(ds[:-1]),ds[-1]
				KEY, VAL = "precipitation",val.split(delemeter)[0]
				
				if lastDay[0] and day != lastDay[1]:
					post = " (Next Week)"
					print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",day+post)
					#finalDay=day
                
				week[day+post] = {}
				if len(week.keys()) <= 10:			
					if day+post not in days:
						days[day+post] = {}
						                        
					if hour in days[day+post]:
						days[day+post][hour][KEY] = VAL
					else:
						days[day+post][hour]={KEY:VAL}
					#time.sleep(0.1)
					print("DAY\n",day+post,"\nHOUR",hour,"\nKEY",KEY,"\n","VAL",VAL)
				if not lastDay[0] and len(week.keys())==7:
					lastDay = True, day
					print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",days.keys())
				
				
				
				
				
			#print("add wind and rain....")
		if saveFile:
			# Save the HTML to a file
			with open(savePath, 'w', encoding='utf-8') as file:
				file.write(full_html)
		print("DONE!")
		return days
		return forcast

urls = []
urls.append( 'https://www.google.com/search?q=%D7%9E%D7%96%D7%92+%D7%90%D7%95%D7%95%D7%99%D7%A8+%D7%94%D7%A8%D7%A6%D7%9C%D7%99%D7%94')
urls.append( 'https://www.google.com/search?q=is+it+going+to+rain+tomorrow+&hl=iw')
urls.append( 'https://www.google.com/search?q=is+it+going+to+rain+tomorrow+&hl=iw')
urls.append( 'https://www.google.com/search?q=what+is+mount+everest&hl=iw')
urls.append( 'https://www.google.com/search?q=what+is+a+dog&oq=what+is+a+dog&h1=iw')
urls.append( 'https://www.google.com/search?q=what+is+a+dog&h1=iw')
urls.append( 'https://www.google.com/search?q=cat&h1=iw')
#("what is a dog",find_top)
#tests = [["cat",find_top],["what is mount everest",find_left_raw],["weather in Herzelia",get_weather_forcast]]
tests = [["what is mount everest",find_left_raw],] # PASS !
tests = [["what is a dog",find_top],] # PASS !
tests = [["weather in Herzelia",get_weather_forcast]] # PASS !
def google_answers(q=None, lang='en', url=None, func=None, tests =None, retSuc=True):
    if isinstance(url,list):
        for url in urls[::-1]:
            print("::: STARTING TEST :::",url)
            return google_answers(url=url)
    if tests:
        for s in tests:
            f= None
            if isinstance(s, list):
                s,f = s
            print("::: STARTING TEST :::",s,f)
            return google_answers(q=s,func =f)
    elif url is None:
        url = 'https://google.com/search?q='+q.replace(" ","+")+str(f'&h1={lang}' if lang is not None else '')
    print(q if q else "", lang if lang else "", ":::", url)
    ### GET SOUP (selenium)
    driver.get(url)

    # Wait for page to fully render
    #driver.implicitly_wait(.8)  

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    options = [find_block_component, find_wa_desc, find_extra, find_top, find_left, find_left_raw, get_weather_forcast, find_time  ]    
    title = getTitle(soup)
    t = 0
    results = []
    if func :
        options = [func]
        print("...........SHOULD BE ONE!")
    for test in options:
        t+=1
        res = test(soup)
        print("::::::::::::::::::TEST",t)
        if res:
            print("SUCCESS!!!!!",res)
            results.append(res)
            if retSuc:
                return res
        else:
            print("FAILED",res)
        print("::::::::::::::::::TEST",t)
    return results
    
results = google_answers(tests = tests)        
print("##############################", len(results))
print(results)
print("##############################")
for key in results:
    print(key)

#find_weather, find_time

# find (time)
#rso first div inside 




# TODO:
# - format , then others
