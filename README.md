# Canine

A convenient API for fetching bioinformatics and genomics datasets. Provides a RESTful framework for grabbing datasets.

This repository contains:

1. The repository requirements in `requirements.txt`
2. Project inner workings under `project/`
  1. Flask API application at `project/application.py`
  2. Custom functions under `project/lib/`
  3. Flask HTML templates under `project/templates/`


## Table of Contents

- [Background](#background)
- [Usage](#usage)


## Background

Bioinformatics software requires that datasets be pulled from various sources including but not limited to the NCBI databases (GenBank, PubMed, nucleotide, etc.), UCI Machine Learning Repository, and many others. To simplify the bioinformatics pipeline, this API provides a single point of contact to pull data from these sources and provided standardized output.


## Usage

Install the requirements in a new python environment using the included requirements file.

```sh
conda create -n bioinformatics python=3.8.6
conda activate bioinformatics
pip3 install -r requirements.txt
```

Then navigate to the `project` directory and run the API.

```sh
python application.py
```

You can connect to the API using a browser or the python request library in another application. Connecting to `http://localhost:5050/` will present a welcome screen with the API documentation. You can test the API using the following query:

[http://localhost:5050/api?version=0.0.0&user=skynet@world.domination&resource=ncbi&database=nucleotide&term=CRT[Gene%20Name]%20AND%20%22Plasmodium%20falciparum%22[Organism]&format=gb](http://localhost:5050/api?version=0.0.0&user=skynet@world.domination&resource=ncbi&database=nucleotide&term=CRT[Gene%20Name]%20AND%20%22Plasmodium%20falciparum%22[Organism]&format=gb)
