import socket
import csv, os
from urllib.parse import urlparse

class ip_puller:

    def __init__(self):
        self.ips = set()

    def run_pull(self, filepath):
        csv_file_path = os.path.abspath(filepath)
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    url = row[0]
                    parse_url = urlparse(url).netloc
                    self.ips.add(socket.gethostbyname("www." + parse_url))
                except:
                    continue