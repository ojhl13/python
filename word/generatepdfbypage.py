# -*- coding: utf-8 -*-
import aspose.words as aw

# load Word document
doc = aw.Document("document.docx")

# get page count
pageCount = doc.page_count

# loop through pages
for page in range(0, pageCount):
  
    # save each page as a separate document
    extractedPage = doc.extract_pages(page, 1)
    extractedPage.save(f"split_by_page_{page + 1}.pdf")