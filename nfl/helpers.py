from dateutil.parser import parse

def extract_year(datestring):
    return parse(datestring, fuzzy=True).year