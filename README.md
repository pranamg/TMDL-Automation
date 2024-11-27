# TMDL-Automation
Repository for automating Power BI tasks using TMDL format.

## Purpose
The purpose of this repository is to automate Power BI tasks using TMDL format.

## Key Features
- Automate Power BI report generation
- Schedule and manage Power BI data refreshes
- Export and import Power BI reports
- Manage Power BI datasets and data sources
- Integrate with other tools and services

## Generating DAX Measures
A new script `scripts/generate_dax_measures.py` has been added to generate DAX measures programmatically based on a JSON input.

### Usage
1. Prepare a JSON file containing measure definitions. Refer to `examples/sample_measures.json` for the input format.
2. Run the script with the JSON file as input and specify the output file for the generated DAX measures.

```sh
python scripts/generate_dax_measures.py path/to/input.json path/to/output.dax
```

## Contribution Guidelines
We welcome contributions to this project. To contribute, please follow these steps:
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes and commit them with clear and descriptive messages
4. Push your changes to your fork
5. Create a pull request to the main repository

Please ensure that your code adheres to our coding standards and includes appropriate tests.
