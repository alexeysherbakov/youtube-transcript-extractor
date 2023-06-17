from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import urllib
import urllib.request
from urllib.parse import urlparse, parse_qs, urlsplit
import requests
import nltk
import json

# nltk.download('punkt')

class GetYouTubeSubs:
    def __init__(self):
        self.video_id = None
        self.video_title = None
        self.subs = None
        self.response = None
    
    def getvideo(self):
        url=input('enter youtube url: ')
        print('\n===\nplease, wait...\n===\n')
        if '=' in url:
            parsed_url = urlparse(url)
            params = parse_qs(parsed_url.query)
            self.video_id = params['v'][0]
        else:
            parsed = urlsplit(url)
            self.video_id=parsed.path.replace('/','')
    
    def gettitle(self):
        params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % self.video_id}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            self.video_title=data['title']

    def getsubs(self):
        gurl=YouTubeTranscriptApi.get_transcript(self.video_id)
        formatter = TextFormatter()
        self.subs=formatter.format_transcript(gurl)

    def punctuation(self):
        data = {'text': self.subs}
        try:
            self.response = requests.post('http://bark.phon.ioc.ee/punctuator', data=data)
        except Exception as e:
            print(e)
        for r in ['[  ]', '[,', '. ]', '[ Music ]']:
            self.response.text.replace(r, '')

    def savetext(self):
        safe_title = "".join(c for c in self.video_title if c.isalnum() or c.isspace())
        sentences = nltk.tokenize.sent_tokenize(self.response.text)
        with open(f'{safe_title}.txt', 'w+') as file:
            for i in range(0, len(sentences), 5):
                file.write(' '.join(sentences[i:i+5]) + '\n' + '\n')
            file.seek(0)
            print(file.read())
        print('\n===\ndone\n===\n')
    
def main():
    gyts=GetYouTubeSubs()
    gyts.getvideo()
    gyts.gettitle()
    gyts.getsubs()
    gyts.punctuation()
    gyts.savetext()

if __name__ == '__main__':
    main()
