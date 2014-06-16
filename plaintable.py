from datetime import datetime

# Python 2.7 fixes
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

__version__ = '0.1a1.dev1'
__license__ = 'MIT'
__copyright__ = '(c) 2014 Stefan Tatschner <stefan@sevenbyte.org>'


class Table:

    THEMES = {'simple': {'header_overline':  '',
                         'header_underline': '-',
                         'bottom_line':      ''},
              'plain':  {'header_overline':  '',
                         'header_underline': '',
                         'bottom_line':      ''},
              'rst':    {'header_overline':  '=',
                         'header_underline': '=',
                         'bottom_line':      '='}}

    def __init__(self, data, headline=None, align='l', padding=2, floatprec=2,
                 header_padding=0, datetimefs='%Y-%m-%d %H:%M', theme='simple'):
        self.align = align
        self.padding = padding
        self.floatprec = floatprec
        self.datetimefs = datetimefs
        self.theme = theme
        data = self._normalize(data)

        self.cols = list(zip_longest(*data, fillvalue=''))
        self._col_widths = self._get_col_widths()

        if headline:
            if header_padding:
                padding_str = ' ' * header_padding
                headline = ['{0}{1}{0}'.format(padding_str, col) for col in headline]
            # Append the table to header and update cols.
            d = self._get_header(headline)
            d.extend(data)
            self.cols = list(zip_longest(*d, fillvalue=''))
            self._col_widths = self._get_col_widths()

        # if self.THEME['bottom_line']:

        self.cols = self._align_cols()

    def _normalize(self, data):
        norm_data = []
        for row in data:
            norm_row = []
            for col_item in row:
                if isinstance(col_item, float):
                    format_str = '{{:.{}f}}'.format(self.floatprec)
                    item = format_str.format(col_item)
                elif isinstance(col_item, datetime):
                    item = col_item.strftime(self.datetimefs)
                else:
                    item = str(col_item)
                norm_row.append(item)
            norm_data.append(norm_row)
        return norm_data

    def _get_col_widths(self):
        # At first get the longest value in a column, then calculate its length.
        return [len(max(col, key=len)) for col in self.cols]

    def _align_cols(self):
        al_cols = []
        # Iterate over several lists at the same time.
        # http://stackoverflow.com/a/10080389
        for col, width in zip(self.cols, self._col_widths):
            al_col = []
            for item in col:
                pad_width = width + self.padding
                # Build formatstring depending on alignment.
                if self.align == 'l':
                    format_str = '{{:<{}}}'.format(pad_width)
                elif self.align == 'r':
                    format_str = '{{:>{}}}'.format(pad_width)
                elif self.align == 'c':
                    format_str = '{{:^{}}}'.format(pad_width)
                else:
                    raise RuntimeError('Error: Wrong alignment!')

                al_item = format_str.format(item)
                al_col.append(al_item)
            al_cols.append(al_col)
        return al_cols

    def _get_header(self, headline):
        header = []
        header_overline = []
        header_underline = []

        header_widths = map(len, headline)
        widths = zip_longest(header_widths, self._col_widths, fillvalue=0)
        for header_width, col_width in widths:
            width = max(header_width, col_width)
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

    def __str__(self):
        table = [''.join(col) for col in zip(*self.cols)]
        table = '\n'.join(table)
        return table
