# author: Arthur
# date: 2018.12.24

import os
import re
import datetime


ROOT = 'codewars'
README = 'README.md'


class Kata:

    folder = ''
    name = ''
    contributor = []
    count = 0
    date = '1970-01-01'
    level = 0

    def __init__(self, folder):
        self.folder = folder

    def __repr__(self):
        return 'contributors:{}, name:{}, date:{}, '.format(self.contributor, self.name, self.date)

    def normalize_contributors(self):
        self.contributor = ['DREAM' if name.endswith('Dr') else name.upper() for name in self.contributor]


def list_contributors(kata, suffix, name_extract_func):
    """ 获取某个kata文件中所有指定后缀名的作者 """
    return [name_extract_func(name.split('.')[0]) for name in os.listdir(os.path.join(ROOT, kata)) if name.endswith(suffix)]


def parse_kata_info(kata):
    """ 通过README文件获取kata的日期、难度等 """
    file = os.path.join(ROOT, kata.folder, README)
    with open(file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 0:
                kata.name = line.strip('# \n')
            if line.startswith('**日期**'):
                kata.date = re.split('[:：]', line)[-1].strip()
            if line.startswith('**等级**'):
                kata.level = re.split('[:：]', line)[-1].strip()
            if kata.date and kata.level:
                break


def collect_kata_stats():
    """ 生成统计数据字典并返回 """
    root_folder = './{}'.format(ROOT)

    # 生成kata统计字典
    katas = [Kata(folder=name) for name in os.listdir(root_folder) if os.path.isdir(os.path.join(ROOT, name))]
    for kata in katas:
        # 统计解题者
        kata.contributor = list_contributors(kata.folder, '.py', lambda x: x.split('_')[-1])
        kata.contributor.extend(list_contributors(kata.folder, '.java', lambda x: x.split('_')[-1]))
        kata.normalize_contributors()
        # 统计总人数
        kata.count = len(kata.contributor)
        # 获取kata日期信息
        parse_kata_info(kata)
    return katas


def write_stats_to_file(katas, filename):
    """ 将统计信息以markdown表格形式写入文件中 """
    stats_file = os.path.join(ROOT, filename)
    katas.sort(key=lambda x: datetime.datetime.strptime(x.date, '%Y.%m.%d'))
    contr_set = set(name for kata in katas for name in kata.contributor)
    contributors = [contributor for contributor in sorted(list(contr_set))]
    with open(stats_file, 'w+', encoding='utf-8') as f:
        f.write('# 算法题统计\n\n')
        f.write('**更新时间**：{}\n\n'.format(datetime.datetime.today().strftime('%Y.%m.%d')))
        f.write('| 时间 | 文件名 | 算法名 | 难度(越低越难) {}'.format(''.join('| %s ' % contributor for contributor in contributors)) + '|\n')
        f.write('| :---: ' * (3 + len(contributors) + 1) + '|\n')
        for kata in katas:
            attendace = ['完成' if name in kata.contributor else '-' for name in contributors ]
            f.write('| {} | {} | {} | {} {}'.format(kata.date,
                                                    kata.folder.replace('_', ' '),
                                                    kata.name,
                                                    kata.level,
                                                    ''.join('| %s ' % content for content in attendace)) + '|\n')


if __name__ == '__main__':
    katas = collect_kata_stats()
    write_stats_to_file(katas, README)





