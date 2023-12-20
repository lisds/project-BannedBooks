""" Fetch and validate data
"""

from pathlib import Path
import requests
import hashlib

file_info = {
    # Dictionary with key values pairs, where keys are output filenames
    # and values are dictionaries with keys URL and SHA1 hash.
    'compas-scores-two-years.csv': {
        'url': 'https://github.com/propublica/compas-analysis/blob/master/compas-scores-two-years.csv',
        'sha1': 'fe047a4d8499d8d75f585a32bb6275572350a6d6'},
    'compas-scores-two-years-violent.csv': {
        'url': 'https://github.com/propublica/compas-analysis/blob/master/compas-scores-two-years-violent.csv',
        'sha1': 'fc0aede9a844e3d8cd77bd853b79e68967970135'},
    'cox-parsed.csv': {
        'url': 'https://github.com/propublica/compas-analysis/blob/master/cox-parsed.csv',
        'sha1': '8ca4da06652b8b0cc67bd2feb6a459680a3118a1'},
    'cox-violent-parsed.csv': {
        'url': 'https://github.com/propublica/compas-analysis/blob/master/cox-violent-parsed.csv',
        'sha1': 'cec855658a958bc926a95abbf54e018edab69925'}
}

data_path = Path('CompasAnalysis')

for fname, info in file_info.items():
    out_path = data_path / fname
    r = requests.get(info['url'])
    out_path.write_bytes(r.content)
    assert hashlib.sha1(out_path.read_bytes()).hexdigest() == info['sha1']

print('Fetch and validation passed')
