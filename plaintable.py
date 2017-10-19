from datetime import datetime

# Python 2.7 fixes
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

__version__ = '0.2.0'
__license__ = 'MIT'
__copyright__ = '(c) 2014-2016 Stefan Tatschner <rumpelsepp@sevenbyte.org>'


ALIGNMENT = { 'l': '<', 'r': '>', 'c': '^' }


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

    def __init__(self, data=None, headline=None, align='l', padding=2, floatprec=2,
                 truncate=True, header_padding=0, datetimefs='%Y-%m-%d %H:%M',
                 theme='simple'):

        self.data = data[:] or []
        self.headline = headline
        self.align = align
        self.padding = padding
        self.floatprec = floatprec
        self.truncate = truncate
        self.header_padding = header_padding
        self.datetimefs = datetimefs
        self.theme = theme

    def _render(self):
        """
        Delay rendering until the table is displayed.
        """
        # Transpose data to get max column widths.
        # Take care of zip and zip_longest, see #8.
        data = self._normalize(self.data)

        if self.truncate:
            columns = list(zip(*data))
        else:
            columns = list(zip_longest(*data, fillvalue=''))
        widths = self._get_widths(columns)

        if self.headline:
            if self.header_padding:
                padding_str = ' ' * self.header_padding
                headline = ['{0}{1}{0}'.format(padding_str, col)
                            for col in self.headline]
            else:
                headline = self.headline

            # Prepend the header to the table and update columns.
            header = self._get_header(headline, widths)
            # We have to use reversed; from docs.python.org:
            # The series of left appends results in reversing the
            # order of elements in the iterable argument.
            for hrow in reversed(header):
                data.insert(0, hrow)
            # See #8.
            if self.truncate:
                columns = list(zip(*data))
            else:
                columns = list(zip_longest(*data, fillvalue=''))
            widths = self._get_widths(columns)

        if self.THEMES[self.theme]['footer_line']:
            footer = self._get_footer(widths)
            data.append(footer)
            # See #8.
            if self.truncate:
                columns = list(zip(*data))
            else:
                columns = list(zip_longest(*data, fillvalue=''))
            widths = self._get_widths(columns)

        # Align columns and then transpose it again to get the table back.
        rendered = list(zip(*self._align(columns, widths)))

        if self.align != 'l':
            table = [''.join(line) for line in rendered]
        else:
            table = [''.join(line).strip() for line in rendered]
        table = '\n'.join(table)
        return table

    def _normalize(self, data):
        """Converts the given data to strings for usage in a table"""
        norm_data = []
        for row in data:
            norm_row = []
            for column in row:
                # Use customer formmaters for float and datetime objects.
                if isinstance(column, float):
                    item = '{:.{}f}'.format(column, self.floatprec)
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
                try:
                    align_mark = ALIGNMENT[self.align]
                except KeyError:
                    msg = 'Alignment must be l, c, or r (not {!r})'.format(self.align)
                    raise ValueError(msg)
                aligned_item = '{:{}{}}'.format(item, align_mark, total_width)
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

    def append(self, row):
        self.data.append(row)

    def extend(self, rows):
        self.data.extend(rows)

    def insert(self, index, row):
        self.data.insert(index, row)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return self._render()
