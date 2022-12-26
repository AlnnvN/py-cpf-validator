

CPF = input("Enter the CPF to be checked (with dots ands the hyphen): ")

def format_cpf(CPF):
    return CPF.replace('.','').replace('-','')

cpf_digitless = format_cpf(CPF)

print(cpf_digitless)