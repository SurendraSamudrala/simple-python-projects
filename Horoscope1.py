n=input('Horoscope name: ')
Horoscope_description={"Aries": "The passionate pioneer, always charging ahead.",
"Taurus":"The grounded realist, seeking stability and comfort.",
"Gemini": "The curious communicator, always on the go.",
"Cancer": "The nurturing empath, deeply emotional and protective.",
"Leo": "The confident leader, seeking attention and admiration.",
"Virgo":"The analytical perfectionist, always striving for improvement.",
"Libra":"The harmonious diplomat, seeking balance and beauty.",
"Scorpio": "The intense and mysterious, passionate and complex.",
"Sagittarius": "The adventurous philosopher, seeking truth and freedom.",
"Capricorn":"The ambitious and disciplined, climbing to the top.",
"Aquarius": "The unconventional thinker, breaking rules and challenging norms.",
"Pisces": "The imaginative dreamer, lost in their own world."}
if n in Horoscope_description:
    print(Horoscope_description[n])
else:
    print('Invalid horoscope name')