from gtts import gTTS
import os

# 1. Enter your text here
poem = """
If I had a shiny gun,
I could have a world of fun
Speeding bullets through the brains
Of the folk who give me pains;

Or had I some poison gas,
I could make the moments pass
Bumping off a number of
People whom I do not love.

But I have no lethal weapon-
Thus does Fate our pleasure step on!
So they still are quick and well
Who should be, by rights, in hell.
"""

print("Generating speech audio... this may take a few seconds.")

# 2. Convert text to speech (we use 'en' for English, 'tld' sets the accent)
# tld='co.uk' makes it a British accent, change to 'com' for American
tts = gTTS(text=poem, lang='en', tld='co.uk', slow=False)

# 3. Save the file directly into your commit_merge folder!
output_path = "commit_merge/poem_speech.mp3"
tts.save(output_path)

print(f"Success! Your audio file is saved at: {output_path}")
