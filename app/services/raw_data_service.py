import os
from typing import Dict, List, Tuple

import app.repository.raw_data_repository as rew_data_repo
from app.services.produce.suspicious_content_producer import produce_suspicious_content

SUSPICIOUS_WORDS = {
    'hostage': os.environ['MESSAGES_HOSTAGE_TOPIC'],
    'explos': os.environ['MESSAGES_EXPLOSIVE_TOPIC'],
}


def handle_raw_data(message) -> bool:
    try:
        inspect_message(message.value)
        insert_raw_data(message.value)
        return True
    except Exception as e:
        print(e)
        return False


def insert_raw_data(raw_data) -> bool:
    try:
        inserted_id = rew_data_repo.save_raw_data(raw_data)
        print(f'Data with id: {inserted_id} inserted successfully.')
        return True
    except Exception as e:
        print(f'Failed to insert data, Error: {e}')
        return False


def find_suspicious_content(sentences: List[str]) -> Tuple[bool, str | None]:
    for sentence in sentences:
        for word, topic in SUSPICIOUS_WORDS.items():
            if word in sentence.lower():
                return True, topic
    return False, None


def sort_by_suspicious(sentences: List[str], suspicious_word: str) -> List[str]:
    return sorted(
        sentences,
        key=lambda sentence: suspicious_word in sentence.lower(),
        reverse=True
    )


def inspect_message(message: Dict) -> None:
    sentences = message.get('sentences', [])
    has_suspicious, topic = find_suspicious_content(sentences)
    if has_suspicious and topic:
        suspicious_word = next(
            word for word, t in SUSPICIOUS_WORDS.items()
            if t == topic
        )
        message['sentences'] = sort_by_suspicious(sentences, suspicious_word)
        produce_suspicious_content(topic, message)
        print(f'suspicious_word: {suspicious_word}, \ntopic: {topic}, \nsorted_sentences: {message['sentences']}')
