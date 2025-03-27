from app import create_app
from celery_config import make_celery
import requests
import os

app = create_app()
celery = make_celery(app)

@celery.task()
def fetch_shodan_data(ip_address):
    api_key = os.environ.get('SHODAN_API_KEY')
    if not api_key:
        print("SHODAN API key not found.")
        return

    url = f"https://api.shodan.io/shodan/host/{ip_address}?key={api_key}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"Shodan data for {ip_address}: {data}")
        else:
            print(f"Failed to fetch Shodan data for {ip_address}")
    except Exception as e:
        print(f"Shodan Error: {e}")
