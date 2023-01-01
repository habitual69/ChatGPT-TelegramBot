FROM python:3.8

# Install the required Python libraries
RUN pip install openai pyTelegramBotAPI
RUN python -m pip install --upgrade pip



# Copy the bot code into the container
COPY bot.py /app/bot.py
COPY config.py /app/config.py

# Run the bot when the container is started
CMD python /app/bot.py
