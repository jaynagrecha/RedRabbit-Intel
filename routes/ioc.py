from flask import Blueprint, request, jsonify
from models.config_models import IOC, db


ioc_bp = Blueprint('ioc_bp', __name__)

@ioc_bp.route('/', methods=['GET'])
def get_iocs():
    iocs = IOC.query.all()
    return jsonify([ioc.serialize() for ioc in iocs])

@ioc_bp.route('/seed', methods=['POST'])
def seed_iocs():
    sample_data = [
        IOC(indicator="8.8.8.8", type="ip", source="Manual"),
        IOC(indicator="malicious.com", type="domain", source="ThreatFeedX"),
        IOC(indicator="badactor.net", type="domain", source="Analyst Note")
    ]
    db.session.bulk_save_objects(sample_data)
    db.session.commit()
    return jsonify({"message": "Sample IOCs seeded."})