# --- Importing Libraries ---
import pandas as pd
import requests

# ---

# --- Setting Parameters for the API Request ---
params = {"page": 1, "per_page": 25}

# ---

# --- API request and handling ---
response = requests.get("https://www.peeringdb.com/api/net", params=params, timeout=30)

data = response.json()


print(response.status_code)
# ---

# --- json file exploration ---
#print(data.keys())
#print(data["data"])
#print(len(data["data"]))
#print(data["data"][0]) 
# ---


# Loading payload into Pandas
dataextract = data["data"]

df = pd.json_normalize(dataextract)


# --- dataframe exploration ---
#print(df.shape)
#print(df.columns)
print(df.info())
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