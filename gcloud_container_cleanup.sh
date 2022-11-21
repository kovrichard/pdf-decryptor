#!/bin/sh

while IFS= read -r line; do
    gcloud container images delete gcr.io/pdfdecryptor/pdfdecryptor@$line --quiet
done < $1
