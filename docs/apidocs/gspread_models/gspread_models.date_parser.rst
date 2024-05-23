:py:mod:`gspread_models.date_parser`
====================================

.. py:module:: gspread_models.date_parser

.. autodoc2-docstring:: gspread_models.date_parser
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DateParser <gspread_models.date_parser.DateParser>`
     - .. autodoc2-docstring:: gspread_models.date_parser.DateParser
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DATE_FORMAT <gspread_models.date_parser.DATE_FORMAT>`
     - .. autodoc2-docstring:: gspread_models.date_parser.DATE_FORMAT
          :summary:

API
~~~

.. py:data:: DATE_FORMAT
   :canonical: gspread_models.date_parser.DATE_FORMAT
   :value: '%Y-%m-%d %H:%M:%S.%f%z'

   .. autodoc2-docstring:: gspread_models.date_parser.DATE_FORMAT

.. py:class:: DateParser
   :canonical: gspread_models.date_parser.DateParser

   .. autodoc2-docstring:: gspread_models.date_parser.DateParser

   .. py:method:: generate_timestamp()
      :canonical: gspread_models.date_parser.DateParser.generate_timestamp
      :staticmethod:

      .. autodoc2-docstring:: gspread_models.date_parser.DateParser.generate_timestamp

   .. py:method:: parse_timestamp(ts: str) -> datetime.datetime
      :canonical: gspread_models.date_parser.DateParser.parse_timestamp
      :staticmethod:

      .. autodoc2-docstring:: gspread_models.date_parser.DateParser.parse_timestamp

   .. py:method:: validate_timestamp(ts: str)
      :canonical: gspread_models.date_parser.DateParser.validate_timestamp
      :staticmethod:

      .. autodoc2-docstring:: gspread_models.date_parser.DateParser.validate_timestamp
