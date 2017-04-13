#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from tqdm import tqdm


def prepare_df(userscat_file_path, usersdoms_file_path):
    print "Load to DataFrame userscat_file_path"
    userscat = pd.read_csv(userscat_file_path,
                           header=None,
                           encoding='utf-8',
                           sep='\t',
                           skipinitialspace=True,
                           names=['uid', 'cat1', 'cat2', 'cat3', 'cat4']
                           )
    auto_users = userscat[userscat['cat1'] == 1][['uid', 'cat1']]

    print "Load to DataFrame usersdoms_file_path"
    userdom = pd.read_csv(usersdoms_file_path,
                          header=None,
                          encoding='utf-8',
                          sep='\t',
                          skipinitialspace=True,
                          names=['uid', 'domain']
                          )

    print "Preparing DataFrame"
    dom_vis_df = pd.merge(userdom, auto_users, how='left', on='uid')[['domain', 'cat1']]
    dom_vis_df['cat1'].fillna(0, inplace=True)

    return dom_vis_df


def relevant_domains(df, file_out):
    p_driver = df[df['cat1'] == 1].count()
    with open(file_out, 'w') as fout:
        for dom in tqdm(df['domain'].unique().tolist()):
            p_domain_driver = df[(df['domain'] == dom) & (df['cat1'] == 1)].count()
            p_domain = df[df['domain'] == dom].count()
            relevant_value = (p_domain_driver**2)/(p_domain*p_driver)
            fout.write((u'%s\t%.20f\n' % (dom, relevant_value[0])).encode('utf-8'))


def main():
    dom_vis_df = prepare_df('/Users/usual/PycharmProjects/first/source/lab03_users.txt',
                            '/Users/usual/PycharmProjects/first/source/111.txt')
    print dom_vis_df.shape
    relevant_domains(dom_vis_df, '/Users/usual/PycharmProjects/first/source/lab03s_domains.txt')

if __name__ == "__main__":
    main()
