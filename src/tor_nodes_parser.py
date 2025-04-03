import requests
import json
import csv
import os
from urllib.parse import urlparse
import ipaddress

ALL_NODES_CSV_FILENAME_V4 = "all_v4.csv"
ALL_NODES_CSV_FILENAME_V6 = "all_v6.csv"
GUARD_NODES_CSV_FILENAME_V4 = "guards_v4.csv"
GUARD_NODES_CSV_FILENAME_V6 = "guards_v6.csv"
EXIT_NODES_CSV_FILENAME_V4 = "exits_v4.csv"
EXIT_NODES_CSV_FILENAME_V6 = "exits_v6.csv"

CSV_HEADER = [
    "fingerprint", "ipaddr", "port", "stix_pattern",
    "label_name", "label_color", "marking_type", "marking_value", "marking_priority"
]

def fetch_tor_nodes():
    url = "https://onionoo.torproject.org/details?search=type:relay%20running:true"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def parse_tor_node(node):
    csv_rows_v4 = []
    csv_rows_v6 = []
    for or_address in node.get("or_addresses", []):
        parsed_url = urlparse(f"tcp://{or_address}")
        ip = parsed_url.hostname
        port = parsed_url.port

        try:
            ip_obj = ipaddress.ip_address(ip)
            if isinstance(ip_obj, ipaddress.IPv4Address):
                stix_pattern = f"[ipv4-addr:value = '{ip}' AND network-traffic:src_port = {port}]"
                csv_rows_v4.append([
                    node["fingerprint"], ip, port, stix_pattern,
                    "tor", "#57C101", "TLP", "TLP:CLEAR", "1"
                ])
            elif isinstance(ip_obj, ipaddress.IPv6Address):
                stix_pattern = f"[ipv6-addr:value = '{ip}' AND network-traffic:src_port = {port}]"
                csv_rows_v6.append([
                    node["fingerprint"], ip, port, stix_pattern,
                    "tor", "#57C101", "TLP", "TLP:CLEAR", "1"
                ])
        except ValueError:
            continue

    return csv_rows_v4, csv_rows_v6

def write_csv(filename, rows):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADER)
        writer.writerows(rows)

def main():
    try:
        data = fetch_tor_nodes()
        all_nodes_rows_v4 = []
        all_nodes_rows_v6 = []
        guard_nodes_rows_v4 = []
        guard_nodes_rows_v6 = []
        exit_nodes_rows_v4 = []
        exit_nodes_rows_v6 = []

        for relay in data.get("relays", []):
            rows_v4, rows_v6 = parse_tor_node(relay)
            all_nodes_rows_v4.extend(rows_v4)
            all_nodes_rows_v6.extend(rows_v6)
            if "Guard" in relay.get("flags", []):
                guard_nodes_rows_v4.extend(rows_v4)
                guard_nodes_rows_v6.extend(rows_v6)
            if "Exit" in relay.get("flags", []):
                exit_nodes_rows_v4.extend(rows_v4)
                exit_nodes_rows_v6.extend(rows_v6)

        write_csv(ALL_NODES_CSV_FILENAME_V4, all_nodes_rows_v4)
        write_csv(ALL_NODES_CSV_FILENAME_V6, all_nodes_rows_v6)
        write_csv(GUARD_NODES_CSV_FILENAME_V4, guard_nodes_rows_v4)
        write_csv(GUARD_NODES_CSV_FILENAME_V6, guard_nodes_rows_v6)
        write_csv(EXIT_NODES_CSV_FILENAME_V4, exit_nodes_rows_v4)
        write_csv(EXIT_NODES_CSV_FILENAME_V6, exit_nodes_rows_v6)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
