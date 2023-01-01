# **ChatGPT Bot**

This is a Python bot that uses the ChatGPT language model to generate responses to user messages.

## **Prerequisites**

- Python 3.8 or later
- An OpenAI API key (**[https://openai.com/](https://openai.com/)**)
- A Telegram bot token (**[https://core.telegram.org/bots](https://core.telegram.org/bots)**)

## **Installing**

1. Clone this repository:

```
git clone https://github.com/YOUR_USERNAME/chatgpt-bot.git
```

1. Navigate to the project directory:

```
cd chatgpt-bot
```

2. Install the required Python libraries:

```
pip install -r requirements.txt
```

3. Create a **`config.py`** file in the project directory with the following contents:

```
API_KEY = "YOUR_API_KEY"
BOT_TOKEN = "YOUR_BOT_TOKEN"
```

Replace **`YOUR_API_KEY`** with your OpenAI API key, and **`YOUR_BOT_TOKEN`** with the token for your Telegram bot.

## **Running the bot**

To run the ChatGPT bot, simply run the following command:

```
python bot.py
```

The bot will start running and will be accessible via Telegram as usual.

## **Deploying with Docker**

You can also use Docker to deploy the ChatGPT bot. To do so, follow these steps:

1. Build the Docker image:

```
docker build -t chatgpt-bot .
```

2. Run the Docker container:

```
docker run -d chatgpt-bot
```

This will start the ChatGPT bot in a Docker container, which you can then access via Telegram as usual.

## **License**

This project is licensed under the MIT License - see the **[LICENSE](https://chat.openai.com/chat/LICENSE)** file for details.
