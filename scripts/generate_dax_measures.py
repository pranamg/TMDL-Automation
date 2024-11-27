import json

def generate_dax_measures(json_file, output_file):
    with open(json_file, 'r') as file:
        measures = json.load(file)

    dax_measures = []
    for measure in measures:
        dax_measure = f'measure "{measure["name"]}" = {measure["expression"]}\n'
        if "formatString" in measure:
            dax_measure += f'    formatString: "{measure["formatString"]}"\n'
        if "displayFolder" in measure:
            dax_measure += f'    displayFolder: "{measure["displayFolder"]}"\n'
        if "description" in measure:
            dax_measure += f'    description: "{measure["description"]}"\n'
        if "isHidden" in measure:
            dax_measure += f'    isHidden: {str(measure["isHidden"]).lower()}\n'
        if "isPrivate" in measure:
            dax_measure += f'    isPrivate: {str(measure["isPrivate"]).lower()}\n'
        if "detailRowsExpression" in measure:
            dax_measure += f'    detailRowsExpression: {measure["detailRowsExpression"]}\n'
        if "annotations" in measure:
            annotations = ', '.join([f'{k}: "{v}"' for k, v in measure["annotations"].items()])
            dax_measure += f'    annotations: {{{annotations}}}\n'
        if "formatStringExpression" in measure:
            dax_measure += f'    formatStringExpression: {measure["formatStringExpression"]}\n'
        if "dataType" in measure:
            dax_measure += f'    dataType: {measure["dataType"]}\n'
        if "summarizeBy" in measure:
            dax_measure += f'    summarizeBy: {measure["summarizeBy"]}\n'
        if "properties" in measure:
            properties = ', '.join([f'{k}: "{v}"' for k, v in measure["properties"].items()])
            dax_measure += f'    properties: {{{properties}}}\n'
        if "isAggDependent" in measure:
            dax_measure += f'    isAggDependent: {str(measure["isAggDependent"]).lower()}\n'
        if "metadata" in measure:
            metadata = ', '.join([f'{k}: "{v}"' for k, v in measure["metadata"].items()])
            dax_measure += f'    metadata: {{{metadata}}}\n'
        dax_measures.append(dax_measure)

    with open(output_file, 'w') as file:
        file.write('\n'.join(dax_measures))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate DAX measures from a JSON file.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file containing measure definitions.')
    parser.add_argument('output_file', type=str, help='Path to the output file to save the generated DAX measures.')

    args = parser.parse_args()

    generate_dax_measures(args.json_file, args.output_file)
