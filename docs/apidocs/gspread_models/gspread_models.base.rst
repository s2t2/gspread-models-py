:py:mod:`gspread_models.base`
=============================

.. py:module:: gspread_models.base

.. autodoc2-docstring:: gspread_models.base
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BaseModel <gspread_models.base.BaseModel>`
     - .. autodoc2-docstring:: gspread_models.base.BaseModel
          :summary:

API
~~~

.. py:class:: BaseModel(attrs: typing.Dict)
   :canonical: gspread_models.base.BaseModel

   .. autodoc2-docstring:: gspread_models.base.BaseModel

   .. rubric:: Initialization

   .. autodoc2-docstring:: gspread_models.base.BaseModel.__init__

   .. py:attribute:: SHEET_NAME
      :canonical: gspread_models.base.BaseModel.SHEET_NAME
      :value: None

      .. autodoc2-docstring:: gspread_models.base.BaseModel.SHEET_NAME

   .. py:attribute:: COLUMNS
      :canonical: gspread_models.base.BaseModel.COLUMNS
      :value: []

      .. autodoc2-docstring:: gspread_models.base.BaseModel.COLUMNS

   .. py:attribute:: SEEDS
      :canonical: gspread_models.base.BaseModel.SEEDS
      :value: []

      .. autodoc2-docstring:: gspread_models.base.BaseModel.SEEDS

   .. py:attribute:: service
      :canonical: gspread_models.base.BaseModel.service
      :value: None

      .. autodoc2-docstring:: gspread_models.base.BaseModel.service

   .. py:property:: created_at
      :canonical: gspread_models.base.BaseModel.created_at

      .. autodoc2-docstring:: gspread_models.base.BaseModel.created_at

   .. py:method:: __iter__()
      :canonical: gspread_models.base.BaseModel.__iter__

      .. autodoc2-docstring:: gspread_models.base.BaseModel.__iter__

   .. py:property:: row
      :canonical: gspread_models.base.BaseModel.row
      :type: typing.List

      .. autodoc2-docstring:: gspread_models.base.BaseModel.row

   .. py:method:: bind(document_id, credentials_filepath=None, credentials=None, creds=None)
      :canonical: gspread_models.base.BaseModel.bind
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.bind

   .. py:method:: get_sheet() -> gspread.Worksheet
      :canonical: gspread_models.base.BaseModel.get_sheet
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.get_sheet

   .. py:property:: sheet
      :canonical: gspread_models.base.BaseModel.sheet
      :classmethod:
      :type: gspread.Worksheet

      .. autodoc2-docstring:: gspread_models.base.BaseModel.sheet

   .. py:method:: find(by_id)
      :canonical: gspread_models.base.BaseModel.find
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.find

   .. py:method:: all()
      :canonical: gspread_models.base.BaseModel.all
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.all

   .. py:method:: destroy_all()
      :canonical: gspread_models.base.BaseModel.destroy_all
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.destroy_all

   .. py:method:: where(**kwargs)
      :canonical: gspread_models.base.BaseModel.where
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.where

   .. py:method:: create_all(new_records: typing.List[typing.Dict], records=[])
      :canonical: gspread_models.base.BaseModel.create_all
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.create_all

   .. py:method:: create(new_record: dict)
      :canonical: gspread_models.base.BaseModel.create
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.create

   .. py:method:: seed()
      :canonical: gspread_models.base.BaseModel.seed
      :classmethod:

      .. autodoc2-docstring:: gspread_models.base.BaseModel.seed
