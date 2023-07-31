
#AppID:34686237
#API Key:l7P4YUZ2GRO8LPiwK2SM7aOn
#Secret Key:klcTBfcwXbSmFeGLmohU7E70WRdWcKR5

import requests
import json
from pprint import pprint


def main():

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=l7P4YUZ2GRO8LPiwK2SM7aOn&client_secret=klcTBfcwXbSmFeGLmohU7E70WRdWcKR5"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    pprint(response.json())

if __name__ == '__main__':
    main()
"""
{'access_token': '24.0a3c03ad35b54f779a6fdfbb8a6b47af.2592000.1689251436.282335-34686237',
 'expires_in': 2592000,
 'refresh_token': '25.150c0fa44aa82d90d248a25eae2bf12d.315360000.2002019436.282335-34686237',
 'scope': 'public nlp_simnet nlp_wordemb nlp_comtag nlp_dnnlm_cn '
          'brain_nlp_lexer brain_all_scope brain_nlp_comment_tag '
          'brain_nlp_dnnlm_cn brain_nlp_word_emb_vec brain_nlp_word_emb_sim '
          'brain_nlp_sentiment_classify brain_nlp_simnet brain_nlp_depparser '
          'brain_nlp_wordembedding brain_nlp_dnnlm_cn_legacy '
          'brain_nlp_simnet_legacy brain_nlp_comment_tag_legacy '
          'brain_nlp_keyword brain_nlp_topic brain_nlp_ecnet brain_nlp_emotion '
          'brain_nlp_news_summary brain_creation_couplets brain_creation_poem '
          'brain_nlp_address brain_nlp_titlepredictor brain_nlp_bless_creation '
          'brain_nlp_brain_entity_analysis '
          'brain_v1_nlp_txt_keywords_extraction brain_v1_nlp_txt_monet '
          'brain_nlp_txt_word_embellish wise_adapt lebo_resource_base '
          'lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian '
          'ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope '
          'ApsMis_fangdi_permission smartapp_snsapi_base '
          'smartapp_mapp_dev_manage iop_autocar oauth_tp_app '
          'smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify '
          'smartapp_opensource_openapi smartapp_opensource_recapi '
          'fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理 '
          'smartapp_component smartapp_search_plugin avatar_video_test '
          'b2b_tp_openapi b2b_tp_openapi_online smartapp_gov_aladin_to_xcx',
 'session_key': '9mzdC3nF2WCLdXKujtUeqxn6vMLlxaOylpvYW0XARWhGzxW2UU4BhCMbv4MHBKd9sXUkTIMPghN/xXFlvjRCKoVkIC0gwQ==',
 'session_secret': '20ccf4f4a32fd9deda0c419939724d22'}
"""