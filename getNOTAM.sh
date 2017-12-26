today=`date "+%y%m%d"`
nextday=`date "+%y%m%d" -d "30 days"`



curl -b cookie.txt --globoff -k "https://aisjapan.mlit.go.jp/KeySearcherAction.do" -d "location=${1}" -d "period=0" -d "periodFrom=${today}0000" -d "periodTo=${nextday}0000" -d "dispScopeA=true" -d "dispScopeE=true" -d "dispScopeW=true">htmldata/${3}.html
