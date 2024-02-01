import requests

# Your Cloudflare API tokens for each account
api_tokens = ['your_api_token_here_account_1', 'your_api_token_here_account_2', ...]

# Header for authentication
headers_template = {
    'Authorization': 'Bearer {}',
    'Content-Type': 'application/json'
}

def list_domains(api_token):
    headers = headers_template.copy()
    headers['Authorization'] = headers['Authorization'].format(api_token)
    domains = []
    page = 1
    while True:
        try:
            response = requests.get(f'https://api.cloudflare.com/client/v4/zones?page={page}&per_page=50', headers=headers)
            response.raise_for_status()
            data = response.json()
            domains.extend(data['result'])
            if not data['result_info']['has_more']:
                break
            page += 1
        except requests.exceptions.RequestException as e:
            print(f"Error fetching domains for token ending in {api_token[-4:]}: {e}")
            break
    return domains

def find_flattened_cnames(api_token, domain):
    headers = headers_template.copy()
    headers['Authorization'] = headers['Authorization'].format(api_token)
    cnames = []
    try:
        response = requests.get(f'https://api.cloudflare.com/client/v4/zones/{domain["id"]}/dns_records?type=CNAME', headers=headers)
        response.raise_for_status()
        for record in response.json()['result']:
            if record['name'] == domain['name']:  # Checking if it's an Apex record
                cnames.append(record)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching DNS records for {domain['name']}: {e}")
    return cnames

flattened_cnames = []
for token in api_tokens:
    for domain in list_domains(token):
        flattened_cnames.extend(find_flattened_cnames(token, domain))

# Saving the results in markdown format
with open('flattened_cnames.md', 'w') as file:
    file.write('| Domain | CNAME Record |\n')
    file.write('| ------ | ------------ |\n')
    for cname in flattened_cnames:
        file.write(f"| {cname['name']} | {cname['content']} |\n")

print("Flattened CNAME records saved to flattened_cnames.md")