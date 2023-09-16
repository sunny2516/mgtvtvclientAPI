#script written by nilaoda
import re
import requests

headers = {
    'User-Agent': 'ImgoMediaPlayerLib/com.starcor.mango.V6.2.401.383.3.DBEI_TVAPP.0.0_Release (Linux;Android 7.1.2(25)) system/0/5.5.6_2.23032101.20230322'
}

def get_title(vid: str) -> str:
    api = f'http://ott.bz.mgtv.com/ott/v1/video/attach?version=5.6.016.200.2.DBEI.0.0_Release&type=0&_support=00100000011&return=all&partId={vid}&tdsourcetag=s_pctim_aiomsg'
    resp = requests.get(api, headers=headers).json()
    return resp['data'][0]['partName']

if __name__ == '__main__':
    url = "" #insert url
    pattern = r"\d+"
    vid = re.findall(pattern, url)[-1]
    title = get_title(vid)
    #print(title)
    ticket = ''#insert ticket
    #quality=10 4K50P quality=9 4K25P quality=4 1080P  origianal=hevc videoencode
    api = f'https://ottlive.api.mgtv.com/v1/epg5/getVodPlayUrl_v2?mod=SM-G973N&quality=10&is_outer=0&uuid=34a03fc3a4c8402c96663572813d7207&ticket={ticket}&svrip=175.6.15.49%2Cpcvideotestws.titan.mgtv.com%2Cpcvideomiguott.titan.mgtv.com&rom_version=&buss_id=1000014&pl_id=-1&net_id=&version=6.2.401.383.3.DBEI_TVAPP.0.0_Release&exdef=&android_sdk_ver=25&hp_id=&_support=10110101011010101010&app_type=1&force_avc=0&try_type=0&clip_id=533278&mf=samsung&abt=181|B%3B179|B%3B167|B%3B155|B%3B150|C%3B146|B%3B99|H&pre=0&tdt=1&f_hot=0&license=ZgOOgo5MjkyOTDu0BUsNtKp8IEu0O7%2B%2FdgYFBYcFfHYGdrQODQWqv0t8BgUGDg2%2FBbRLjkyOTI5MZgOOgg%3D%3D&pver=1.1.501.R|1.1.501.R|1.1.501.R|1.1.201.R|0|0&platform=3&os_ver=7.1.2&business_id=3100001&device_id=c4729438624cffe077578e0e41973f2807019f74&auth_mode=1&time_zone=GMT%2B08%3A00&dcp_id=0&channel_code=DBEI&part_id={vid}&model_code=SM-G973N&mac_id=34-8C-D5-92-DC-92&'
    resp = requests.get(api, headers=headers).json()
    print(f"{resp['data']['videoFormat']} => {resp['data']['videoWidth']}x{resp['data']['videoHeight']} => {resp['data']['filebitrate']}Kbps => {resp['data']['framerate']}")
    m3u8 = resp['data']['url']
    #print(m3u8)
    cmd_headers = ' '.join(['-H "{}: {}"'.format(key, value) for key, value in headers.items()])

    print(f'N_m3u8DL-RE --binary-merge --save-name "{title}" {cmd_headers} "{m3u8}"')