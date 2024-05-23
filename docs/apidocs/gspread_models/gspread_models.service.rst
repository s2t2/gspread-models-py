:py:mod:`gspread_models.service`
================================

.. py:module:: gspread_models.service

.. autodoc2-docstring:: gspread_models.service
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SpreadsheetService <gspread_models.service.SpreadsheetService>`
     -

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DEFAULT_FILEPATH <gspread_models.service.DEFAULT_FILEPATH>`
     - .. autodoc2-docstring:: gspread_models.service.DEFAULT_FILEPATH
          :summary:
   * - :py:obj:`GOOGLE_CREDENTIALS_FILEPATH <gspread_models.service.GOOGLE_CREDENTIALS_FILEPATH>`
     - .. autodoc2-docstring:: gspread_models.service.GOOGLE_CREDENTIALS_FILEPATH
          :summary:
   * - :py:obj:`GOOGLE_SHEETS_DOCUMENT_ID <gspread_models.service.GOOGLE_SHEETS_DOCUMENT_ID>`
     - .. autodoc2-docstring:: gspread_models.service.GOOGLE_SHEETS_DOCUMENT_ID
          :summary:

API
~~~

.. py:data:: DEFAULT_FILEPATH
   :canonical: gspread_models.service.DEFAULT_FILEPATH
   :value: 'join(...)'

   .. autodoc2-docstring:: gspread_models.service.DEFAULT_FILEPATH

.. py:data:: GOOGLE_CREDENTIALS_FILEPATH
   :canonical: gspread_models.service.GOOGLE_CREDENTIALS_FILEPATH
   :value: 'getenv(...)'

   .. autodoc2-docstring:: gspread_models.service.GOOGLE_CREDENTIALS_FILEPATH

.. py:data:: GOOGLE_SHEETS_DOCUMENT_ID
   :canonical: gspread_models.service.GOOGLE_SHEETS_DOCUMENT_ID
   :value: 'getenv(...)'

   .. autodoc2-docstring:: gspread_models.service.GOOGLE_SHEETS_DOCUMENT_ID

.. py:class:: SpreadsheetService(credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH, document_id=GOOGLE_SHEETS_DOCUMENT_ID, creds=None, credentials=None)
   :canonical: gspread_models.service.SpreadsheetService

   Bases: :py:obj:`gspread_models.date_parser.DateParser`

   .. py:method:: doc() -> gspread.Spreadsheet
      :canonical: gspread_models.service.SpreadsheetService.doc

      .. autodoc2-docstring:: gspread_models.service.SpreadsheetService.doc

   .. py:property:: sheets
      :canonical: gspread_models.service.SpreadsheetService.sheets
      :type: typing.List[gspread.Worksheet]

      .. autodoc2-docstring:: gspread_models.service.SpreadsheetService.sheets

   .. py:method:: get_sheet(sheet_name) -> gspread.Worksheet
      :canonical: gspread_models.service.SpreadsheetService.get_sheet

      .. autodoc2-docstring:: gspread_models.service.SpreadsheetService.get_sheet

   .. py:method:: find_or_create_sheet(sheet_name) -> gspread.Worksheet
      :canonical: gspread_models.service.SpreadsheetService.find_or_create_sheet

      .. autodoc2-docstring:: gspread_models.service.SpreadsheetService.find_or_create_sheet
