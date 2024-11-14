from typing import Optional, Dict
from collections import Counter

from app.psql_db.models import Email
from app.repository.queries_repository import email_by_address, get_all_sentences


def format_email_data(email: Email) -> dict:
    return {
        "id": str(email.id),
        "email": email.email,
        "username": email.username,
        "ip_address": email.ip_address,
        "created_at": email.created_at.isoformat(),
        "location": {
            "id": str(email.location.id),
            "latitude": email.location.latitude,
            "longitude": email.location.longitude,
            "city": email.location.city,
            "country": email.location.country
        } if email.location else None,
        "device_info": {
            "id": str(email.device_info.id),
            "browser": email.device_info.browser,
            "os": email.device_info.os,
            "device_id": str(email.device_info.device_id)
        } if email.device_info else None,
        "explosive_sentences": [
            {"id": s.id, "content": s.content}
            for s in (email.explosive_sentences or [])
        ],
        "hostage_sentences": [
            {"id": s.id, "content": s.content}
            for s in (email.hostage_sentences or [])
        ]
    }


def get_email_by_address(email_address: str) -> Optional[Dict]:
    email_data = email_by_address(email_address)
    if email_data is not None:
        return format_email_data(email_data)
    else:
        return {}


# def get_most_common_word() -> dict:
#
#     sentences = get_all_sentences()
#
#     all_words = []
#     for sentence in sentences:
#         words = sentence.lower().replace('.', '').replace(',', '').split()
#         all_words.extend(words)
#
#     word_counts = Counter(all_words).most_common()
#
#     if not word_counts:
#         return {
#             "word": None,
#             "count": 0,
#             "total_words": 0
#         }
#
#     most_common_word, count = word_counts[0]
#     return {
#         "word": most_common_word,
#         "count": count,
#         "total_words": len(all_words),
#         "percentage": round((count / len(all_words)) * 100, 2) if all_words else 0
#     }

from collections import Counter
from typing import Dict, List
from toolz import pipe, compose
from toolz.curried import map, reduce
from operator import concat


def get_all_words(sentences: List[str]) -> List[str]:
    return pipe(
        sentences,
        map(str.lower),
        map(lambda s: s.replace('.', '').replace(',', '')),
        map(str.split),
        reduce(concat)
    )


def calculate_word_stats(words: List[str]) -> Dict:
    if not words:
        return {
            "word": None,
            "count": 0,
            "total_words": 0,
            "percentage": 0
        }

    words_rank = Counter(words).most_common()
    top_word, count = words_rank[0]
    total_words = len(words)

    return {
        "word": top_word,
        "count": count,
        "total_words": total_words,
        "percentage": round((count / total_words) * 100, 2)
    }


def get_most_common_word() -> Dict:
    return pipe(
        get_all_sentences(),
        get_all_words,
        calculate_word_stats
    )
