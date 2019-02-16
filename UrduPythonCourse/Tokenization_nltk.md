## How Text Tokenization Works
Tokenization is a way to split text into tokens. These tokens could be paragraphs, sentences, or individual words. NLTK provides a number of tokenizers in the tokenize module. This demo shows how 5 of them work.

The text is first tokenized into sentences using the **PunktSentenceTokenizer**. Then each sentence is tokenized into words using 4 different word tokenizers:

- **TreebankWordTokenizer**
- WordPunctTokenizer
- **PunctWordTokenizer**
- WhitespaceTokenizer

The pattern tokenizer does its own sentence and word tokenization, and is included to show how this library tokenizes text before further parsing.