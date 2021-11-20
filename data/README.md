# data

This directory contains the various stages of study data used for analysis.
Brief descriptions of each stage are provided below in order from least to most
modified.

## Raw Data

The raw data (`raw-owners.csv` and `raw-dogs.csv`) is a dump of the collected
responses from the electric data capture (EDC) platform Typeform. The raw data
is split across two datasets because information about a dog owner was collected
separately from the information about each owned dog. The tables below are for
illustrative purposes to convey the general structure of the data.

### Raw Owner Data

owner-id | field-1 | ... | field-n
--- | --- | --- | ---
abc123 | answer-1 | ... | answer-n
xyz456 | answer-1 | ... | answer-n

### Raw Dog Data

dog-name | field-1 | ... | field-n | owner-id
mark | answer-1 | ... | answer-n | abc123
kevin | answer-1 | ... | answer-n | abc123
dan | answer-1 | ... | answer-n | xyz456
