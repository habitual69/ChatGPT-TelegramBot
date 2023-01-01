import openai
import telebot
from config import YOUR_TBOT_TOKEN, YOUR_OAPI_KEY


# Initialize the ChatGPT and DALL-E models
openai.api_key = YOUR_OAPI_KEY
model_engine = "text-davinci-002"

# Create a TeleBot instance
bot = telebot.TeleBot(YOUR_TBOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(message.chat.id, """
                   <b>Hi!</b> I'm a bot that uses the <b>ChatGPT</b> and <b>DALL-E</b> language models to generate responses to your messages. To get started, just send me a /help to get the list of all the command(s)""", parse_mode='html')
  
@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    if "help" in message.text.lower():
        bot.send_message(message.chat.id, """
Here are the Available command(s)
<b>1: /Start to start the bot</b>
<b>2: /help to get this help text again</b>
<b>3: /generate_image to generate image based of description</b>                        
<i>Note: This bot is still in beta phase and is available for free only for testing purposes.</i>

\n<pre>This bot is createb by</pre> <b>Arbind Singh</b>
<b>Follow me on</b> <a href='https://github.com/habitual69'>Github</a>
""",parse_mode='html')
        
    # Check if the user is requesting an image
    elif "generate_image" in message.text.lower():
        # Use the DALL-E model to generate an image
        image_url = openai.Image.create(
        prompt=f"{message.text}",
        size="1024x1024",
        n=1,
        response_format="url"
        ).data[0].url
        bot.send_photo(message.chat.id, image_url)
    else:
    # Use the ChatGPT model to generate a response
        response = openai.Completion.create(
        engine=model_engine,
        prompt=f"User: {message.text}\nBot: ",
        max_tokens=2048,
        n=1,
        temperature=0.5,
        ).choices[0].text

        # Send the generated response to the user
        bot.send_message(message.chat.id, response)

def run_bot():
    try:
        # Start the bot
        bot.polling()
    except Exception as e:
        # If the bot crashes, print the error message and start the bot again
        print(e)
        run_bot()

# Run the bot indefinitely
while True:
    run_bot()
