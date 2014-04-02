__author__ = 'mathfac'

import sys
import re

sys.stdin = open(sys.argv[1])
sys.stdout = open(sys.argv[2], 'w')

tex = "".join(line for line in sys.stdin)


for bibitem in tex.split("\\bibitem")[1:]:
    blocks = re.split( r"\n* *\\newblock *\n*", bibitem)


    key = re.match( r'\{(.*?)\}', bibitem).group(1)
    authors = re.split("\} *", blocks[0])[1]
    authors = re.sub("(\{\\\em *)|\}|\\n", "", authors)
    authors = re.sub("  *", " ", authors)
        #replace("{\em ", "").replace("\n", "")\
        #.replace("}", "")
    #.replace(",", " and")

    authors = re.split(", ?", authors)

    for id, author in enumerate(authors):
        names = re.split("\. |  ?|\.", author)
        author = names[1]
        for name in names[2:]:
            author += ". " + name
        authors[id] = author + names[0]

    authors = " and ".join(authors)
    title = blocks[1]
    #print blocks[1]
    press = re.split("\n?  *-?-  *\n?", blocks[2])
    rest_id = 1
    if press[0] != "":
        journal = press[0]
    else:
        journal = press[1]
        rest_id = 2
    journal = re.sub(".$|\n|-- ", "", journal)

    rest = "-".join(press[id] for id in range(rest_id, len(press)))

    try:
        year = re.match("\d{4}", rest).group()
    except:
        year = ""

    rest = re.sub(year, "", rest)

    res = re.findall(r"(v|N)(.*?)(\d{1,4})", rest)
    if (res is not None) and (len(res) > 0):
        volume = res[len(res) - 1][2]
    else:
        volume = ""
    rest = re.sub(r"(v|N)(.*?)" + volume, "", rest)

    #print rest
    pages = re.findall(r"(\d{1,3}) ?--? ?(\d{1,3})", rest)
    #print pages
    if (pages is not None) and (len(pages) > 0):
        pages = pages[len(pages) - 1][0] + "--" + pages[len(pages) - 1][1]
    else:
        pages = re.findall(r"(\d{1,3})", rest)
        #print pages
        if (pages is not None) and (len(pages) > 0):
            pages = pages[len(pages) - 1]
        else:
            pages = ""



    print "@ARTICLE{" + key + ",\n" \
                                "author       = \"" + authors + "\",\n"\
                                "title        = \"" + title + "\",\n"\
                                "journal      = \"" + journal + "\","
    if volume != "":
        print                   "volume       = \"" + volume + "\","
    if year != "":
        print                   "year         = \"" + year + "\","
    if pages != "":
        print                   "pages        = \"" + pages + "\","

    if title[0] > "z":
        print                   "language     = \"russian\""
    else:
        print                   "language     = \"english\""

    print "}\n"
