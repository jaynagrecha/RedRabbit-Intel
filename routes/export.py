from flask import Blueprint, jsonify, make_response
from models import IOC, db
import csv
import io
from stix2 import Indicator, Bundle

export_bp = Blueprint('export_bp', __name__)

@export_bp.route('/csv', methods=['GET'])
def export_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Indicator', 'Type', 'Source'])

    for ioc in IOC.query.all():
        writer.writerow([ioc.id, ioc.indicator, ioc.type, ioc.source])
    
    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=iocs.csv"
    response.headers["Content-type"] = "text/csv"
    return response

@export_bp.route('/json', methods=['GET'])
def export_json():
    iocs = IOC.query.all()
    return jsonify([ioc.serialize() for ioc in iocs])

@export_bp.route('/stix2', methods=['GET'])
def export_stix2():
    indicators = []
    for ioc in IOC.query.all():
        indicator = Indicator(
            name=f"IOC: {ioc.indicator}",
            labels=["malicious-activity"],
            pattern_type="stix",
            pattern=f"[ipv4-addr:value = '{ioc.indicator}']" if ioc.type == "ip" else f"[domain-name:value = '{ioc.indicator}']"
        )
        indicators.append(indicator)
    bundle = Bundle(objects=indicators)
    return jsonify(bundle.serialize())
