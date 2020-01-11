<center><h1>FACEBOOK CRAWLING BOT</h1></center>

## 1. BACKGROUND
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
> 6. SQL

## 2. WHAT THIS DOES
### 2.1. Notify shipping request posts from non-ahamove users
#### 2.1.1. Send notification via Telegram

> **NEW POST** <br>
> **Nội dung:** {post_content} <br>
> **Facebook:** {facebook_profile} <br>
> **Phone:** {phone_detected_in_content} <br>
> **Link:** {post_link} <br>
> {staff}

### 2.1.2. Save posts on Google Sheet for staff
|phone   |time               |content|post                               |profile                     |staff   |note|
|--------|-------------------|-------|-----------------------------------|----------------------------|--------|----|
|84xxxxxx|2019-12-24 14:17:00|ứng 100|https://www.facebook.com/groups/...|https://www.facebook.com/...|@quancao|good|

### 2.1.3. Save posts Google Sheet for log
|phone   |time               |content|post                               |profile                     |
|--------|-------------------|-------|-----------------------------------|----------------------------|
|84xxxxxx|2019-12-24 14:17:00|ứng 100|https://www.facebook.com/groups/...|https://www.facebook.com/...|

### 2.2. Notify shipping request posts from ahamove users via Telegram
**Filter:** Only users in their 40 days old.

> **NEW POST** <br>
> **Nội dung:** {post_content} <br>
> **Facebook:** {facebook_profile} <br>
> **Link:** {post_link} <br>
> #nophone

## 3. Store posts
All gathered posts will be stored in format of SQL in order to conduct analytic later on.

## CHANGELOG

### Version 2.1.1:
- Append site-package path to sys.path in order to run py file w/o venv.
- Set end time for script.
- Handle WebDriverException.

### Version 2.1.0:
- Posts for staff: Notify non-phone posts with hashtag #nophone.
- Blacklist keywords: mua, cáng, con chó, bàn, tủ, ghế, bắn.

### Version 2.0.0:
- Separate posts for log and posts for staff. Update posts into 2 different Google Sheets.
    - For staff:
        - Filter AhaMove users.
        - Every profile will only appear once in a day.
    - For log:
        - Keep all posts from AhaMove users and multiple posts from 1 profile.

### Verion 1.1.0:
- Slightly increase crawling speed.
- Simultaneously sync to Google Sheet to take note along side of Telegram notification.
- Remove duplicated posts within day.
- Blacklist keyword "bắn"