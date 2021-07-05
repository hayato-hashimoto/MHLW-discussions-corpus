# get minister interviews
wget https://www.mhlw.go.jp/stf/kaiken/daijin/oldindex.html
wget -w 4 -i urllist_kaiken.txt -P kaiken_html # 112MB in 2.2 hours

# get discussions
wget https://www.mhlw.go.jp/stf/shingi/indexshingi.html
python get_url.py indexshingi.html > urllist_shingi.txt
grep indexshingiother_ urllist_shingi.txt | sed -e 's#^#https://www.mhlw.go.jp#' > urllist_shingi_index.txt
grep -v  indexshingiother_ urllist_shingi.txt | grep -v 'https:' | grep -v '#' | sed -e 's#^#https://www.mhlw.go.jp#' > _urllist_shingi.txt
mv _urllist_shingi.txt urllist_shingi.txt
wget -w 4 -i urllist_shingi.txt -P shingi_tables
wget -w 4 -i urllist_shingi_index.txt -P shingi_indexes
echo > urllist_other_shingi.txt

for x in shingi_indexes/*
do
python get_url.py $x >> urllist_other_shingi.txt
done

# get URLs for the table of discussions
grep -v 'http' urllist_other_shingi.txt | sed -e 's#^#https://www.mhlw.go.jp#' > _urllist_shingi.txt
mv _urllist_shingi.txt urllist_other_shingi.txt
wget -w 4 -i urllist_other_shingi.txt -P shingi_tables
echo > urllist_text.txt

for x in shingi_tables/*
do
python get_text_url.py $x >> urllist_text.txt
done

# get URLs for the discussion text
grep -v 'http' urllist_text.txt | sed -e 's#^#https://www.mhlw.go.jp#' > _urllist.txt
grep 'http' urllist_text.txt >> _urllist.txt
sort _urllist.txt | uniq  > urllist.txt

wget -w 2 -i urllist.txt -P download

mkdir download/txt
mv download/*.txt > txt
mv download/*.TXT > txt

# convert htmls
mkdir download/html
mv download/*.html > html
mkdir download/html-txt
ls download/html/* | xargs -n 1 -P 64 python get_text_from_html.py

# remove short files
ls download/html-txt/* -lh | grep -v K | sed -e 's/^.* //' | xargs rm
