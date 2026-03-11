from googlesearch import search

# --- CONFIGURATION ---
# Replace with your name and specific 2013 'Grit' keywords
target_name = "Jeffrey [Gates]" 
keywords = ["BTD", "Chava", "Uephoric", "Livin Poetry"]
query = f'"{target_name}" ' + " OR ".join([f'"{k}"' for k in keywords])

print(f"R2-D2 Protocol: Scraping the web for 'Shadow' mentions...")

# --- THE EXTRACTION ---
results = []
# We search the first 50 results to find the 'Defamatory' sources
for url in search(query, num_results=50):
    results.append(url)
    print(f"[FOUND]: {url}")

# --- THE MANAGER SUMMARY ---
if not results:
    print("Status: SOVEREIGN. No 'Shadow' links found.")
else:
    print(f"\nALERT: Found {len(results)} potential 'Grit' points.")
    print("Next Step: Systematically request 'Right to be Forgotten' or SEO-bury these links.")
