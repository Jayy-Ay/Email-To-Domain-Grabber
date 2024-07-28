"""
@author: Jared Tan
@date: 26/7/2024

Turns a csv file with an 'Email' column into a list of domains
"""
import pandas as pd

def getDomain(email):           
    rec = False
    out = ""
    for e in str(email):                                                            # Only records words past the "@"
        if rec: out+=e
        if e=="@": rec=True
    return out

if __name__ == "__main__":
    file_path = input("Insert Pathway: ")                                           # Get Path
    file_path = file_path.strip('"')                                                # Remove "" if nessesary

    df = pd.read_csv(file_path, encoding='unicode_escape', usecols=["Email"])       # Gets only Email Column
    df_filtered = df.dropna(subset=['Email'], inplace=False)                        # Remove empty rows

    domains = []
    for index, row in df_filtered.iterrows():                                       # For each email in each row...
        email = row["Email"]
        domains.append(getDomain(email))
    
    domains = sorted(set(domains))                                                  # Removes duplicate + Sorts alphabetically
    for e in domains:
        print(e)