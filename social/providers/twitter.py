import datetime

import requests
from requests.exceptions import HTTPError

from social.models import Message
from social.providers.base import Provider


class TwitterProvider(Provider):
    def __init__(self, provider):
        super().__init__(provider)
        self.access_token = None
        self.auth()

    def auth(self):
        auth_req = requests.post("https://api.twitter.com/oauth2/token",
                                 auth=(self.provider.app_id, self.provider.app_secret),
                                 data={'grant_type': 'client_credentials'}).json()
        if 'error' in auth_req:
            raise Exception('Cannot login to Twitter')
        self.access_token = auth_req['access_token']

    def fetch_messages(self, feed, **kwargs):
        try:
            last_message = feed.messages.filter(provider=self.provider).order_by('published_at').last()
            if last_message is None:
                last_id = None
            else:
                last_id = last_message.provider_post_id

            results = requests.get("https://api.twitter.com/1.1/search/tweets.json", params={
                'q': '%23{}'.format(feed.hashtag),
                'count': '100',
                'since_id': last_id,
                'entities': True
            }, headers={"Authorization": "Bearer {}".format(self.access_token)}).json()
            messages = []
            for tweet in results['statuses']:
                message = Message()
                message.author_name = tweet['user']['name']
                message.author_picture = tweet['user']['profile_image_url_https'].replace('_normal', '')
                message.author_username = "@{}".format(tweet['user']['screen_name'])
                content = tweet['text']
                if 'extended_entities' in tweet:
                    for media in tweet['extended_entities']['media']:
                        if media['type'] == 'photo':
                            message.image = media['media_url_https']
                        if media['type'] in ('animated_gif', 'video'):
                            variants = media['video_info']['variants']
                            # Select the MP4 with the best bitrate
                            mp4 = [variant for variant in variants if variant['content_type'] == 'video/mp4']
                            if len(mp4) > 0:
                                best_bitrate = max(mp4, key=lambda item: item['bitrate'])
                                message.video = best_bitrate['url']
                                if media['type'] == 'animated_gif':
                                    message.video_is_gif = True
                message.text = content
                import pytz
                locale = pytz.utc
                message.published_at = locale.localize(datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
                message.provider = self.provider
                message.provider_post_id = tweet['id_str']
                message.feed = feed
                messages.append(message)
                message.save()
            return messages
        except HTTPError:
            self.auth()
            return self.fetch_messages(feed, **kwargs)

