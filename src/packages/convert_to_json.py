import logging
import mailparser
import os
import re
from bs4 import BeautifulSoup
import json
from src import path_to_output

def parse_email_to_json(directory, ENABLE_ATTACHMENT):
    
    mail_blob = {}
    mail_blob['256Hash of mail'] = {}

    for email in os.listdir(directory):
        # Replace the name of the file with the hash of the file and iterate.
        logging.debug(f"Scanning {email}...")
        hash256email = email.replace(".elm",'')
        emailDir = os.path.join(directory, email)

        mail = mailparser.parse_from_file(emailDir)

        # Creating a key value for the headers
        logging.debug("Creating json blob.")
        mail_blob['256Hash of mail'][hash256email] = {}
        mail_blob['256Hash of mail'][hash256email]['Headers'] = mail.headers
        del mail_blob['256Hash of mail'][hash256email]['Headers']['Received']  
        mail_blob['256Hash of mail'][hash256email]['Headers']['Received'] = mail.received
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', mail.received_raw[0])
        mail_blob['256Hash of mail'][hash256email]['Headers']['SenderIP'] = ip
        mail_blob['256Hash of mail'][hash256email]['Attachments'] = mail.attachments
    
        #Build attachments in folder Attachments
        if ENABLE_ATTACHMENT is True:
            logging.debug("Extracting attachments.")
            if not os.path.exists("attachments"):
                os.makedirs("attachments")
            for attachment in mail_blob['256Hash of mail'][hash256email]['Attachments']:
                if "/" in attachment["filename"]:
                    attachment["filename"] = attachment["filename"].replace("/","?")
                mail.write_attachments("attachments/")

        # Create json key for body, then set the content of the body under content key
        body = mail.body
        mail_blob['256Hash of mail'][hash256email]['Body'] = {}
        
        # Strip html, css tags. We most likely wont need this. We only need the words, seems highly unlikely that
        # malicious payloads can be send through mail interface.
        mail_blob['256Hash of mail'][hash256email]['Body']['Content'] = clean_html(body)
        
        # Extract all links in email and save them in json.
        # Links will be saved in the body json key.
        try:
            logging.debug("Extracting links from body.")
            urls_list = []
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
            for url in urls:
                if url not in urls_list:
                    urls_list.append(url)
            mail_blob['256Hash of mail'][hash256email]['Body']['Links'] = urls_list
        except AttributeError:
            urls = None
            mail_blob['256Hash of mail'][hash256email]['Body']['Links'] = urls

     
    save_to_json(mail_blob)

def save_to_json(mail_blob):
    
    with open(f'{path_to_output}/json_data.json', 'w', encoding='utf-8') as outfile:
        logging.debug("Saving json blob to json file.")
        json.dump(mail_blob, outfile, indent=4,ensure_ascii=False)


def clean_html(string):
    logging.debug("Cleaning html tags from body.")
    return " ".join(BeautifulSoup(string, 'html.parser').text
                    .replace('\n','')
                    .replace('\t','')
                    .split())