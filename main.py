import praw, re, random

client_id = "LtH1Z5-emvHVjPYezTPA4w" 
client_secret = "xiaS24pVqwgxkxREXZQB6A2Wh4XpxA" 
username = "spaztic_monkey" 
password = "bYckok-8fitki-pahbev" 
user_agent = "SpotOfBother" 

reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     user_agent = user_agent)

subreddit = reddit.subreddit('CasualUK')

words = {
  "color": "colour",
  "cilantro": "coriander",
  "coffee": "tea",
  "eggplant": "aubergine",
  "zucchini": "courgette",
  "sidewalk": "roundabout",
  "truck": "lorry",
  "New York": "York",
  "baking soda": "bicarbonate of soda",
  "skillet": "pan",
  "gray": "grey",
  "fries": "chips",
  "garbage": "rubbish",
  "cookie": "biscuit",
  "cotton candy": "candyfloss",
  "parking lot": "car park",
  "pedophile": "paedophile",
  "armor": "armour",
  "flavor": "flavour",
  "idolize": "idolise",
  "apologize": "apologise",
  "meter": "metre",
  "luster": "lustre"
  }



for comment in subreddit.stream.comments():
  blasphemies = words.keys()
  for sin in blasphemies:
    if re.search (sin, comment.body, re.IGNORECASE):
      hailmary = words[sin]
      reprimands = (f"Sorry old chap, you said '{sin}' which is rather uncouth, I presume you meant '{hailmary}'>", f"Well I never, the nerve to say '{sin}'! Stick to '{hailmary}' in future")
      reprimand = random.choice(reprimands)
      print(reprimand)
