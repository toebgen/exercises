#!/usr/bin/env python
import datetime
import sys
import os

import hashlib
import json
from tqdm import tqdm


def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk


def get_hash(filename, first_chunk_only=False, hash=hashlib.sha1):
    hashobj = hash()
    file_object = open(filename, 'rb')

    if first_chunk_only:
        hashobj.update(file_object.read(1024))
    else:
        for chunk in chunk_reader(file_object):
            hashobj.update(chunk)
    hashed = hashobj.digest()

    file_object.close()
    return hashed


def transform_to_file_hash_dict(duplicate_file_size_dict):
    file_hash_dict = {}
    for filesize, the_list in tqdm(duplicate_file_size_dict.items()):
        for full_path in the_list:
            file_hash = get_hash(full_path, first_chunk_only=True)
            if file_hash not in file_hash_dict:
                file_hash_dict[file_hash] = [full_path]
            else:
                file_hash_dict[file_hash].append(full_path)
    return file_hash_dict


def transform_to_file_size_dict(duplicate_file_names_dict):
    file_size_dict = {}
    for filename, the_list in duplicate_file_names_dict.items():
        for entry in the_list:
            full_path, filesize = entry
            if filesize not in file_size_dict:
                file_size_dict[filesize] = [full_path]
            else:
                file_size_dict[filesize].append(full_path)
    return file_size_dict


def crawl_file_names(paths):
    dotfiles = []
    dotfiles_full_paths = []
    file_names = []
    full_paths = []
    file_names_dict = {}  # Store full path(s) for every file name
    
    for path in paths:
        print('Crawling through the path...', path, '\n')
        for dirpath, _, filenames in tqdm(os.walk(path), desc='os walk'):
            # TODO Maybe skip filenames completely, start with filesizes right away
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    # if the target is a symlink (soft one), this will 
                    # dereference it - change the value to the actual target file
                    full_path = os.path.realpath(full_path)
                except (OSError,):
                    # not accessible (permissions, etc) - pass on
                    continue
                filesize = os.path.getsize(full_path)
                
                if filename.startswith('.'):
                    dotfiles.append(filename)
                    dotfiles_full_paths.append(full_path)
                else:
                    file_names.append(filename)
                    full_paths.append(full_path)
                    file_tuple = (full_path, filesize)
                    if filename not in file_names_dict:
                        file_names_dict[filename] = [file_tuple]
                    else:
                        file_names_dict[filename].append(file_tuple)
                    number_of_entries = len(file_names_dict[filename])

        # Figure out duplicate file names
        unique_file_names = set(file_names)
        duplicate_file_names_dict = {k: v for k, v in file_names_dict.items() if len(v)>1}

        # Create dict with file size as key
        duplicate_file_size_dict = transform_to_file_size_dict(duplicate_file_names_dict)
        duplicate_file_size_dict = {k: v for k, v in duplicate_file_size_dict.items() if len(v)>1}

        # Hash the remaining duplicates to check if they're the same
        duplicate_file_hash_dict = transform_to_file_hash_dict(duplicate_file_size_dict)
        duplicate_file_hash_dict = {k: v for k, v in duplicate_file_hash_dict.items() if len(v)>1}

        # Combine in one results dictionary
        results = {
            'paths': paths,
            'file_names': file_names,
            'unique_file_names': unique_file_names,
            'dotfiles': dotfiles,
            'dotfiles_full_paths': dotfiles_full_paths,
            'full_paths': full_paths,
            'file_names_dict': file_names_dict,
            'duplicate_file_names_dict': duplicate_file_names_dict,
            'duplicate_file_size_dict': duplicate_file_size_dict,
            'RESULT_duplicate_file_hash_dict': duplicate_file_hash_dict,
        }

        # Output results
        write_results(path, results)
        
        print('\n... Finished path', path, '!')
    
    print('\n... Done with all', len(paths), 'given paths!')


def write_results(path, results):
    # Output results
    path_split = list(filter(None, path.split('/')))
    output_folder_name = 'crawlfiles-' + ''.join(path_split[-2:])
    outputpath = '{prefix}/{folder_name}-{date:%Y%m%d-%H%M%S}/'.format(
        prefix='.',
        folder_name=output_folder_name,
        date=datetime.datetime.now()
    )
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    for key, the_list in results.items():
        # Print quick statistic
        print('Length of', key, ':', len(the_list))

        # Write list to files for further examination/processing
        with open(outputpath + key + '.txt', 'w') as f:
            # print('Writing', key, 'to file...')
            if isinstance(the_list, dict):
                # dump dict as json
                f.write(json.dumps(list(the_list.values()), indent=4))
            else:
                for item in the_list:
                    f.write("%s\n" % item)
                

if sys.argv[1:]:
    crawl_file_names(sys.argv[1:])
else:
    print("Please pass the paths to check as parameters to the script")

