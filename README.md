# TG eSpeak Bot

A little telegram inline bot that implements text-to-speech functionality using [eSpeak](https://espeak.sourceforge.net/) synthesizer (also often used as a narrator in "trollge" videos)

## Installation & Deployment

### Environmental variables
- `TG_BOT_TOKEN` - Token in a format like "0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" given by BotFather. Also, don't forget to enable "Inline" mode.
- `TG_BUFFER_CHAT_ID` - A chat id, that will be used as a buffer for created voice messages - because of telegram limitations bot cannot create them directly for inline sending. Notice that the bot must have access to this chat - activated by the user or added to the group. Use your own id, if you have doubts.
### Docker
The preferable way to start because it has "batteries included". There is a Dockerfile in the repo.
1. Build
```bash
docker build . -t espeak_bot:latest
```
2. Launch
```bash
docker run -d -e TG_BOT_TOKEN="0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-k" -e TG_BUFFER_CHAT_ID=000000 espeak_bot:latest
```

### Directly

1. Install the eSpeak package. It may differ depending on your OS. On ubuntu, use ```apt-get update && apt-get install -y espeak```

2. Install bot requirements. This is a poetry project, so, if you have it installed, use
    
    ```bash
    poetry install
    ```

    Alternatively, you can install that just using pure pip (better use venv though)

    ```bash
    pip install .
    ```

3. Create environmental variables. On Linux & MacOS use:
    
    ```bash
    export TG_BOT_TOKEN="0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    export TG_BUFFER_CHAT_ID=000000
    ```

4. Launch the bot

    Using `poetry run python main.py` or just `python main.py`

## Usage

It is an inline bot, in order to use just open telegram, and type
```
@tag_of_your_bot <text you want to voice out>
```
Then select voice message from the drop-out menu.

You can use ALL CAPS TEXT to voice out it with a lower voice.
