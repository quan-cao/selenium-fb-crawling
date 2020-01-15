## Version 2.1.2:
- Handle Facebook changing login screen.

## Version 2.1.1:
- Append site-package path to sys.path in order to run py file w/o venv.
- Set end time for script.
- Handle WebDriverException.

## Version 2.1.0:
- Posts for staff: Notify non-phone posts with hashtag #nophone.
- Blacklist keywords: mua, cáng, con chó, bàn, tủ, ghế, bắn.

## Version 2.0.0:
- Separate posts for log and posts for staff. Update posts into 2 different Google Sheets.
    - For staff:
        - Filter AhaMove users.
        - Every profile will only appear once in a day.
    - For log:
        - Keep all posts from AhaMove users and multiple posts from 1 profile.

## Version 1.1.0:
- Slightly increase crawling speed.
- Simultaneously sync to Google Sheet to take note along side of Telegram notification.
- Remove duplicated posts within day.
- Blacklist keyword "bắn"

## Version 1.0.0:
- Beta released