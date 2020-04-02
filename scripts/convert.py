#!/usr/bin/env python3
from argparse import ArgumentParser
import csv
import os
import yaml

JEKYLL_CONFIG = "_config.yml"


def retrieve_site_base_uri():
    config = yaml.safe_load(open(JEKYLL_CONFIG))
    url = config['url']
    baseurl = config['baseurl']
    return url + baseurl


def convert_csv(taxonomy_file, site_baseURI, output_file):
    taxonomy = yaml.safe_load(open(taxonomy_file))

    taxonomy_baseURI = taxonomy['scheme']['baseurl']
    baseURI = site_baseURI + taxonomy_baseURI

    concepts = [value for key, value in taxonomy.items()
                if value['type'] == 'concept']

    with open(output_file, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['id', 'uri', 'label', 'description'])
        for concept in concepts:
            csv_writer.writerow([concept['id'],
                                baseURI + '#' + concept['id'],
                                concept['prefLabel'],
                                concept['description'].rstrip()])


def main():
    parser = ArgumentParser(description='Taxonomy conversion utility')

    parser.add_argument('-t', '--taxonomies', nargs='+',
                        help='The taxonomies to be converted')
    parser.add_argument('-d', '--destination', nargs='?',
                        default='assets/data',
                        help="Destination folder")

    args = parser.parse_args()

    # ensure destination directory
    if not os.path.exists(args.destination):
        os.makedirs(args.destination)

    # read base URI from config file
    site_baseURI = retrieve_site_base_uri()

    for taxonomy_file in args.taxonomies:
        print("Processing {}".format(taxonomy_file))
        output_file = args.destination + '/' + \
            os.path.splitext(os.path.basename(taxonomy_file))[0] + ".csv"
        print("Writing output to {}".format(output_file))
        convert_csv(taxonomy_file, site_baseURI, output_file)


if __name__ == '__main__':
    main()
