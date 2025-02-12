#Copyright Bail&Will&loaf0808 2025
#SkyNet:libwordclass 单词类模块

LOGLEVEL = 0

Word = Lesson = None   #先定义一下，防止循环依赖时报错AttributeError
                            #这个问题在d48ccdb2d22ddd2672e17d05bb1bf7d659c6c5e4已经出现，暂无更好解决方案

import logging,libunf

class Word:
    '''单词类'''
    def __init__(self,word:str,trans:str):
        self.word = word
        self.trans = trans
    def __str__(self)->str:
        return self.word
    def __eq__(self,b:Word):
        return self.word == b.word
    def to_unf(self)->libunf.UnfamiliarWord:
        '''转为生词'''
        obj = libunf.UnfamiliarWord(self.word,self.trans)
        obj.right = 0
        return obj
class Lesson:
    '''课程类'''
    def __init__(self,words:dict[str:Word],md5:str,progress:list,**info):
        '''课程类初始化
info:课程信息。包括:
- name(str):课程简称（用于显示）
- fullname(str):课程全称
- author(str):课程作者/编写者（推荐附上邮箱，如：Bail <2915289604@qq.com>）
- file_version(int):文件版本
words(tuple):课程中包括的单词。元组中的对象类型为Word
md5(str):课程文件的md5值，作为ID
progress(list):学习进度。长度为3，类型为int，依次为记忆、听写、默写的学习进度'''
        self.name = info['name']
        self.fullname = info['fullname']
        self.author = info['author']
        self.file_version = info['file_version']
        self.words = words
        self.md5 = md5
        self.progress = progress
##    def __iter__(self):
##        return self.words
    def get_word(self,word:str)->Word:
        '''根据单词字符串获取单词对象'''
        if word not in self.words:
            raise WordNotFoundError(self,word)
        return self.words[word]

class WrongFileVersion(Exception):
    '''课程文件版本错误'''
    def __init__(self,e):
        self.e = e
    def __str__(self) -> str:
        return self.e
class WordNotFoundError(KeyError):
    '''未从课程中找到单词'''
    def __init__(self, lesson:Lesson, word:str):
        super().__init__()
        self.lesson = lesson
        self.errorWord = word
    def __str__(self):
        return f'未从课程“{self.lesson.name}”中找到单词“{self.errorWord}”'

class Logger(logging.Logger):
    def __init__(self):
        super().__init__(__name__,LOGLEVEL)
