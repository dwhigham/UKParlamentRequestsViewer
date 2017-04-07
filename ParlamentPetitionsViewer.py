import requests

url = "https://petition.parliament.uk/petitions/180642.json"
#url = "https://petition.parliament.uk/petitions/131215.json"

def main():
	response = requests.request("GET", url)
	outside_gb_count = 0;
	#print(response.text)
	for country in response.json()['data']['attributes']['signatures_by_country']:

		if country['code'] != 'GB':
			outside_gb_count += country['signature_count']

	print ('{} votes outside GB' .format(outside_gb_count))

	from_scot_count = 0
	from_eng_count = 0
	from_wal_count = 0 
	from_irl_count = 0
	
	for constituency in response.json()['data']['attributes']['signatures_by_constituency']:

		if constituency['ons_code'][:1] == 'S':
			from_scot_count += constituency['signature_count']

	print ('{} votes from Scotland' .format(from_scot_count))

	for constituency in response.json()['data']['attributes']['signatures_by_constituency']:

		if constituency['ons_code'][:1] == 'E':
			from_eng_count += constituency['signature_count']

	print ('{} votes from England' .format(from_eng_count))

	for constituency in response.json()['data']['attributes']['signatures_by_constituency']:

		if constituency['ons_code'][:1] == 'W':
			from_wal_count += constituency['signature_count']

	print ('{} votes from Wales' .format(from_wal_count))

	for constituency in response.json()['data']['attributes']['signatures_by_constituency']:

		if constituency['ons_code'][:1] == 'N':
			from_irl_count += constituency['signature_count']

	print ('{} votes from NI' .format(from_irl_count))

	
	print ('{} votes in TOTAL' .format(from_scot_count + from_eng_count + from_wal_count + from_irl_count + outside_gb_count))



if __name__ == "__main__":
    main()
