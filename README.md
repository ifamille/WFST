WFST
====
WFST (Weighted Finite-State Transducers) is one of the best solutions for LVCSR. This toolkit is to construct a ASR decoder which is based on WFST, to recognize large vocabulary continurous Mandarin speech.

The toolkit includes:

1. pinyinStandard2Variant.py:

    input: .pys file

    output: .pyv file

2. transposeText.py

    input: text file

    output: .tt file

3. pinyinVariant2Word.py

    input: .pyv file

    output: .pyw file

4. pinyinWord2Sentence.py

    input: .pyw file

    output: .sent file

5. promptsGenerator.py

    input: .sent file

    output: prompts file

6. toneExtraction.py

    input: .pys file

    output: .tone file

Decoder Construction
====
1. Pre-processing:

1.1. Speech Transcription Construction:

Text extraction -> Stanford Segmentation -> transposeText.py -> Google Translate -> pinyinStandard2Variant.py -> pinyinVariant2Word.py -> pinyinWord2Sentence.py -> promptsGenerator.py

1.2. Lexicon Construction

... pinyinStandard2Variant.py -> pinyinVariant2Pronunciation.py -> pinyinVariant2Word -> Shell: paste -d " " .pyw .pyp > .lex

1.3. Dic

... pinyinStandard2Variant.py -> pinyinVariant2Word.py
