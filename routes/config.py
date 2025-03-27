from flask import Blueprint, request, jsonify
from models import db, APIKey, SourceToggle

config_bp = Blueprint('config_bp', __name__)

@config_bp.route('/apikey', methods=['POST'])
def add_apikey():
    data = request.json
    service = data.get('service')
    key = data.get('key')
    existing = APIKey.query.filter_by(service=service).first()
    if existing:
        existing.key = key
    else:
        new_key = APIKey(service=service, key=key)
        db.session.add(new_key)
    db.session.commit()
    return jsonify({'status': 'success'})

@config_bp.route('/toggle/<string:source>', methods=['PATCH'])
def toggle_source(source):
    toggle = SourceToggle.query.filter_by(source=source).first()
    if toggle:
        toggle.enabled = not toggle.enabled
    else:
        toggle = SourceToggle(source=source, enabled=True)
        db.session.add(toggle)
    db.session.commit()
    return jsonify({'source': source, 'enabled': toggle.enabled})

@config_bp.route('/toggles', methods=['GET'])
def get_toggles():
    toggles = SourceToggle.query.all()
    return jsonify([{ 'source': t.source, 'enabled': t.enabled } for t in toggles])
