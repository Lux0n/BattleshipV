import sys

for arg in sys.argv:
    if len(sys.argv) >= 2:
        print ('Hello '+sys.argv[1]+'!',sep='')
        break
    else:
        print ('Hello World!')