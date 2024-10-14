import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import datetime
import json
import time


# 忽略InsecureRequestWarning警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


productId='81144' 
storeIdArr='174'   
cookie='userToken=b3cda91cd32845a58de6e20fa65fd93f264782016; ec=XsiiHII1-1726621353332-bc0647e9b3da3-1928364744; _hudVID=88080055-5290-7b1d-cb0e-7df182f02bd1; _hudSID=1728697224555_1; CSRF-NWACT=bb203e2a-0e20-4ccd-9585-8c5494e9fc81; SK=b3cda91cd32845a58de6e20fa65fd93f264782016; _efmdata=IBlh2r4pgNGoYCvxaJyPcPK2RJ8hK2gtxe0biQ6b%2B7u%2BTWpxgiwmpqPKdevNXiCsuu6cl%2Foh5Wffpq43GYIZidGpoiz9a6tBkmwIo4WcWnY%3D; _exid=iR%2B%2Br3VfcLo%2FHugyyEtpOZshx%2BLPosvgyJbRlCh5wprvHWVdGKSRFrFni%2BcFWoNatEgxXATg2x00g%2B3mn8WeNQ%3D%3D; tgw_l7_route=6b255fa0ad00cf388078de4ca0395e2b; JSESSIONID=52A9A5959D237FCCE068F7AE24808FB8; hmallWebMember_autoLogin_sessionId=52A9A5959D237FCCE068F7AE24808FB8; ST=sso_591e0af3977ec4666ffa6a64269e7d38264782016; _hudSource=; sajssdk_2015_cross_new_user=1; _hudPVID=5; _hudSID_TS=1728697611826; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2223957661%22%2C%22first_id%22%3A%221927e681bc58ad-0aacca1c9112fe-6535111b-2073600-1927e681bc6935%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221927e681bc58ad-0aacca1c9112fe-6535111b-2073600-1927e681bc6935%22%7D; hud_refer=hmall.huazhu.com/lottery/lotteryDetailPage|5834,hmall.huazhu.com/carts/buyNow/191/81143/1/1|5822; Hm_lvt_9fbe3879c5974f2bbf5b97b2b10512ac=1726623519,1727318841,1728349842,1728697613; Hm_lpvt_9fbe3879c5974f2bbf5b97b2b10512ac=1728697613; HMACCOUNT=388B3C946ACE8440; Hm_cv_9fbe3879c5974f2bbf5b97b2b10512ac=1*memberId*264782016!1*memberName*%E5%88%98%E6%B6%9B!1*gender*%E7%94%B7'
def hzhcj():
    # 请求的URL
    url = "https://hmall.huazhu.com/order/createOrder"

    # 请求头
    headers = {
        'Host': 'hmall.huazhu.com',
        'Connection': 'keep-alive',
        'Content-Length': '718',  # 根据实际的数据长度进行调整
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                       'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11275'),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://hmall.huazhu.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://hmall.huazhu.com/carts/buyNow/25/81066/1/1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookie
        }

    # POST数据
    data = {
        "addressId": 1939343,
        "agreeRules": 1,
        "agreeServiceRules": 1,
        "cartFlag": False,
        "crmStoreId": 202,
        "fullyPointsFlag": 1,
        "fuluBizContent": None,
        "goodsType": "normal",
        "invoiceStoreId": 5,
        "isFullyPoints": 1,
        "isMissSendSms": 1,
        "lotteryFlag": True,
        "memberMobile": "17752413876",
        "memberPoint": 'null',
        "myaddressId": "MTkzOTM0Mw==",
        "num": 1,
        "orderInfoStores": [
            {
                "storeId": "5",
                "receiptType": "0",
                "receiptTitle": "",
                "receiptEmail": "",
                "taxPayerId": "",
                "remark": ""
            }
        ],
        "orderPoint": 1,
        "paymentType": 5,
        "pPrices": 1,
        "productId": productId,
        "receiptType": 0,
        "storeId": storeIdArr,
        "storeIdArr": storeIdArr
    }

    # 将数据转换为URL编码形式
    encoded_data = "&".join(f"{k}={v}" if not isinstance(v, list) else f"{k}={json.dumps(v)}" for k, v in data.items())

    # 发送POST请求并忽略SSL验证
    response = requests.post(url, headers=headers, data=encoded_data, verify=False)

    # 打印响应状态码和内容
    print(response.status_code)
    print(response.text)
    response_json = response.json()
    order_sn = response_json.get('data', {}).get('orderSn')
    print(f"Message: {order_sn}")




    timestamp = time.time()
    timestamp = int(timestamp)
    timestamp = str(timestamp)
    # 请求的URL
    url = f"https://hmall.huazhu.com/payment/miniappsToPay/{order_sn}?_={timestamp}"


    # 请求头
    headers = {
        'Host': 'hmall.huazhu.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                       'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11275'),
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://hmall.huazhu.com/carts/buyNow/25/81066/1/1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookie
        }

    # 发送GET请求
    response = requests.get(url, headers=headers, verify=False)

    # 检查响应状态码是否为200
    if response.status_code == 200:
        # 解析JSON响应
        try:
            response_json = response.json()
            
            # 输出响应内容
            print(json.dumps(response_json, indent=4, ensure_ascii=False))
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON response: {e}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        
if __name__ == "__main__":

    productId='81141' 
    storeIdArr='5'   
    cookie='userToken=b3cda91cd32845a58de6e20fa65fd93f264782016; ec=XsiiHII1-1726621353332-bc0647e9b3da3-1928364744; _hudVID=88080055-5290-7b1d-cb0e-7df182f02bd1; _hudSID=1728697224555_1; CSRF-NWACT=bb203e2a-0e20-4ccd-9585-8c5494e9fc81; SK=b3cda91cd32845a58de6e20fa65fd93f264782016; _efmdata=IBlh2r4pgNGoYCvxaJyPcPK2RJ8hK2gtxe0biQ6b%2B7u%2BTWpxgiwmpqPKdevNXiCsuu6cl%2Foh5Wffpq43GYIZidGpoiz9a6tBkmwIo4WcWnY%3D; _exid=iR%2B%2Br3VfcLo%2FHugyyEtpOZshx%2BLPosvgyJbRlCh5wprvHWVdGKSRFrFni%2BcFWoNatEgxXATg2x00g%2B3mn8WeNQ%3D%3D; tgw_l7_route=6b255fa0ad00cf388078de4ca0395e2b; JSESSIONID=52A9A5959D237FCCE068F7AE24808FB8; hmallWebMember_autoLogin_sessionId=52A9A5959D237FCCE068F7AE24808FB8; ST=sso_591e0af3977ec4666ffa6a64269e7d38264782016; _hudSource=; sajssdk_2015_cross_new_user=1; _hudPVID=5; _hudSID_TS=1728697611826; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2223957661%22%2C%22first_id%22%3A%221927e681bc58ad-0aacca1c9112fe-6535111b-2073600-1927e681bc6935%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221927e681bc58ad-0aacca1c9112fe-6535111b-2073600-1927e681bc6935%22%7D; hud_refer=hmall.huazhu.com/lottery/lotteryDetailPage|5834,hmall.huazhu.com/carts/buyNow/191/81143/1/1|5822; Hm_lvt_9fbe3879c5974f2bbf5b97b2b10512ac=1726623519,1727318841,1728349842,1728697613; Hm_lpvt_9fbe3879c5974f2bbf5b97b2b10512ac=1728697613; HMACCOUNT=388B3C946ACE8440; Hm_cv_9fbe3879c5974f2bbf5b97b2b10512ac=1*memberId*264782016!1*memberName*%E5%88%98%E6%B6%9B!1*gender*%E7%94%B7'

    for i in range(9):
        hzhcj()
        time.sleep(5)