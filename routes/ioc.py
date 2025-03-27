from flask import Blueprint, request, jsonify
from models import IOC, db

ioc_bp = Blueprint('ioc_bp', __name__)

@ioc_bp.route('/', methods=['GET'])
def get_iocs():
    iocs = IOC.query.all()
    return jsonify([ioc.serialize() for ioc in iocs])
