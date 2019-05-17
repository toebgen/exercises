#!/usr/bin/env python
import datetime
import sys
import os

import json
from tqdm import tqdm


def crawl_file_names(paths):
    dotfiles = []
    dotfiles_full_paths = []
    file_names = []
    full_paths = []
    file_names_dict = {}  # Store full path(s) for every file name

    for path in paths:
        print('Crawling through the path...', path, '\n')
        for dirpath, _, filenames in tqdm(os.walk(path), desc='os walk'):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    # if the target is a symlink (soft one), this will 
                    # dereference it - change the value to the actual target file
                    full_path = os.path.realpath(full_path)
                except (OSError,):
                    # not accessible (permissions, etc) - pass on
                    continue
                
                if filename.startswith('.'):
                    dotfiles.append(filename)
                    dotfiles_full_paths.append(full_path)
                else:
                    file_names.append(filename)
                    full_paths.append(full_path)
                    if filename not in file_names_dict:
                        file_names_dict[filename] = [full_path]
                    else:
                        # print(file_names_dict[filename])
                        file_names_dict[filename].append(full_path)
                    number_of_entries = len(file_names_dict[filename])
                    if number_of_entries > 1:
                        # print('\nfile_names_dict[filename]:', file_names_dict[filename])
                        # print('len(file_names_dict[filename]):', len(file_names_dict[filename]))
                        # print('Found', number_of_entries, 'duplicates for file', filename)
                        pass

        # Figure out duplicates
        unique_file_names = set(file_names)
        duplicate_file_names_dict = {k: v for k, v in file_names_dict.items() if len(v)>1}
        
        # Combine in one dictionary
        results = {
            'file_names': file_names,
            'unique_file_names': unique_file_names,
            'dotfiles': dotfiles,
            'dotfiles_full_paths': dotfiles_full_paths,
            'full_paths': full_paths,
            'file_names_dict': file_names_dict,
            'duplicate_file_names_dict': duplicate_file_names_dict,
        }

        # Output results
        output_folder_name = 'crawlfiles-' + path.split('/')[-2]
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

            # Write list to files for further processing
            with open(outputpath + key + '.txt', 'w') as f:
                # print('Writing', key, 'to file...')
                if isinstance(the_list, dict):
                    # dump dict as json
                    f.write(json.dumps(the_list, indent=4))
                else:
                    for item in the_list:
                        f.write("%s\n" % item)
        
        print('\n... Finished path', path, '!')
    
    print('\n... Done with all', len(paths), 'given paths!')
    return duplicate_file_names_dict
                

if sys.argv[1:]:
    duplicate_file_names_dict = crawl_file_names(sys.argv[1:])
else:
    print("Please pass the paths to check as parameters to the script")

