#!/bin/bash

# Cleaning old file
rm -f $DATADIR/downloaded.csv.gz

curl https://static.data.gouv.fr/resources/bases-statistiques-communale-et-departementale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales/20230719-080828/donnee-dep-data.gouv-2022-geographie2023-produit-le2023-07-17.csv.gz > "$DATADIR/downloaded.csv.gz"

cd "$DATADIR"

gunzip -f downloaded.csv.gz
mv downloaded.csv "$DOWNLOADED_FILE"
