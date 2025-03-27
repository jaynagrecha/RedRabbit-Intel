from app import create_app
from celery_config import make_celery
import requests
import os

app = create_app()
celery = make_celery(app)

@celery.task()
def fetch_virustotal_data(ioc):
    api_key = os.environ.get('VT_API_KEY')
    headers = {
        "x-apikey": api_key
    }
    url = f"https://www.virustotal.com/api/v3/search?query={ioc}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"VirusTotal data for {ioc}: {data}")
        else:
            print(f"Failed to fetch VT data for {ioc}")
    except Exception as e:
        print(f"VirusTotal Error: {e}")
