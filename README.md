# V2Ray Server Stats Bot

A Telegram bot for fetching and displaying stats from a V2Ray server database. Supports multiple servers and designed to work with databases that are collected on a server using the `scp` command and cronjobs.

![Mozilla Public License 2](https://img.shields.io/badge/license-MPL2-blue.svg)

## Features

- Fetch Download/Upload Stats
- Remaining Data Information
- Expiry Time and Days Left
- Works with multiple databases
- Automatically processes newly collected databases


## Screenshots

<p float="left">
  <img src="screenshots/Client%20View" width="400" />
  <figcaption>Client View.jpg</figcaption>
  <img src="screenshots/Console%20View" width="400" />
  <figcaption>Console View.jpg</figcaption>
</p>


## Requirements

- Python 3.x
- pyrogram
- sqlite3
- An API ID and a HASH ID from Telegram

## Installation and Setup

1. Clone the repository:

    ```
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory and install the required packages:

    ```
    pip install -r requirements.txt
    ```

3. Add your `API ID` and `HASH ID` into the designated places in the code.

4. Run the bot:

    ```
    python main.py
    ```

## Usage

Send the `/stats` command to the bot to fetch the server statistics.

## License

This project is licensed under the Mozilla Public License 2.0 - see the [LICENSE](LICENSE) file for details.
