# Getting started

- Create a `.env` file with your discord & teams webhook URL. Also set the website that you want to monitor
- Run the following commands

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- You may want to set up a cron jobs to run this script in a defined time interval.

### cron

Below instructions are given to run the script every 30 min, everday

- Run `crontab -e` to open crontab file for editing
- Paste the following line with correct path

```bash
*/30 * * * * /path/to/venv/bin/python /path/to/app.py
```
