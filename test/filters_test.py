import datetime
from stale_prs.filters import create_label_filter, create_age_filter

def test_label_filter_false_case():
    f = create_label_filter('test')
    result = f({'labels': [{'name': 'foo'}, {'name': 'bar'}]})
    assert result == False

def test_label_filter_true_case():
    f = create_label_filter('test')
    result = f({'labels': [{'name': 'foo'}, {'name': 'bar'}, {'name': 'test'}]})
    assert result == True

def test_age_filter_false_case():
    date_1 = datetime.datetime.now()
    date_2 = date_1 - datetime.timedelta(days=1)
    f = create_age_filter(date_1)
    result = f({'created_at': date_2.isoformat()})
    # date2 < date1 so we should include in result (True)
    assert result == True

def test_age_filter_true_case():
    date_1 = datetime.datetime.now()
    date_2 = date_1 - datetime.timedelta(days=1)
    f = create_age_filter(date_2)
    result = f({'created_at': date_1.isoformat()})
    # date2 < date1 so we should NOT include in result (False)
    assert result == False
