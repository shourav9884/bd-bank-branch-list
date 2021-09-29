import requests
import scrapy
from scrapy.http import TextResponse, XmlResponse
import json

def get_bank_list():
	return [{'slug': 'AB_BANK_LIMITED', 'bank_code': '020', 'name': 'AB BANK LIMITED'}, {'slug': 'AGRANI_BANK_LIMITED', 'bank_code': '010', 'name': 'AGRANI BANK LIMITED'}, {'slug': 'AL-ARAFAH_ISLAMI_BANK_LIMITED', 'bank_code': '015', 'name': 'AL-ARAFAH ISLAMI BANK LIMITED'}, {'slug': 'BANGLADESH_BANK', 'bank_code': '025', 'name': 'BANGLADESH BANK'}, {'slug': 'BANGLADESH_COMMERCE_BANK_LIMITED', 'bank_code': '030', 'name': 'BANGLADESH COMMERCE BANK LIMITED'}, {'slug': 'BANGLADESH_DEVELOPMENT_BANK_LIMITED', 'bank_code': '047', 'name': 'BANGLADESH DEVELOPMENT BANK LIMITED'}, {'slug': 'BANGLADESH_KRISHI_BANK', 'bank_code': '035', 'name': 'BANGLADESH KRISHI BANK'}, {'slug': 'BANGLADESH_SAMABAYA_BANK_LTD', 'bank_code': '040', 'name': 'BANGLADESH SAMABAYA BANK LTD'}, {'slug': 'BANGLADESH_SMALL_INDUSTRIES_AND_COMMERCE_BANK_LIMITED', 'bank_code': '055', 'name': 'BANGLADESH SMALL INDUSTRIES AND COMMERCE BANK LIMITED'}, {'slug': 'BANK_ALFALAH_LIMITED', 'bank_code': '065', 'name': 'BANK ALFALAH LIMITED'}, {'slug': 'BANK_ASIA_LIMITED', 'bank_code': '070', 'name': 'BANK ASIA LIMITED'}, {'slug': 'BASIC_BANK_LTD', 'bank_code': '055', 'name': 'BASIC BANK LTD'}, {'slug': 'BRAC_BANK_LIMITED', 'bank_code': '060', 'name': 'BRAC BANK LIMITED'}, {'slug': 'CITIBANK_N.A', 'bank_code': '075', 'name': 'CITIBANK N.A'}, {'slug': 'COMMERCIAL_BANK_OF_CEYLON_LIMITED', 'bank_code': '080', 'name': 'COMMERCIAL BANK OF CEYLON LIMITED'}, {'slug': 'DHAKA_BANK_LIMITED', 'bank_code': '085', 'name': 'DHAKA BANK LIMITED'}, {'slug': 'DUTCH-BANGLA_BANK_LIMITED', 'bank_code': '090', 'name': 'DUTCH-BANGLA BANK LIMITED'}, {'slug': 'EASTERN_BANK_LIMITED', 'bank_code': '095', 'name': 'EASTERN BANK LIMITED'}, {'slug': 'EXIM_BANK_LTD', 'bank_code': '100', 'name': 'EXIM BANK LTD'}, {'slug': 'EXPORT_IMPORT_BANK_OF_BANGLADESH_LIMITED', 'bank_code': '100', 'name': 'EXPORT IMPORT BANK OF BANGLADESH LIMITED'}, {'slug': 'FIRST_SECURITY_ISLAMI_BANK_LIMITED', 'bank_code': '105', 'name': 'FIRST SECURITY ISLAMI BANK LIMITED'}, {'slug': 'HABIB_BANK_LIMITED', 'bank_code': '110', 'name': 'HABIB BANK LIMITED'}, {'slug': 'HONGKONG_AND_SHANGHAI_BANKING_CORP', 'bank_code': '115', 'name': 'HONGKONG AND SHANGHAI BANKING CORP'}, {'slug': 'ICB_ISLAMIC_BANK_LIMITED', 'bank_code': '230', 'name': 'ICB ISLAMIC BANK LIMITED'}, {'slug': 'INTERNATIONAL_FINANCE_INVEST_AND_COMMERCE_BANK_LIMITED', 'bank_code': '120', 'name': 'INTERNATIONAL FINANCE INVEST AND COMMERCE BANK LIMITED'}, {'slug': 'ISLAMI_BANK_BANGLADESH_LIMITED', 'bank_code': '125', 'name': 'ISLAMI BANK BANGLADESH LIMITED'}, {'slug': 'JAMUNA_BANK_LIMITED', 'bank_code': '130', 'name': 'JAMUNA BANK LIMITED'}, {'slug': 'JANATA_BANK_LIMITED', 'bank_code': '135', 'name': 'JANATA BANK LIMITED'}, {'slug': 'MEGHNA_BANK_LIMITED', 'bank_code': '0', 'name': 'MEGHNA BANK LIMITED'}, {'slug': 'MERCANTILE_BANK_LIMITED', 'bank_code': '140', 'name': 'MERCANTILE BANK LIMITED'}, {'slug': 'MODHUMOTI_BANK_LIMITED', 'bank_code': '0', 'name': 'MODHUMOTI BANK LIMITED'}, {'slug': 'MUTUAL_TRUST_BANK_LIMITED', 'bank_code': '145', 'name': 'MUTUAL TRUST BANK LIMITED'}, {'slug': 'NA', 'bank_code': '050', 'name': 'NA'}, {'slug': 'NATIONAL_BANK_LIMITED', 'bank_code': '150', 'name': 'NATIONAL BANK LIMITED'}, {'slug': 'NATIONAL_BANK_OF_PAKISTAN', 'bank_code': '155', 'name': 'NATIONAL BANK OF PAKISTAN'}, {'slug': 'NATIONAL_CREDIT_&_COMMERCE_BANK_LIMITED', 'bank_code': '160', 'name': 'NATIONAL CREDIT &amp; COMMERCE BANK LIMITED'}, {'slug': 'NRB_BANK_LIMITED', 'bank_code': '0', 'name': 'NRB BANK LIMITED'}, {'slug': 'NRB_COMMERCIAL_BANK_LIMITED', 'bank_code': '0', 'name': 'NRB COMMERCIAL BANK LIMITED'}, {'slug': 'NRB_GLOBAL_BANK_LIMITED', 'bank_code': '0', 'name': 'NRB GLOBAL BANK LIMITED'}, {'slug': 'OFFICE_OF_THE_CONTROLLER_GENERAL__OF_ACCOUNTS', 'bank_code': '405', 'name': 'OFFICE OF THE CONTROLLER GENERAL  OF ACCOUNTS'}, {'slug': 'ONE_BANK_LIMITED', 'bank_code': '165', 'name': 'ONE BANK LIMITED'}, {'slug': 'PRIME_BANK_LIMITED', 'bank_code': '170', 'name': 'PRIME BANK LIMITED'}, {'slug': 'PUBALI_BANK_LIMITED', 'bank_code': '175', 'name': 'PUBALI BANK LIMITED'}, {'slug': 'RAJSHAHI_KRISHI_UNNAYAN_BANK', 'bank_code': '180', 'name': 'RAJSHAHI KRISHI UNNAYAN BANK'}, {'slug': 'RUPALI_BANK_LIMITED', 'bank_code': '185', 'name': 'RUPALI BANK LIMITED'}, {'slug': 'SHAHJALAL_ISLAMI_BANK_LIMITED', 'bank_code': '190', 'name': 'SHAHJALAL ISLAMI BANK LIMITED'}, {'slug': 'SOCIAL_ISLAMI_BANK_LIMITED', 'bank_code': '195', 'name': 'SOCIAL ISLAMI BANK LIMITED'}, {'slug': 'SONALI_BANK_LIMITED', 'bank_code': '200', 'name': 'SONALI BANK LIMITED'}, {'slug': 'SOUTHEAST_BANK_LIMITED', 'bank_code': '205', 'name': 'SOUTHEAST BANK LIMITED'}, {'slug': 'SOUTH_BANGLA_AGRICULTURE_AND_COMMERCE_BANK_LIMITED', 'bank_code': '0', 'name': 'SOUTH BANGLA AGRICULTURE AND COMMERCE BANK LIMITED'}, {'slug': 'STANDARD_BANK_LIMITED', 'bank_code': '210', 'name': 'STANDARD BANK LIMITED'}, {'slug': 'STANDARD_CHARTERED_BANK', 'bank_code': '215', 'name': 'STANDARD CHARTERED BANK'}, {'slug': 'STATE_BANK_OF_INDIA', 'bank_code': '220', 'name': 'STATE BANK OF INDIA'}, {'slug': 'THE_CITY_BANK_LIMITED', 'bank_code': '225', 'name': 'THE CITY BANK LIMITED'}, {'slug': 'THE_FARMERS_BANK_LIMITED', 'bank_code': '0', 'name': 'THE FARMERS BANK LIMITED'}, {'slug': 'THE_HONGKONG_AND_SHANGHAI_BANKING_CORPORATION_LIMITED', 'bank_code': '115', 'name': 'THE HONGKONG AND SHANGHAI BANKING CORPORATION LIMITED'}, {'slug': 'THE_PREMIER_BANK_LIMITED', 'bank_code': '235', 'name': 'THE PREMIER BANK LIMITED'}, {'slug': 'TRUST_BANK_LIMITED', 'bank_code': '240', 'name': 'TRUST BANK LIMITED'}, {'slug': 'UNION_BANK_LIMITED', 'bank_code': '0', 'name': 'UNION BANK LIMITED'}, {'slug': 'UNITED_COMMERCIAL_BANK_LIMITED', 'bank_code': '245', 'name': 'UNITED COMMERCIAL BANK LIMITED'}, {'slug': 'UTTARA_BANK_LIMITED', 'bank_code': '250', 'name': 'UTTARA BANK LIMITED'}, {'slug': 'WOORI_BANK_BANGLADESH', 'bank_code': '255', 'name': 'WOORI BANK BANGLADESH'}]

