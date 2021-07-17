from SegmentWord import Segment

segment = Segment()

word_list = ['కృష్ణదేవరాలయలు', 'చంద్రగుప్త మౌర్య', 'రాముడు మంచి బాలుడు']

for word in word_list:
    print(segment.extract(word))
