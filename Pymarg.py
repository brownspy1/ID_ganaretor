from pypdf import PdfMerger


def marge(page_one,page_two,bordroll):
    image = [page_one, page_two]
    merger = PdfMerger()

    for pdf in image:
        merger.append(pdf)

    merger.write(f"id Card/{bordroll}.pdf")
    merger.close()
