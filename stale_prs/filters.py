import datetime
from typing import Callable
import dateparser

def create_label_filter(label: str) -> Callable[[object], bool]:
    def _do_filter(record):
        return any(True for l in record['labels'] if l['name'] == label)
    return _do_filter

def create_age_filter(age: datetime.datetime) -> Callable[[object], bool]:
    def _do_filter(record):
        record_created_at = dateparser.parse(record['created_at'])
        return record_created_at <= age
    return _do_filter
