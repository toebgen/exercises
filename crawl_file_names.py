#!/usr/bin/env python
import datetime
import sys
import os

from tqdm import tqdm


def crawl_file_names(paths):
    dotfiles = []
    dotfiles_full_paths = []
    file_names = []
    full_paths = []
    for path in paths:
        print('Crawling through the path...')
        for dirpath, dirnames, filenames in tqdm(os.walk(path), desc='os walk'):
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

        # Figure out duplicates
        unique_file_names = set(file_names)

        # Combine in one dictionary
        results = {
            'file_names': file_names,
            'unique_file_names': unique_file_names,
            'dotfiles': dotfiles,
            'dotfiles_full_paths': dotfiles_full_paths,
            'full_paths': full_paths,
        }

        # Output results
        newpath = '{prefix}/crawl-files-{date:%Y-%m-%d-%H-%M-%S}/'.format(prefix=path, date=datetime.datetime.now())
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        for key, the_list in tqdm(results.items(), desc='results output'):
            # Print quick statistic
            print('Number of', key, ':', len(the_list))

            # Write list to files for further processing
            with open(newpath + key + '.txt', 'w') as f:
                # print('Writing', key, 'to file...')
                for item in the_list:
                    f.write("%s\n" % item)
        
        print('Finished!')
                

if sys.argv[1:]:
    crawl_file_names(sys.argv[1:])
else:
    print("Please pass the paths to check as parameters to the script")

