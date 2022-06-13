import time
from typing import Union, Any, List, Tuple
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import PageElement, ResultSet


# def get_giant_list() -> List[Tuple[str, str]]:
#     html = urlopen("https://www.marxists.org/chinese/index.html")
#     html_text: str = bytes.decode(html.read(), encoding='GBK')
#     html_context: BeautifulSoup = BeautifulSoup(html_text, 'html.parser')
#     result = []
#     for giant in html_context.body.div.find_next('div').find_all('a'):
#         result.append((giant.string, "https://www.marxists.org/chinese/" + giant['href']))
#     return result

def get_engels() -> List[Tuple[str, str]]:
    html = urlopen('https://www.marxists.org/chinese/engels/index.htm')
    text: str = bytes.decode(html.read(), encoding='GBK')
    context: BeautifulSoup = BeautifulSoup(text, 'html.parser')
    result = []
    for paper in context.body.pre.find_all('a'):
        if 'PDF' in paper.string or 'CHM' in paper.string:
            continue
        if paper['href'].endswith('pdf'):
            continue
        if paper['href'].endswith('chm'):
            continue
        result.append((paper.string, 'https://www.marxists.org/chinese/engels/' + paper['href']))
    return result


def write_engels():
    engels_paper_list: List[Tuple[str, str]] = get_engels()
    counter = 1
    for paper in engels_paper_list:
        if paper is None or paper[0] is None or paper[1] is None:
            print('Invalid url pair, skipped')
            counter += 1
            continue

        try:
            html = urlopen(paper[1])
            context: BeautifulSoup = BeautifulSoup(bytes.decode(html.read(), encoding='GBK'), 'html.parser')
            text = context.get_text()

            f = open('恩格斯-' + paper[0] + '.txt', 'w')
            f.write(paper[0])
            f.write('\n')
            f.write('恩格斯')
            f.write('\n')
            f.write(paper[1])
            f.write('\n')
            f.write(text)
            f.close()
        except:
            print('Failed to connect to ' + paper[1])
        print('{}/{}'.format(counter, len(engels_paper_list)))
        counter += 1


def get_mao() -> List[Tuple[str, str]]:
    html = urlopen('https://www.marxists.org/chinese/maozedong/index.htm')
    text: str = bytes.decode(html.read(), encoding='GBK')
    context: BeautifulSoup = BeautifulSoup(text, 'html.parser')
    result = []
    for pre in context.body.find_all('pre'):
        for paper in pre.find_all('a'):
            url: str = paper['href']
            ctx: str = paper.string
            # if ('PDF' in ctx) or ('CHM' in ctx):
            #     continue
            if url.startswith('#'):
                continue
            if url.endswith('pdf'):
                continue
            result.append((ctx, 'https://www.marxists.org/chinese/maozedong/' + url))
            # if 'PDF' in paper.string or 'CHM' in paper.string:
            #     continue
            # if paper['href'].startswith('#'):
            #     continue
            # result.append((paper.string, 'https://www.marxists.org/chinese/maozedong/' + paper['href']))
    return result


def write_mao():
    mao_paper_list = get_mao()
    counter = 1
    for paper in mao_paper_list:
        if paper is None or paper[0] is None or paper[1] is None:
            print('Invalid url pair, skipped')
            counter += 1
            continue

        try:
            html = urlopen(paper[1])
            context: BeautifulSoup = BeautifulSoup(bytes.decode(html.read(), encoding='GBK'), 'html.parser')
            text = context.get_text()

            f = open('毛泽东-{}.txt'.format(paper[0]), 'w')
            f.write(paper[0])
            f.write('\n')
            f.write('毛泽东')
            f.write('\n')
            f.write(paper[1])
            f.write('\n')
            f.write(text)
            f.close()
        except:
            print('Failed to handle ' + paper[0] + ', ' + paper[1])
        print('{}/{}'.format(counter, len(mao_paper_list)))
        counter += 1


def get_marx() -> List[Tuple[str, str]]:
    html = urlopen('https://www.marxists.org/chinese/marx/index.htm')
    text: str = bytes.decode(html.read(), encoding='GBK')
    context: BeautifulSoup = BeautifulSoup(text, 'html.parser')
    result = []
    for paper in context.body.pre.find_all('a'):
        if paper.string is not None and ('PDF' in paper.string or 'CHM' in paper.string):
            continue
        if paper['href'].endswith('pdf'):
            continue
        result.append((paper.string, 'https://www.marxists.org/chinese/marx/' + paper['href']))
    return result


def write_marx():
    marx_paper_list = get_marx()
    counter = 1
    for paper in marx_paper_list:
        if paper is None or paper[0] is None or paper[1] is None:
            print('Invalid url pair, skipped')
            counter += 1
            continue

        try:
            html = urlopen(paper[1])
            context: BeautifulSoup = BeautifulSoup(bytes.decode(html.read(), encoding='GBK'), 'html.parser')
            text = context.get_text()

            f = open('马克思-{}.txt'.format(paper[0]), 'w')
            f.write(paper[0])
            f.write('\n')
            f.write('马克思')
            f.write('\n')
            f.write(paper[1])
            f.write('\n')
            f.write(text)
            f.close()
        except:
            print('Failed to handle ' + paper[0] + ', ' + paper[1])
        print('{}/{}'.format(counter, len(marx_paper_list)))
        counter += 1


if __name__ == '__main__':
    write_marx()
    write_engels()
    write_mao()
