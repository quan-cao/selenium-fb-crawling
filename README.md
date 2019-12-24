# selenium-fb-crawling

# 1. Background
An Python program which helps finding customers for AhaMove sales team.<br>
Automatically look for shipping request posts in pre-defined groups and notify staffs via Telegram.<br>
Staff will be assign using Telegram Username (Ex: @quancao). Therefore, please make sure all staffs have Username on Telegram.<br>
Posts will be simultaneously logged on Google Sheet.

**Skills involved:**
> 1. Python
> 2. Multi-threading
> 3. Selenium
> 4. Google Sheet API
> 5. Telegram API

# 2. Content
## 2.1. Content on Telegram

> **NEW POST** <br>
> **Nội dung:** {post_content} <br>
> **Facebook:** {facebook_profile} <br>
> **Phone:** {phone_detected_in_content} <br>
> **Link:** {post_link} <br>
> {staff}

## 2.2. Content on Google Sheet for staff
|phone   |time               |content|post                               |profile                     |staff   |note|
|--------|-------------------|-------|-----------------------------------|----------------------------|--------|----|
|84xxxxxx|2019-12-24 14:17:00|ứng 100|https://www.facebook.com/groups/...|https://www.facebook.com/...|@quancao|good|

## 2.3. Content on Google Sheet for log
|phone   |time               |content|post                               |profile                     |
|--------|-------------------|-------|-----------------------------------|----------------------------|
|84xxxxxx|2019-12-24 14:17:00|ứng 100|https://www.facebook.com/groups/...|https://www.facebook.com/...|

# UPDATE LOG

## Verion Beta 1.1:
- Slightly increase crawling speed.
- Simultaneously sync to Google Sheet to take note along side of Telegram notification.
- Remove duplicated posts within day.
- Blacklist keyword "bắn"

## Version Beta 2.0:
- Separate posts for log and posts for staff. Update posts into 2 different Google Sheets.
    - For staff:
        - Filter AhaMove users.
        - Every profile will only appear once in a day.
    - For log:
        - Keep all posts from AhaMove users and multiple posts from 1 profile.