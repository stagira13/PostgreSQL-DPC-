$z = Import-Csv DRGD.txt -Delimiter "`t" -Encoding Default -Header '�{�ݔԍ�'`
,'�f�[�^���ʔԍ�','�މ@�N����','���@�N����'`
,'�f�[�^�敪','�����ԍ�','�_���}�X�^�R�[�h'`
,'���Z�d�Z�����R�[�h','���ߔԍ�','�f�Ís�ז���','�s�ד_��','�s�ז�ܗ�'`
,'�s�׍ޗ���','�~�_�敪','�s�׉�','�ی��Ҕԍ�','���Z�v�g��ʃR�[�h'`
,'���{�N����','���Z�v�g�ȋ敪','�f�Éȋ敪'`
,'��t�R�[�h','�a���R�[�h','�a���敪','���O�敪'`
,'�{�݃^�C�v','�Z��J�n��','�Z��I����','�Z��N�Z��'`
,'���ޔԍ�','��Ë@�֌W��'

$z | foreach {
$_.�މ@�N���� = $_.�މ@�N����.replace("00000000","infinity")
}
$z | Export-Csv outputD.txt -notype -Encoding UTF8 -Delimiter "`t"