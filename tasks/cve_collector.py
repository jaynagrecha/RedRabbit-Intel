from app import create_app
from celery_config import make_celery
import requests

app = create_app()
celery = make_celery(app)

@celery.task()
def fetch_cve_data():
    url = 'https://services.nvd.nist.gov/rest/json/cves/1.0'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Placeholder logic to process CVEs
            print(f"Fetched {len(data.get('result', {}).get('CVE_Items', []))} CVEs")
        else:
            print("Failed to fetch CVEs")
    except Exception as e:
        print(f"Error: {e}")
