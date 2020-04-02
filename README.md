# Dark Web and Cryptoasset Taxonomies

This repository contains taxonomies covering common types of entities found in Dark Web and Cryptoasset Ecosystems, as well as abusive, possibly criminal behaviors found in real-world investigations.

Taxonomies are defined as [YAML][yaml] files and automatically rendered as a human-readable Website by using the [Jekyll][jekyll] static site generator.

## How to run the Website locally

Checkout this git repository to your local machine

	git clone git@github.com:INTERPOL-Innovation-Centre/DW-CC-Taxonomy.git
	cd DW-CC-Taxonomy

Make sure you have [Jekyll][jekyll] installed

	gem install bundler jekyll

Run Jekyll locally

	bundle exec jekyll serve --baseurl '' --watch

Access the taxonomy website locallly using your browser

	http://127.0.0.1:4000/

## How to create / modify / delete concept defintions

All taxonomy definition YAML-files reside in the [\_data](_data) directory.

Each taxonomy file defines a so-called [(concept) **scheme**](https://www.w3.org/2009/08/skos-reference/skos.html#ConceptScheme), which can be viewed as an aggregation of one or more SKOS concepts.

	scheme:
	  baseurl: /taxonomies/abuses
	  csvfile: assets/data/abuses.csv
	  type: conceptScheme
	  version: 0.1
	  lastmod: 2020-03-31
	  title: Abuse Taxonomy
	  creator: INTERPOL Darknet and Cryptocurrencies Working Group
	  description: >
	   This taxonomy defines common forms of abuses encountered in Darknet
	   and Cryptoasset Investigations. This includes improper deployment or
	   usage of services to unfairly or improperly gain benefit.
	  default_language: en

Further it defines a number of concepts that are linked with each other through [broader](https://www.w3.org/2009/08/skos-reference/skos.html#broader)
and [narrower](https://www.w3.org/2009/08/skos-reference/skos.html#narrower) relations and therefore form a hierarchical strucuture. The `seeAlso`relation can be used for referencing external defintion sources.

	scam:
	  id: scam
	  type: concept
	  prefLabel: Scam
	  description: >
	    Scam denotes a fraudulent or deceptive act or operation.
	  seeAlso: https://www.merriam-webster.com/dictionary/scam

A taxonomy can be modified by changing these defintions.

## How to generate downloadable CSV files from defined taxonomies

The taxonomy YAML files in `_data` feed the [Jekyll static Website generator][jekyll] but they are not directly exposed on the Web.

In order to provide machine-processable, downloadable taxonomy representations, they must first be converted into (a) commonly accepted format(s) and provided as downloadable files. This is what the conversion script `script/convert.py` does.

Before running the script, make sure you have Python3 up and running and install the dependencies.

	python3 -m venv venv
	. venv/bin/activate

	pip install -r requirements

Then run the conversion script by passing the taxonomy YAML files and an optional output folder (which is `assets/data` by default.

	./scripts/convert.py -t _data/*.yaml -d assets/data	

This converts each YAML file into a corresponding CSV file, which can then be integrated by client applications that make use of that taxonomy.

	id,uri,label,description
	scam,https://interpol-innovation-centre.github.io/DW-CC-Taxonomy/taxonomies/abuses#scam,Scam,Scam denotes a fraudulent or deceptive act or operation.

After conversion, these files must be added and committed in order to show up on the Website.

	git add assets/data
	git commit -m "updated taxonomy serializion"

## How to contribute

If you have write access to this repository, create a branch, change stuff, and push the branch to Github.

	git branch my_concept_proposal
	git checkout my_concept_proposal
	... change files ..
	git add [... changed files ...]
	git commit -m "some meaningful message"
	git push -u origin my_concept_proposal

Please note that the **master branch is protected**. It feeds the static Website generator and should therefore not be modified without testing things first.

If you are an **external contributor** without direct write access to this repository, then you can basically follow the same procedure, with the main difference being that **you must fork this repository** before. Please check to the [forking documentation](https://guides.github.com/activities/forking/) on Github.

Should you wish to contribute to this project, please review our [Contributor's page][contributing].

[contributing]: CONTRIBUTING.md
[yaml]: https://yaml.org/
[jekyll]: https://jekyllrb.com/
[python]: https://www.python.org/
