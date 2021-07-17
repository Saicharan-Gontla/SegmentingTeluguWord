# Character Segmentation of a Telugu Word
Segmenting a Word into individual Characters is called Character Segmentation. In English it is easier to segment a word but in the case of Indian languages it is difficult. This Repository contains an algorithm which segments Telugu word into individual characters.

The following are some examples.

కృష్ణదేవరాలయలు  -->  'కృ', 'ష్ణ', 'దే', 'వ', 'రా', 'ల', 'య', 'లు'

చంద్రగుప్తమౌర్య  -->  'చం', 'ద్ర', 'గు', 'ప్త', 'మౌ', 'ర్య'

రాముడు మంచి బాలుడు  -->  'రా', 'ము', 'డు', ' ', 'మం', 'చి', ' ', 'బా', 'లు', 'డు'

-------------------------

There are two different ways to segment a complex gunintham (consonant + vowel + vowel) which contains more than two vowel modifiers. First one is a normal vowel modifier and the second is one among these three ('ఁ', 'ం', 'ః'). Some of the examples are shown below.


'కాం' --> 'క' + 'ా' + 'ం' 

'క్రాం' -->  'క' + '్' + 'ర' + 'ా' + 'ం'

There are two ways to segment these complex gunintham

