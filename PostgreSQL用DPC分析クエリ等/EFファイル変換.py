# -*- coding: utf-8 -*-

data = pd.read_csv('DRGEF.TXT',delimiter='\t',dtype={'退院年月日':pd.np.int64,'医師コード':str,'行為明細区分情報':str},
                   encoding = 'shift_jisx0213')
data['退院年月日'] = data['退院年月日'].replace(0,'infinity')
K = data['医師コード']
data['医師コード'] = [i.strip() for i in K]
data.to_csv('outputE.txt',index=False,sep='\t',encoding='utf-8')

