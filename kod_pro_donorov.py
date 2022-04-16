import pandas as pd
from matplotlib_venn import venn2

donor1=pd.read_excel('donor1.xlsx')
donor3=pd.read_excel('donor3.xlsx')

znach3=donor3[donor3.TPM>int(input())]
znach1=donor1[donor1.TPM>int(input())]

l1=znach1.gene_name.tolist()
l3=znach3.gene_name.tolist()

infadonor1=set (l1)
infadonor3=set(l3)

venn2(subsets=[infadonor1, infadonor3], set_labels=('donor1', 'donor3'))  