def get_district_list(bank_slug, bank_code):
	url = "http://thecodes.us/BANGLADESH/{}/{}".format(bank_slug, bank_code)
	response = requests.get(url)
	response = TextResponse(body=response.content, url=url)
	option_list = response.css('select')[1].css('option').extract()
	i=0 
	data = []
	for option in option_list:
		if i==0:
			i += 1
			continue
		if option.startswith('<option value="{}/'.format(url)):	
			option = option.replace('<option value="{}/'.format(url), '')	
			option = option.replace('</option>', '')
			option = option.replace('">', '/')
			d_list = option.split('/')
			data.append({"district_name": d_list[0]})
		i += 1
	return data

def get_branch_list(bank_slug, bank_code, district):
	url = "http://thecodes.us/BANGLADESH/{}/{}/{}".format(bank_slug, bank_code, district)
	print("district: {}".format(url))
	response = requests.get(url)
	response = TextResponse(body=response.content, url=url)
	option_list = response.css('select')[2].css('option').extract()
	i=0 
	data = []
	temp_url="http://thecodes.us/BANGLADESH/{}/{}".format(bank_slug, district)
	for option in option_list:
		if i==0:
			i += 1
			continue
		option = option.replace('<option value="{}/'.format(temp_url), '')	
		option = option.replace('</option>', '')
		option = option.replace('">', '/')
		d_list = option.split('/')
		data.append({"routing_number": d_list[1], "branch_name": d_list[2], 'branch_slug': d_list[0]})
		i += 1
	return data

