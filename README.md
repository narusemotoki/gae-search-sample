Google App EngineでPythonを使って検索API(Full Text Search, FTS)を使用するサンプルです。  

ライセンスはMITライセンスです。Google App Engineなど、サーバ側で利用する分にはライセンス表記の必要もありません。  
自由に使ってください。  

ここで実際に動作しているものを試すことができます。  
http://gae-search-sample.appspot.com/  

WikiPediaのPython, Java, Goの書き出し部分に対して検索を行い、検索ワードがヒットした言語名を返します。  
AppEngineの検索APIは、おそらく形態素解析を行なっています。  
そのため、「ヘビ」で検索してもPythonがヒットしません。「ニシキヘビ」ならヒットします。  

また、開発サーバでの実行結果と、AppEngineでの実行結果は異なります。  
AppEngineにデプロイしてからでないと、まともに検索できません。  
サンプルを作ってみた段階でのことなので、SDKの更新により改善されている可能性もあります。  
SDK 1.7.5

motoki@naru.se  
http://blog.naru.se