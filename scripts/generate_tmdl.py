def generate_tmdl(fact_table_name, value_column_name, date_column_name, calendar_table_name, calendar_date_column_name, measure_table_name):
    """
    Generates a TMDL file with parameterized time intelligence measures in YAML-like format.

    Args:
        fact_table_name (str): The name of the fact table.
        value_column_name (str): The name of the value column.
        date_column_name (str): The name of the date column in the fact table.
        calendar_table_name (str): The name of the calendar table.
        calendar_date_column_name (str): The name of the date column in the calendar table.
        measure_table_name (str): The name of the table where the measures should be placed.


    Returns:
        str: The generated TMDL content.
    """


    format_string_definition = """
        VAR CurrentValue  = SELECTEDMEASURE()
        RETURN SWITCH (
            TRUE (),
            CurrentValue < -1E6, "$#,0,,.00 M",
            CurrentValue < -1E3, "$#,0,.00 K",
            CurrentValue < 1E3, "#,0",
            CurrentValue < 1E6, "#,0,.00 K",
            CurrentValue < 1E9, "#,0,,.00 M",
            "#,0,,,.000 B"
        )
    """

    tmdl_content = f"table '{measure_table_name}'\n"
        
    tmdl_content += "\n"  # Add the newline after table definition
    
    tmdl_content += f"\t/// This measure calculates the Total of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'Total {value_column_name}\' =\n'
    tmdl_content += f'\t\tSUM({fact_table_name}[{value_column_name}])\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Year-to-Date (YTD) of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'YTD {value_column_name}\' =\n'
    tmdl_content += f'\t\tTOTALYTD([Total {value_column_name}], {calendar_table_name}[{calendar_date_column_name}])\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Quarter-to-Date (QTD) of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'QTD {value_column_name}\' =\n'
    tmdl_content += f'\t\tTOTALQTD([Total {value_column_name}], {calendar_table_name}[{calendar_date_column_name}])\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Month-to-Date (MTD) of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'MTD {value_column_name}\' =\n'
    tmdl_content += f'\t\tTOTALMTD([Total {value_column_name}], {calendar_table_name}[{calendar_date_column_name}])\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Previous Year (PY) of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'PY {value_column_name}\' =\n'
    tmdl_content += f'\t\tCALCULATE([Total {value_column_name}], SAMEPERIODLASTYEAR({calendar_table_name}[{calendar_date_column_name}]))\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Previous Quarter (PQ) of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'PQ {value_column_name}\' =\n'
    tmdl_content += f'\t\tCALCULATE([Total {value_column_name}], PREVIOUSQUARTER({calendar_table_name}[{calendar_date_column_name}]))\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Previous Month (PM) of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'PM {value_column_name}\' =\n'
    tmdl_content += f'\t\tCALCULATE([Total {value_column_name}], PREVIOUSMONTH({calendar_table_name}[{calendar_date_column_name}]))\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Year-over-Year (YoY) Growth of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'YoY Growth\' =\n'
    tmdl_content += f'\t\tDIVIDE([Total {value_column_name}] - [PY {value_column_name}], [PY {value_column_name}], 0)\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Quarter-over-Quarter (QoQ) Growth of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'QoQ Growth\' =\n'
    tmdl_content += f'\t\tDIVIDE([Total {value_column_name}] - [PQ {value_column_name}], [PQ {value_column_name}], 0)\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the Month-over-Month (MoM) Growth of the {value_column_name}.\n"
    tmdl_content += f'\tmeasure \'MoM Growth\' =\n'
    tmdl_content += f'\t\tDIVIDE([Total {value_column_name}] - [PM {value_column_name}], [PM {value_column_name}], 0)\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the {value_column_name} of Last Year Same Month.\n"
    tmdl_content += f'\tmeasure \'{value_column_name} Last Year Same Month\' =\n'
    tmdl_content += f'\t\tCALCULATE ([Total {value_column_name}],SAMEPERIODLASTYEAR (DATEADD({calendar_table_name}[{calendar_date_column_name}], - (DAY({calendar_table_name}[{calendar_date_column_name}])-1), DAY)))\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the YTD {value_column_name} of Same Month Previous Year.\n"
    tmdl_content += f'\tmeasure \'{value_column_name} Same Month Previous Year YTD\' =\n'
    tmdl_content += f'\t\tCALCULATE ([YTD {value_column_name}],SAMEPERIODLASTYEAR (DATEADD({calendar_table_name}[{calendar_date_column_name}], - (DAY({calendar_table_name}[{calendar_date_column_name}])-1), DAY)))\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the {value_column_name} of Last Year Same Quarter.\n"
    tmdl_content += f'\tmeasure \'{value_column_name} Last Year Same Quarter\' =\n'
    tmdl_content += f'\t\tCALCULATE ( [Total {value_column_name}], SAMEPERIODLASTYEAR (DATEADD({calendar_table_name}[{calendar_date_column_name}],- (DAY({calendar_table_name}[{calendar_date_column_name}])-1),DAY) - (MONTH({calendar_table_name}[{calendar_date_column_name}]) -1),MONTH))\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the YTD {value_column_name} of Same Quarter Previous Year.\n"
    tmdl_content += f'\tmeasure \'{value_column_name} Same Quarter Previous Year YTD\' =\n'
    tmdl_content += f'\t\tCALCULATE ( [YTD {value_column_name}], SAMEPERIODLASTYEAR (DATEADD({calendar_table_name}[{calendar_date_column_name}],- (DAY({calendar_table_name}[{calendar_date_column_name}])-1),DAY) - (MONTH({calendar_table_name}[{calendar_date_column_name}]) -1),MONTH))\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the {value_column_name} of Last Year Same Day.\n"
    tmdl_content += f'\tmeasure \'{value_column_name} Last Year Same Day\' =\n'
    tmdl_content += f'\t\tCALCULATE ( [Total {value_column_name}], SAMEPERIODLASTYEAR ( {calendar_table_name}[{calendar_date_column_name}] ) )\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += f"\t/// This measure calculates the YTD {value_column_name} of Last Year Same Day.\n"
    tmdl_content += f'\tmeasure \'{value_column_name} Last Year Same Day YTD\' =\n'
    tmdl_content += f'\t\tCALCULATE ( [YTD {value_column_name}], SAMEPERIODLASTYEAR ( {calendar_table_name}[{calendar_date_column_name}] ) )\n'
    tmdl_content += f'\t\tdisplayFolder: TimeIntelligence\n'
    tmdl_content += f'\t\tformatStringDefinition = \n\t\t\t{format_string_definition}\n\n'

    tmdl_content += "\n"  # Add the newline after table definition

    return tmdl_content


if __name__ == "__main__":
    fact_table = input("Enter the fact table name: ")
    value_column = input("Enter the value column name: ")
    date_column = input("Enter the date column name in the fact table: ")
    calendar_table = input("Enter the calendar table name: ")
    calendar_date_column = input("Enter the calendar date column name: ")
    measure_table = input("Enter the table name where the measures should be placed: ")

    tmdl_content = generate_tmdl(fact_table, value_column, date_column, calendar_table, calendar_date_column, measure_table)

    filename = f"{measure_table}.tmdl"
    with open(filename, "w") as outfile:
        outfile.write(tmdl_content)

    print(f"TMDL file generated successfully as {filename}")