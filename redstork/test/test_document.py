from redstork import Document
from redstork.test import res
import tempfile


def test_document():
    doc = Document(res('sample.pdf'))

    assert len(doc) == 15

    assert doc.meta['Title'] == 'Red Stork'


def test_document_save():

    with tempfile.TemporaryDirectory() as d:
        doc = Document(res('sample.pdf'))
        fname = f'{d}/temp.pdf'
        doc.save(fname)

        doc2 = Document(fname)

        assert len(doc) == len(doc2)
        assert doc2.meta['Title'] == 'Red Stork'