today=`date "+%y%m%d"`
nextday=`date "+%y%m%d" -d "30 days"`

#getNOTAM2 id password code

if [ $# -ne 3 ]; then
    echo "getNOTAM2.sh AIS_ID AIS_PASS RJ**"
    exit 1
fi

curl -k -c cookie.txt -d "formName=ais-web" -d "userID=${1}" -d "password=${2}" "https://aisjapan.mlit.go.jp/LoginAction.do"


curl -b cookie.txt --globoff -k "https://aisjapan.mlit.go.jp/KeySearcherAction.do" -d "location=${3}" -d "period=0" -d "periodFrom=${today}0000" -d "periodTo=${nextday}0000" -d "dispScopeA=true" -d "dispScopeE=true" -d "dispScopeW=true">htmldata/${3}.html
