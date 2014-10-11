from collections import deque
from datetime import datetime

# Python 2.7 fixes
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

__version__ = '0.1.1'
__license__ = 'MIT'
__copyright__ = '(c) 2014 Stefan Tatschner <stefan@sevenbyte.org>'


class Table:

    THEMES = {
        'simple': {
            'header_overline':  '',
            'header_underline': '-',
            'footer_line':      '',
        },
        'plain': {
            'header_overline':  '',
            'header_underline': '',
            'footer_line':      '',
        },
        'rst': {
            'header_overline':  '=',
            'header_underline': '=',
            'footer_line':      '=',
        },
    }

    def __init__(self, data, headline=None, align='l', padding=2, floatprec=2,
                 header_padding=0, datetimefs='%Y-%m-%d %H:%M',
                 theme='simple'):
        self.align = align
        self.padding = padding
        self.floatprec = floatprec
        self.datetimefs = datetimefs
        self.theme = theme

        # Use a deque to be able to easily prepend the table header.
        data = deque(self._normalize(data))
        # Transpose data to get max column widths.
        # Use zip_longest to fill empty fields.
        columns = list(zip_longest(*data, fillvalue=''))
        widths = self._get_widths(columns)

        if headline:
            if header_padding:
                padding_str = ' ' * header_padding
                headline = ['{0}{1}{0}'.format(padding_str, col)
                            for col in headline]

            # Prepend the header to the table and update columns.
            header = self._get_header(headline, widths)
            # We have to use reversed; from docs.python.org:
            # The series of left appends results in reversing the
            # order of elements in the iterable argument.
            data.extendleft(reversed(header))
            columns = list(zip(*data))
            widths = self._get_widths(columns)

        if self.THEMES[self.theme]['footer_line']:
            footer = self._get_footer(widths)
            data.append(footer)
            columns = list(zip(*data))
            widths = self._get_widths(columns)

        # Align columns and then transpose it again to get the table back.
        self.data = list(zip(*self._align(columns, widths)))

    def _normalize(self, data):
        """Converts the given data to strings for usage in a table"""
        norm_data = []
        for row in data:
            norm_row = []
            for column in row:
                # Build custom formatstrings for specific objects.
                if isinstance(column, float):
                    format_str = '{{:.{}f}}'.format(self.floatprec)
                    item = format_str.format(column)
                elif isinstance(column, datetime):
                    item = column.strftime(self.datetimefs)
                else:
                    item = str(column)
                norm_row.append(item)
            norm_data.append(norm_row)
        return norm_data

    @staticmethod
    def _get_widths(columns):
        """Gets the max width of each column."""
        # At first find the longest value in
        # a column, then calculate its length.
        return [len(max(column, key=len)) for column in columns]

    def _align(self, columns, widths):
        """Aligns the given columns columns depending on self.alignment"""
        aligned_columns = []
        # Iterate over several lists at the same time.
        # http://stackoverflow.com/a/10080389
        for column, width in zip(columns, widths):
            aligned_column = []
            for item in column:
                # Add padding to the actual column width.
                total_width = width + self.padding
                # Build formatstring depending on alignment.
                if self.align == 'l':
                    format_str = '{{:<{}}}'.format(total_width)
                elif self.align == 'r':
                    format_str = '{{:>{}}}'.format(total_width)
                elif self.align == 'c':
                    format_str = '{{:^{}}}'.format(total_width)
                else:
                    raise RuntimeError('Wrong alignment string')

                aligned_item = format_str.format(item)
                aligned_column.append(aligned_item)
            aligned_columns.append(aligned_column)
        return aligned_columns

    def _get_header(self, headline, column_widths):
        """Creates the table header depending on the chosen theme"""
        header = []
        header_overline = []
        header_underline = []
        header_widths = map(len, headline)

        for width, header_width in zip(column_widths, header_widths):
            width = max(header_width, width)
            if self.THEMES[self.theme]['header_overline']:
                item = self.THEMES[self.theme]['header_overline'] * width
                header_overline.append(item)
            if self.THEMES[self.theme]['header_underline']:
                item = self.THEMES[self.theme]['header_underline'] * width
                header_underline.append(item)

        if header_overline:
            header.append(header_overline)
        header.append(headline)
        if header_underline:
            header.append(header_underline)
        return header

    def _get_footer(self, column_widths):
        footer = []
        for width in column_widths:
            item = self.THEMES[self.theme]['footer_line'] * width
            footer.append(item)
        return footer

    def __str__(self):
        if self.align != 'l':
            table = [''.join(line) for line in self.data]
        else:
            table = [''.join(line).strip() for line in self.data]
        table = '\n'.join(table)
        return table
