import os
import datetime
import pathlib
from time import time
from PyPDF2 import PdfFileMerger


def all_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


if __name__ == '__main__':
    s = input("Dir: ")
    rootDir = s.strip('\"')
    start = time()

    todaydetail = datetime.datetime.today()
    datetime = todaydetail.strftime("%Y%m%d%H%M%S")

    cwd = os.getcwd()
    resultFile = str(pathlib.Path(cwd).joinpath('merge_' + datetime + '.pdf'))

    pdfs = []

    merger = PdfFileMerger()

    for i in all_files(rootDir):
        file_p = pathlib.Path(i)
        if file_p.suffix == ".pdf":
            print(file_p)
            merger.append(i)

    merger.write(resultFile)
    merger.close()

    print('\nDone!')
    print('{}s'.format(time() - start))
