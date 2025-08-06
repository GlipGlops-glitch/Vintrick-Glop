# vintrick-backend/tools/export_ad_users.py
# Export enabled AD users to CSV (filters out disabled accounts)

import csv
from ldap3 import Server, Connection, ALL, NTLM

# === CONFIGURE THESE VALUES ===
AD_SERVER = "stemichelle.ustis.com"           # Or a specific DC, e.g. dc01.stemichelle.ustis.com
AD_DOMAIN = "STEMICHELLE"                     # Confirm with 'echo %USERDOMAIN%' on your PC
AD_USER = "CAH01"
AD_PASSWORD = "Welcome12!"
AD_SEARCH_BASE = "DC=stemichelle,DC=ustis,DC=com"

# LDAP filter to select enabled user accounts (exclude disabled accounts)
# userAccountControl:1.2.840.113556.1.4.803:=2 means the DISABLED flag is set; !(...) means NOT disabled.
ldap_filter = "(&(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"

# Connect to the AD server
server = Server(AD_SERVER, get_info=ALL)
conn = Connection(
    server,
    user=f"{AD_DOMAIN}\\{AD_USER}",
    password=AD_PASSWORD,
    authentication=NTLM,
    auto_bind=True
)

# Search for enabled users only
conn.search(
    AD_SEARCH_BASE,
    ldap_filter,
    attributes=["sAMAccountName", "displayName", "mail"]
)

# Write results to CSV
with open("ad_users.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["username", "display_name", "email"])
    for entry in conn.entries:
        username = str(entry.sAMAccountName) if hasattr(entry, "sAMAccountName") else ""
        display_name = str(entry.displayName) if hasattr(entry, "displayName") else ""
        email = str(entry.mail) if hasattr(entry, "mail") else ""
        writer.writerow([username, display_name, email])

print("Export complete. Saved to ad_users.csv")

conn.unbind()