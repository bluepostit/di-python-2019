# Finding a profile
def find_profile(username):
    user_profile = {}
    for profile in profiles:
        if profile['username'] == username:
            user_profile = profile

    return user_profile


# Profile list
profiles = [
  {
    'id': 1,
    'username': 'frank_s',
    'first_name': 'Frank',
    'last_name': 'Sinatra',
    'picture': 'http://www.bohemiaticket.cz/photos/db/57/db57d4caf42e8d79b3e3b891d510bf3e-7324-750x450-fit.jpg',
    'friends': [2, 5, 9],
  },
  {
    'id': 2,
    'username': 'miles_d',
    'first_name': 'Miles',
    'last_name': 'Davis',
    'picture': 'https://img.discogs.com/saz25T9xJgOthJLeH0-lQg7jk34=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/A-23755-1394387343-4500.jpeg.jpg',
    'friends': [1, 5, 9],
  },
  {
    'id': 5,
    'username': 'vicky_d',
    'first_name': 'Vic',
    'last_name': 'Damone',
    'picture': 'https://www.washingtonpost.com/resizer/d9vDql2uOfEASSSp_9amBMdFtcA=/480x0/arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/GZL4SLAQDYI6RDVBYHMR7TWD7Y.jpg',
    'friends': [1, 2, 9],
  },
  {
    'id': 9,
    'username': 'tony_b',
    'first_name': 'Tony',
    'last_name': 'Benett',
    'picture': 'https://pbs.twimg.com/profile_images/1027596542901972997/OTwYIp_O_400x400.jpg',
    'friends': [2, 5, 1],
  },
]
