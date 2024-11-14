
Usage of doc
Yogesh Google doc
<iframe src="https://docs.google.com/document/d/e/2PACX-1vRpL-zI_hT4_fO0Ut_Z99XaLsy1znL4hzYYO6w442RpXlqFEBqvEYb2N78BBy722S1YITq_l9L1SKlo/pub?embedded=true"></iframe>
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

