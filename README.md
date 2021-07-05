# MHLW-discussions-corpus

厚生労働省のWebサイトで公開されている、同省が主催した審議会の議事録および記者会見のテキストを加工し、
機械学習の適した形にするスクリプトです。会議や会話、医療に関する言語資源として使えるかと思います。

形式は、以下のように、一つの議事録は`<doc>`タグから始まり、個々の発言は `<turn>` タグから始まります。
```
<doc>
<turn> 発言者1 発言内容...
<turn> 発言者2 発言内容...
```
発言内容は複数パラグラフにまたがることもあります。

なお、機械的に変換しているため、発言の区切りの認定に一部誤りがあったり、議事録本文ではないテキストが混入している場合もあります。

## テキストデータの配布について
以下のリンクからデータをダウンロード可能です。

https://github.com/hayato-hashimoto/MHLW-discussions-corpus/releases/download/v1.0/MHLW_discussions.zip

展開すると約 1GB の容量を消費します。

フォルダ構成:
<pre>
MHLW_discussions
 MHLW_discussions.txt # 審議会議事録など
 MHLW_interviews.txt # 大臣記者会見記録
</pre>
単語分割等はされていません。

本テキストデータは、[政府標準利用規約 2.0](https://www.mhlw.go.jp/seisakunitsuite/bunya/kenkou_iryou/iryou/hansen/sinseien/2016-pdf/t-20.pdf)および[著作権法30条の4](https://elaws.e-gov.go.jp/document?lawid=345AC0000000048#Mp-At_30_4)
に従い、機械学習・統計などの目的のために公開しております。法的適合性については利用者の責任でご判断ください。

このデータは、厚生労働省のWebサイトで公開されている、同省が主催した審議会の議事録および記者会見のテキストを、このサイトで公開しているスクリプト等により加工したデータです。
収集の対象となった文書のURLの一覧は[urllist.txt](https://raw.githubusercontent.com/hayato-hashimoto/MHLW-discussions-corpus/main/urllist.txt)に記載されています。

