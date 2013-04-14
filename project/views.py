# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from google.appengine.api import search

_INDEX_NAME = 'programming_language'
_PYTHON_TEXT = u"""Python（パイソン）は、オランダ人のグイド・ヴァンロッサムが作ったオープンソースのプログラミング言語。オブジェクト指向スクリプト言語の一種であり、Perlとともに欧米で広く普及している。イギリスのテレビ局 BBC が製作したコメディ番組『空飛ぶモンティ・パイソン』にちなんで名付けられた。Pythonは英語で爬虫類のニシキヘビの意味で、Python言語のマスコットやアイコンとして使われることがある。"""
_JAVA_TEXT = u"""Java（ジャバ）は、狭義ではオブジェクト指向プログラミング言語Javaであり、広義ではプログラミング言語Javaのプログラムの実行環境および開発環境をいう。本稿ではプログラミング言語としての Java、および関連する技術や設計思想、およびJava言語の実行環境として見たJavaプラットフォームについて解説する。クラスライブラリなどを含めた、Javaバイトコードの実行環境と開発環境（広義のJava）については、Javaプラットフォームを参照。また、言語の文法に関してはJavaの文法を参照。"""
_GO_TEXT = u"""Goはプログラミング言語のひとつ。Google社によって開発されており、設計にロブ・パイク、ケン・トンプソンらが関わっている。
主な特徴として、軽量スレッディングのための機能、Pythonのような動的型付け言語のようなプログラミングの容易性、などがある。Go処理系としてはコンパイラのみが開発されている。
発表当初はLinuxとMac OS Xのみしかサポートしていなかったが、2012年3月にリリースされたversion 1からはWindowsもサポートされている。また、2011年5月10日に公開された Google App Engine 1.5.0 でも、Go言語がサポートされている。"""

def index(request):
    result = []
    if 'POST' == request.method:
        query_string = request.POST['query']
        if 0 == len(query_string):
            result.append(u'検索ワードが空です')
        else:
            options = search.QueryOptions(returned_fields=['title'])
            query = search.Query(query_string=query_string, options=options)
            for document in search.Index(name=_INDEX_NAME).search(query):
                result.append(document.field('title').value)


        if 0 == len(result):
            result.append(u'該当なし')
    else:
        result.append(u'ここに検索結果が表示されます')

    return render(request, 'index.html', {'python_text': _PYTHON_TEXT,
                                          'java_text': _JAVA_TEXT,
                                          'go_text': _GO_TEXT,
                                          'result': result})

def init(request):
    index = search.Index(name=_INDEX_NAME)

    while True:
        document_ids = [document.doc_id
                        for document in index.get_range(ids_only=True)]
        if not document_ids:
            break
        index.delete(document_ids)

    python_document = search.Document(
        fields=[search.TextField(name='title', value='Python'),
               search.TextField(name='text', value=_PYTHON_TEXT)]
    )
    index.put(python_document)

    java_document = search.Document(
        fields=[search.TextField(name='title', value='Java'),
               search.TextField(name='text', value=_JAVA_TEXT)]
    )
    index.put(java_document)

    go_document = search.Document(
        fields=[search.TextField(name='title', value='Go'),
               search.TextField(name='text', value=_GO_TEXT)]
    )
    index.put(go_document)

    return redirect('/')
