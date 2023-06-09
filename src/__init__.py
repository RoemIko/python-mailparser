from os import path, makedirs

path_of_project_root = path.dirname(path.dirname(path.abspath(__file__)))
path_to_src = path.join(path_of_project_root, 'src')
path_to_resources = path.join(path_of_project_root, 'resources')
path_to_output = path.join(path_to_resources, 'out')
path_to_logs = path.join(path_to_resources, 'logs')
path_to_attachments = path.join(path_to_resources, 'attachments')

if not path.exists(path_to_logs):
    makedirs(path_to_logs)
if not path.exists(path_to_output):
    makedirs(path_to_output)
if not path.exists(path_to_attachments):
    makedirs(path_to_attachments)

