from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from urllib.parse import urlparse, parse_qs, urlsplit
import requests

def getvideo():
    global video_id
    url=input('enter youtube url: ')
    print('\n===\nplease, wait...\n===\n')
    if '=' in url:
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)
        video_id = params['v'][0]
    else:
        parsed = urlsplit(url)
        video_id=parsed.path.replace('/','')

def getsubs():
    global subs
    gurl=YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    subs=formatter.format_transcript(gurl)

def punctuation():
    global response
    data = {'text': f'{subs}'}
    response = requests.post('http://bark.phon.ioc.ee/punctuator', data=data)
    print(response.text)

def savetext():
    with open ('output.txt', 'w') as f:
        f.write(response.text)
    print('\n===\ndone\n===')
    
def main():
    getvideo()
    getsubs()
    punctuation()
    savetext()

if __name__ == '__main__':
    main()