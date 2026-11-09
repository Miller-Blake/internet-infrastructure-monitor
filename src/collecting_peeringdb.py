# --- Importing Libraries ---
import pandas as pd
import requests
import time

# ---

# --- Setting Parameters for the API Request ---

#Currently undefined
#params = {"page": 1, "per_page": 200}

# ---

# --- API request and handling ---
def get_api_data_pull(url, params=None, timeout=30):

    
    attempt = 0
    attempt_retry = [2, 4, 8]

        
    for attempt, delay in enumerate(attempt_retry):

        try:
            res = requests.get(url, params=params, timeout= .00001)

            res.raise_for_status()

            pulled_data = res.json()
            
            return pulled_data
        
            
        except requests.exceptions.Timeout as err:
            print(f"Error: {err}")
            print(f"Attempt {attempt + 1} failed. Waiting {delay} seconds.")
            continue

        except requests.exceptions.ConnectionError as err:
            print(f'Error: {err}')
            print(f"Attempt {attempt + 1} failed. Waiting {delay} seconds.")
            return None
    
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Status Code: {err.response.status_code}")
            print(f"Error Details: {err}")
            return None
    
        except requests.exceptions.JSONDecodeError as err:
            print(f'Error: {err}')
            return None
    else:
        print("Failed Retry Protocol")
        
        return None


#network_data = get_api_data_pull("https://www.peeringdb.com/api/net",params)

#requires ID after 'ix/'
#ix_data = get_api_data_pull("https://www.peeringdb.com/api/ix/33")

has_next = True
page = 1
network_data = []

# Automated Extract of Network Data
while has_next:

    params = {'page': page, "per_page":200}
    time.sleep(2)
    data_get = get_api_data_pull("https://www.peeringdb.com/api/net",params)

    if data_get is None:
        print(f"Collection failed on page {page}")
        break

    network_data.extend(data_get['data'])

    has_next = data_get['meta']['pagination']['has_next']

    page += 1


# ---

# --- json file exploration ---

#print(data.keys())
#print(ix_data.keys())
def examine_json(json):
    print(json["data"])
    print(len(json["data"]))
    print(json["data"][0])

#examine_json(data)
#examine_json(ix_data)

# ---


# --- Loading payload into Pandas ---

#ix_dataextract = ix_data["data"]

#Full Dataframe
network_df = pd.json_normalize(network_data)


#Singular ID Dataframes
#ix_df = pd.json_normalize(ix_dataextract)
#fac_set_df = pd.json_normalize(ix_dataextract[0]["fac_set"])
#ixlan_set_df = pd.json_normalize(ix_dataextract[0]["ixlan_set"])

# ---

# --- dataframe exploration ---

print(len(network_data))
print(network_df.shape)
print(network_df.head())

# ---

### --- The following are the column names - 42 Total Columns ---
#['id', 'org_id', 'name', 'aka', 'name_long', 'website', 'social_media',
#'asn', 'looking_glass', 'route_server', 'irr_as_set', 'info_type', 
#'info_types', 'info_prefixes4', 'info_prefixes6', 'info_traffic',
#'info_ratio', 'info_scope', 'info_unicast', 'info_multicast',
#'info_ipv6', 'info_never_via_route_servers', 'ix_count', 'fac_count',
#'notes', 'netixlan_updated', 'netfac_updated', 'poc_updated',
#'policy_url', 'policy_general', 'policy_locations', 'policy_ratio',
#'policy_contracts', 'allow_ixp_update', 'ixp_update_exclude',
#'status_dashboard', 'rir_status', 'rir_status_updated', 'logo',
#'created', 'updated', 'status']
# ---