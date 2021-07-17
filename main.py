from SegmentWord import Segment

segment = Segment()

word_list = ['కృష్ణదేవరాయలు', 'చంద్రగుప్త మౌర్య', 'రాముడు మంచి బాలుడు','కుంతి', 'కాండౌన్']

for word in word_list:
    ExtractedWord = segment.extract(word,1)
    print (ExtractedWord)