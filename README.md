# pycobol2csv
pycobol2csv is a Python library to convert COBOL ebcdic file to CSV format. The package is built to cater for advanced features in COBOL copybooks such as *OCCURES x TIMES*. 

The CSV file is RDBMS friendly and all headers are ready to be used as database column names.
CSV conversion is controlled by config file in *csv_config.json*

Install the python module:

`pip install `

To use the module:

```
from pycobol2csv import convert_cobol_file

convert_cobol_file(copybook_file, data_file, output_file, config_file, codepage)

```

- copybook_file: copybook filename
- data_file: data filename 
- output_file: output csv filename
- config_file: csv configuration filename, refer to csv_config.json
- codepage: codepage for edibic, refer to https://docs.python.org/3.7/library/codecs.html#standard-encodings for details

Repo: https://github.com/jasonli-lijie/pycobol2csv
