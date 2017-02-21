# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv('DRGD.TXT',delimiter='\t',names = ('施設番号'
    ,'データ識別番号'
	,'退院年月日'
	,'入院年月日'
	,'データ区分'
	,'順序番号'
	,'点数マスタコード'
	,'レセ電算処理コード'
	,'解釈番号'
	,'診療行為名称'
	,'行為点数'
	,'行為薬剤料'
	,'行為材料料'
	,'円点区分'
	,'行為回数'
	,'保険者番号'
	,'レセプト種別コード'
	,'実施年月日'
	,'レセプト科区分'
	,'診療科区分'
	,'医師コード'
	,'病棟コード'
	,'病棟区分'
	,'入外区分'
	,'施設タイプ'
	,'算定開始日'
	,'算定終了日'	
	,'算定起算日'	
	,'分類番号'
	,'医療機関係数'),header = None,dtype={'医師コード':str},encoding = 'shift_jisx0213')
data['退院年月日'] = data['退院年月日'].replace(0,'infinity')
data['入院年月日'] = data['入院年月日'].replace(0,'epoch')
K = data['医師コード']
data['医師コード'] = [i.strip() for i in K]
data.to_csv('outputD.txt',index=False,sep='\t',encoding='utf-8')
