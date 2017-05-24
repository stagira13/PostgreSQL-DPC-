# -*- coding: utf-8 -*-

import pandas as pd

e_names = ['施設コード','データ識別番号','退院年月日','入院年月日','データ区分','順序番号',
'病院点数マスタコード','レセプト電算コード','解釈番号','診療明細名称','行為点数','行為薬剤料',
'行為材料料','円点区分','行為回数','保険者番号','レセプト種別コード','実施年月日',
'レセプト科区分	','診療科区分','医師コード','病棟コード','病棟区分','入外区分','施設タイプ']
#正しくはEファイルには「診療明細名称」ではなく「診療行為名称」だが、統合のため変えている

f_names = ['施設コード','データ識別番号','退院年月日','入院年月日','データ区分',
'順序番号','行為明細番号','病院点数マスタコード','レセプト電算コード','解釈番号','診療明細名称',
'使用量','基準単位','行為明細点数','行為明細薬剤料','行為明細材料料','円点区分',
'出来高実績点数','行為明細区分情報']

edata = pd.read_csv('DRGE.TXT',delimiter='\t',parse_dates=['入院年月日','実施年月日'],dtype={'医師コード':str},
	encoding = 'shift_jisx0213',names=e_names)

fdata = pd.read_csv('DRGF.TXT',delimiter='\t',parse_dates=['入院年月日'],dtype={'行為明細区分情報':str},
	encoding = 'shift_jisx0213',names=f_names)

fdata['明細点数・金額'] = fdata['行為明細点数'] + fdata['行為明細薬剤料'] + fdata['行為明細材料料']
fdata.drop(['行為明細点数','行為明細薬剤料','行為明細材料料'],axis=1,inplace = True)

efdata = pd.concat([edata,fdata])

#Sortは好意明細番号も含める（０～５の順に並べないとgroupbyfillnaが機能しない）
#ここで一度fillna(0)すべきであろう。inplace=trueを忘れずに

efdata['行為明細番号'].fillna(0,inplace=True)

efdata.sort_values(['データ識別番号','入院年月日','データ区分','順序番号','行為明細番号'],inplace = True)
efdata.reset_index(inplace=True)
#ここからgroupby fillnaで処理を行えばよい

fill_list='行為回数','実施年月日','診療科区分','医師コード','病棟コード','病棟区分'

for val in fill_list:
    efdata[val].fillna(method='pad',inplace=True)

sort_list = '施設コード','データ識別番号','退院年月日','入院年月日','データ区分',\
'順序番号','行為明細番号','病院点数マスタコード','レセプト電算コード','解釈番号','診療明細名称',\
'使用量','基準単位','明細点数・金額','円点区分','出来高実績点数','行為明細区分情報','行為点数','行為薬剤料',\
'行為材料料','行為回数','保険者番号','レセプト種別コード','実施年月日','レセプト科区分',\
'診療科区分','医師コード','病棟コード','病棟区分','入外区分','施設タイプ'


efdata_sorted = efdata.reindex(columns=sort_list)

efdata_sorted['退院年月日'] = efdata_sorted['退院年月日'].replace(0,'infinity')
efdata_sorted['入院年月日'] = efdata_sorted['入院年月日'].replace('0','epoch')

#上のはバッドノウハウ。入院年月日は数値ではなく文字列になってしまっているので、（恐らくパースに失敗したから）
#やむなくこうしている。うーん…
#変なデータが混じってなければ、入院年月日はいじらなくてもいいです。

K = efdata_sorted['医師コード']
efdata_sorted['医師コード'] = [i.strip() for i in K]

Fillzero = ['行為点数','行為薬剤料','行為材料料','使用量','基準単位','明細点数・金額','出来高実績点数']
for fillzero in Fillzero:
	efdata_sorted[fillzero].fillna(0,inplace=True)


efdata_sorted.to_csv('outputEF.txt',index=False,sep='\t',encoding='utf-8')
