"""Dictionary related utility functions."""

__author__ = "730480069"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(lib: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Head to the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for item in lib:
        head_rows: list[str] = []
        i: int = 0
        while i < N and i < len(lib[item]):
            head_rows.append(lib[item][i])
            i += 1
        result[item] = head_rows
    return result


def select(lib: dict[str, list[str]], subset: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only selected subset."""
    result: dict[str, list[str]] = {}
    for item in subset:
        result[item] = lib[item]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for item in table1:
        result[item] = table1[item]
    for key in table2:
        if key in result:
            for value in table2[key]:
                result[key].append(value)
        else:
            result[key] = table2[key]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Count the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result