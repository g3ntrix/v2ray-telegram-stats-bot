# V2Ray Server Statistics Telegram Bot

This Telegram bot is designed to fetch and display user statistics related to network usage on V2Ray servers. Built using [Pyrogram](https://github.com/pyrogram/pyrogram), this bot works seamlessly with multiple V2Ray servers and their SQLite databases.

## Features

- Compatible with multiple V2Ray servers.
- Automatically processes SQLite databases transferred via SCP.
- Fetches and displays detailed user statistics:
  - Download
  - Upload
  - Total usage
  - Remaining data
  - Expiry information

## Architecture

Databases from multiple V2Ray servers are sent to a centralized server using SCP and collected in a specific folder. These databases are updated every minute via a cronjob. The bot then processes these databases to fetch user statistics.

## Requirements

- Python 3.x
- Pyrogram
- SQLite3
- An active Telegram Bot token
- An API ID and a HASH ID
- SCP and Cronjob setup for database transfer

## Installation & Setup

1. Clone the repository
    ```
    git clone https://github.com/your_username/your_repository_name.git
    ```

2. Navigate to the directory
    ```
    cd your_repository_name
    ```

3. Install the required Python packages
    ```
    pip install pyrogram
    ```

4. Create a `.env` file to store sensitive information like Telegram Bot Token, API ID, and API hash, or input them directly into the Python script.

5. Run the script
    ```
    python your_script_name.py
    ```

## Usage

- Start the Telegram bot.
- Use `/stats` command to initiate the bot.
- You will be prompted to send your configuration URI.
- The bot will then fetch and display your statistics.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

Licensed under the Mozilla Public License 2.0. See the `LICENSE` file for more details.

## Contact

If you have any questions, feel free to [contact me](mailto:your_email_here).

## Acknowledgments

- Thanks to [Pyrogram](https://github.com/pyrogram/pyrogram) for their robust API.
