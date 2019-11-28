# Postcode-plotter-python
Takes a single list of postcodes in xlsx format, can be formatted correctly or all as one string with no spaces and plots them on a map of the UK. This was done as a request from a friend.

- Choose an xsls file with post codes (UK) that are allocated one per cell (phone numbers can be included but are wiped out)
- Run the command : `python3 main.py -f path/to/file`
- Running with ~4k postcodes takes about 30-40s
- A html file will be generated in project root with pinlocated post codes
- Non premium google maps api users get a daily max of 20k requests
