data_dd_mm_aaaa=input("Digite a data no formato dd/mm/aaaa: ")
dia=data_dd_mm_aaaa[:2]
mes=data_dd_mm_aaaa[2:4]
ano=data_dd_mm_aaaa[4:]
data_aaaa_mm_dd=ano+'/'+mes+'/'+dia
print(f"Data no formato AAAA/MM/DD: {data_aaaa_mm_dd}")