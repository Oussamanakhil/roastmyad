import os
import requests

SUPABASE_URL = os.getenv("https://ecyudrlpprqfxccvqkyd.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVjeXVkcmxwcHJxZnhjY3Zxa3lkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQxODQ1MDgsImV4cCI6MjA2OTc2MDUwOH0.eLF1amtbtZFGLdUm15fQaU8emmgeBFtr1Z5lFLXJeRE")
SUPABASE_TABLE = "roasts"

def insert_roast(data):
    url = f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()
