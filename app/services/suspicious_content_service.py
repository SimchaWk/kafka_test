from typing import Dict

from functools import partial

from app.repository.suspicious_content_repository import save_email_with_relations
from app.services.parse_models_service import parse_json_to_models


def save_hostage_sentences(data):
    email_model = parse_json_to_models(data.value, 'hostage')
    save_email_with_relations(email_model)


def save_explosive_sentences(data):
    email_model = parse_json_to_models(data.value, 'explosive')
    save_email_with_relations(email_model)
