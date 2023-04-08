# Python-Mailparser

Parse E-mails into a JSON blob that can easily be analyzed.

All the information in a header, body and attachment are put into a JSON blob, making it easier for Incident Responders
to analyze the content of an E-mail.

| Made with the Python mail-parser

## Extraction Features
These features could be helpfull to do a quick analysis on the E-mail.
- Extract URLS from body.
- Extract Sender-IP out of headers.
- Extract Attachments out of E-Mail.

## Installation

Install packages mentioned in the `requirements.txt`

```bash
pip3 install -r requirements.txt
```

## Usage

```
usage: Python Email Parser [-h] [-v] [-d DIR] [-a] [-o] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Parse emails to JSON format.

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d DIR, --dir DIR     Path to directory with emails.
  -a, --attachments     Extract attachments out of emails. Saves into attachment directory.
  -o, --output          Name of the output JSON file.
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the log level for debugging purposes. Choices: DEBUG, INFO, WARNING, ERROR, CRITICAL

Example: python3 main.py -d /home/user/emails/ -a
```
## Directory Content
The `resources` directory contains the output of the program, logs and extracted attachments.
- `attachments` contains extracted attachements
- `logs` contains logs of the mail-parser
- `out` contains the JSON files

## Example JSON
```
{
    "256Hash of mail": {
        "HASH": {
            "Headers": {
                "Return-Path": "<RETURN-PATH>",
                "X-Original-To": "EMAIL",
                "Delivered-To": "EMAIL",
                "From": "NAME <EMAIL>",
                "To": "EMAIL",
                "Subject": "SUBJECT",
                "Date": "09 Dec 2019 04:41:12 +0200",
                "Message-ID": "<MESSAGE_ID>",
                "MIME-Version": "1.0",
                "Content-Type": "text/html;\n\tcharset=\"iso-8859-1\"",
                "Content-Transfer-Encoding": "quoted-printable",
                "Received": [
                    {
                        "from": "MAIL_SERVER unknown SENDER_IP",
                        "by": "RECEIVER_MAILSERVER Postfix",
                        "with": "ESMTP",
                        "id": "EMAIL_ID",
                        "for": "<EMAIL>",
                        "date": "Tue, 09 Dec 2019 04:41:12 +0200 CEST",
                        "hop": 1,
                        "date_utc": "2019-12-09T02:41:12",
                        "delay": 0
                    }
                ],
                "SenderIP": [
                    "EXTRACTED_IP"
                ]
            },
            "Attachments": [],
            "Body": {
                "Content": "BODY_STRIPPED_FROM_HTML_TAGS",
                "Links": [
                    "LINK_0",
                    "LINK_1"
                ]
            }
        }
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.