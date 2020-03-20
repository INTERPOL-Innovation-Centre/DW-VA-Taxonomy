# Dark Web and Crytocurrency Taxonomies

This directory contains taxonomies covering common types of entities found in Dark Web and Cryptocurrency Ecosystems, as well as abusive, possibly criminal behaviors found in real-world investigations.

Concept definitions follow the [Simple Knowledge Organization System (SKOS)](https://www.w3.org/2004/02/skos/).

For readability, and low-barrier bootsprapping, all taxonomies follow the YAML format proposed by [SKOUT](https://github.com/marcelotto/skout).

## How to run the Website locally

Checkout this git repository to your local machine

	git clone git@github.com:INTERPOL-Innovation-Centre/DW-CC-Taxonomy.git
	cd DW-CC-Taxonomy

Make sure you have [Jekyll][jekyll] installed

	gem install bundler jekyll

Run Jekyll locally

	bundle exec jekyll serve --watch

Access the taxonomy website locallly using your browser

	http://127.0.0.1:4000/

## How to convert from YAML to a defined SKOS serialization format

Make sure SKOUT is installed

	~/.mix/escripts/skout entity_taxonomy.yaml entity_taxonomy.ttl

## Contribute

Should you wish to contribute to this project, please review our [Contributor's page][contributing]

[contributing]: CONTRIBUTING.md
[jekyll]: https://jekyllrb.com/
