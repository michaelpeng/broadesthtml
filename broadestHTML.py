from lxml import html
import requests
import cssselect
import operator

def main():
	TOPELEMENTS = 1 					# Change to print the TOPELEMENTS most frequent elements, defaults to 1

	url_input = raw_input("Enter the URL (format e.g. 'google.com' etc): ")
	page = requests.get('http://'+str(url_input))
	
	tree_format = html.fromstring(page.text)
	elements = tree_format.cssselect('div')

	unique_elements = set()
	elements_dict = {}

	for item in elements:				# iterate through each list in elements
		for eachtuple in item.items():	# iterate through each tuple in each accessed list in elements
			element_type = eachtuple[0]
			if element_type == 'class':
				element_name = eachtuple[1] #
				if element_name not in unique_elements:
					unique_elements.add(element_name)
					elements_dict[element_name] = 1
				else:
					elements_dict[element_name] += 1

	sorted_dict = sorted(elements_dict.items(), key=operator.itemgetter(1), reverse=True)

	num_of_classes = len(sorted_dict) 	# in case there are fewer than TOPELEMENTS number of classes
	if num_of_classes < TOPELEMENTS:
		TOPELEMENTS = num_of_classes

	if TOPELEMENTS == 1:
		print "Most common class: " + sorted_dict[0][0] + ", with " + str(sorted_dict[0][1]) + " appearances."

	else:
		print "Top " + str(TOPELEMENTS) + " most common classes:"
		for i in range (0, TOPELEMENTS):
			print "Number " + str(i+1) + ": " + sorted_dict[i][0] + ", with " + str(sorted_dict[i][1]) + " appearances."

main()