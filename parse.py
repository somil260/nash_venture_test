from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict


driver = webdriver.Firefox()
url1 = 'http://www.tennisabstract.com/cgi-bin/wplayer.cgi?p=MariaSharapova'
url2 = 'http://www.tennisabstract.com/cgi-bin/wplayer.cgi?p=MariaSharapova&f=r1'
lst = list()

driver.get(url1)
table_body = driver.find_element_by_xpath("//*[@id='matches']//tbody")
table_row = table_body.find_elements_by_tag_name("tr")[:10]
for row in table_row:
	data = OrderedDict({
		"ace": row.find_elements_by_tag_name("td")[9].text,
		"first_serve": row.find_elements_by_tag_name("td")[12].text,
		"second_serve": row.find_elements_by_tag_name("td")[13].text,
		})
	lst.append(data)


driver.get(url2)
table_body = driver.find_element_by_xpath("//*[@id='matches']//tbody")
table_row = table_body.find_elements_by_tag_name("tr")[:10]
for i, row in enumerate(table_row):
	rpw = row.find_elements_by_tag_name("td")[10].text
	lst[i].update({'rpw': rpw})

print(lst)
