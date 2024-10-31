# YouTube-Transcript-Extractor

This project includes a straightforward and functional Python script that automates the process of fetching transcripts from YouTube videos. The script takes a YouTube URL as an input, extracts the video transcript, punctuates it using an external API, and saves the result as a text file. It uses the [youtube_transcript_api](https://github.com/jdepoix/youtube-transcript-api) package for transcript retrieval and the [Bark Punctuator](https://github.com/chrisspen/punctuator2) API for punctuating the transcripts.

The extracted transcript is then processed further to make it more readable and editable. For this, the Natural Language Toolkit [NLTK](https://github.com/nltk/nltk) is employed. The resulting formatted and punctuated transcript is finally saved as a text file, providing a ready-to-use document for further uses like analysis, translation, etc.

![ss](https://i.imgur.com/TvQPuWD.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:
```bash
requests
youtube_transcript_api
nltk==3.8.1
```
Also, make sure to download NLTK's tokenizers before you can use them. This can be done by running the following Python command:
```bash
nltk.download('punkt')
```
