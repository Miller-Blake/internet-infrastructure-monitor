# --- Importing Libraries ---
import pandas as pd
import requests

# ---

# --- Setting Parameters for the API Request ---
params = {"page": 1, "per_page": 25}

# ---

# --- API request and handling ---
def get_api_data_pull(url, params=None, timeout=30):

    try:
        res = requests.get(url, params=params, timeout=timeout)
        res.raise_for_status()
        pulled_data = res.json()
        return pulled_data
    
    except requests.exceptions.Timeout:
        print("Timed Out")
        return None

    except requests.exceptions.ConnectionError:
        print('Connectivity Error')
        return None
    
    except requests.exceptions.HTTPError:
        print('HTTPError')
        return None
    
    except requests.exceptions.JSONDecodeError:
        print('Error decoding the JSON file')
        return None


network_data = get_api_data_pull("https://www.peeringdb.com/api/net",params)
ix_data = get_api_data_pull("https://www.peeringdb.com/api/ix/33")

#print(response.status_code)
#print(ix_response.status_code)

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
network_dataextract = network_data["data"]
ix_dataextract = ix_data["data"]

network_df = pd.json_normalize(network_dataextract)
ix_df = pd.json_normalize(ix_dataextract)

fac_set_df = pd.json_normalize(ix_dataextract[0]["fac_set"])
ixlan_set_df = pd.json_normalize(ix_dataextract[0]["ixlan_set"])

print(fac_set_df.head())
print(ixlan_set_df.head())
# ---

# --- dataframe exploration ---
#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df.isna().sum())
#print(df.describe())
#print(df["notes"].head(10))
#print(df["looking_glass"].head(10))
#print(df[['policy_general', 'policy_locations', 'policy_url', 'policy_ratio', 'policy_contracts']].head(10))
#print(df[["name", "asn", "ix_count", "fac_count"]].head(25))

#print(ix_df.iloc[0].to_string())
#print(ix_df["fac_set"])
#print(ix_df["ixlan_set"])
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