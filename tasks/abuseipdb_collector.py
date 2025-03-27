from app import create_app
from celery_config import make_celery
import requests
import os

app = create_app()
celery = make_celery(app)

@celery.task()
def fetch_abuseipdb_data(ip_address):
    api_key = os.environ.get('ABUSEIPDB_API_KEY')
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}&maxAgeInDays=90"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"AbuseIPDB data for {ip_address}: {data}")
        else:
            print(f"Failed to fetch AbuseIPDB data for {ip_address}")
    except Exception as e:
        print(f"AbuseIPDB Error: {e}")