def get_branch_details(bank_slug, district, branch_slug, routing_number):
	url = "http://thecodes.us/BANGLADESH/{}/{}/{}/{}".format(bank_slug, district, branch_slug, routing_number)
	print("branch: {}".format(url))
	response = requests.get(url)
	response = TextResponse(body=response.content, url=url)
	info_list = ['branch_code', 'swift_code', 'address', 'telephone', 'email', 'fax']
	data = {}
	for i in range(0, len(info_list)):
		if len(response.css('tr')) >= 6+i:
			d = response.css('tr')[5+i].css('td')[1].extract()
			d = d.replace('<td style="padding: 6px;">', '')
			d = d.replace('</td>', '')
			data[info_list[i]] = d
	return data	 


def scrape():
	bank_list = get_bank_list()
	result = []
	for bank in bank_list:
		districts = get_district_list(bank['slug'], bank['bank_code'])
		bank['districts'] = []
		for district in districts:
			branches = get_branch_list(bank['slug'], bank['bank_code'], district['district_name'])
			district['branches'] = []
			for branch in branches:
				details = get_branch_details(bank['slug'], district['district_name'], branch['branch_slug'], branch['routing_number'])
				for k,v in details.items():
					branch[k] = v
				district['branches'].append(branch)
			bank['districts'].append(district)
		result.append(bank)
		print("===bank done: {}".format(bank['slug']))
	return result
# print(get_district_list('AB_BANK_LIMITED', '020'))
data = scrape()
with open('bank_data.json', 'w+') as data_file:
	 json.dump(data, data_file, indent=4)




