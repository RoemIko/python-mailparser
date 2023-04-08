from typing import *
import argparse
import src.helpers.logger as logger
from src.packages.convert_to_json import parse_email_to_json

def main(directory, ENABLE_ATTACHMENT):
    parse_email_to_json(directory=directory, ENABLE_ATTACHMENT=ENABLE_ATTACHMENT)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'Python Email Parser',
                    description = 'Parse emails to JSON format.',
                    epilog = 'Example: python3 main.py -d /home/user/emails/ -a')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-d', '--dir', help='Path to directory with emails.')
    parser.add_argument('-a', '--attachments', help='Extract attachments out of emails. Saves into attachment directory.', action='store_true')
    parser.add_argument("-l", "--loglevel", help="Set the log level for debugging purposes. " \
                        "Choices: DEBUG, INFO, WARNING, ERROR, CRITICAL", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        required=False, default='INFO')
    args = parser.parse_args()

    if args.dir:
        directory = args.dir
    else:
        print("No directory specified. Use -d or --dir to specify a directory.")
        exit()
        
    if args.attachments:
        ENABLE_ATTACHMENT = True
    else:
        ENABLE_ATTACHMENT = False
        
    if args.loglevel:
        loglevel = args.loglevel
    else:
        loglevel = 'INFO'
        
    logger.Logger('root', loglevel)
    main(directory=directory, ENABLE_ATTACHMENT=ENABLE_ATTACHMENT)

