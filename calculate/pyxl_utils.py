"""
OpenPyXl_Utils

Utility functions to help with OpenPyXL.

Len Wanger
6/28/2016
"""

import logging
import numbers


#
# OpenPyXl utility functions
#


def sheet_generator(wb, ignore_sheets=None):
    if ignore_sheets is None:
        ignore_sheets = []
    sheets = wb.get_sheet_names()

    for sheet in sheets:
        sh = wb.get_sheet_by_name(sheet)

        if sh.title in ignore_sheets:
            logging.warning('\t{:15}Ignoring sheet'.format(sh.title))
            continue

        yield sh


def make_cell_range(sh, min_col='A', max_col=None, min_row=1, max_row=None):
    if max_col is None:
        max_col = sh.max_col
    if max_row is None:
        max_row = sh.max_row

    return '{}{}:{}{}'.format(min_col, min_row, max_col, max_row)


def is_blank_cell(cell):
    if cell.value is None:
        return True
    elif isinstance(cell.value, str) and (len(cell.value) == 0 or cell.value.isspace()):
        return True
    else:
        return False


def is_formula(cell):  # cell.type == 'f' is a formula?
    if cell.value and isinstance(cell.value, str) and cell.value[0] == '=':
        return True
    else:
        return False


def is_number(cell):  # LRW - should check for data_type of 'n' or 'f' instead?
    if cell.value is None:
        return False
    else:
        return isinstance(cell.value, numbers.Number)
        # return cell.data_type in ('n', 'f') and not cell.is_date # strings can be type 'f'


def is_date(cell):
    if cell.value is None:
        return False
    else:
        return cell.is_date


def is_string(cell):
    if cell.value is None:
        return False
    else:
        return cell.data_type == 's'


def startswith(cell, s, lower=True):
    if is_string(cell):
        if lower:
            return cell.value.lower().startswith(s)
        else:
            return cell.value.startswith(s)

    return False


def cell_range_generator(ws, cell_range, skip_nones=True):
    for row in ws.iter_rows(cell_range):
        for cell in row:
            if cell.value is None and skip_nones:
                continue
            yield cell
