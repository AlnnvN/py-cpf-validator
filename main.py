#https://www.macoratti.net/alg_cpf.htm




def format_cpf(CPF):
    return CPF.replace('.','').replace('-','')[0:9]

def product_sum(cpf_digitless):
    product = 0 
    for i, number in enumerate(cpf_digitless):
        product+=int(number)*(len(cpf_digitless)+1-i)
    return int(product)

def calc_digit(cpf_digitless):
    product = product_sum(cpf_digitless)
    if product%11 < 2:
        return 0
    else:
        return 11-product%11

def add_two_digits(cpf_digitless):
    for i in range(2):
        cpf_digitless+=str(calc_digit(cpf_digitless))
    return cpf_digitless

def validate_cpf():
    CPF = input("Enter the CPF to be checked (optional dots ands the hyphen): ")
    if len(CPF) != 11 and len(CPF) != 14:
        raise ValueError

    cpf_digitless = format_cpf(CPF)

    final_cpf = add_two_digits(cpf_digitless)
    final_cpf = f'{final_cpf[0:3]}.{final_cpf[3:6]}.{final_cpf[6:9]}-{final_cpf[9:11]}'

    if final_cpf.replace('.','').replace('-','') == CPF:
        print(f"The entered CPF is valid! (matches the calculated one - {final_cpf})")
    else:
        print(f"The entered CPF is invalid. (it does not match the calculated one - {final_cpf})")

try:
    validate_cpf()
except ValueError:
    print("\n\nEnter a format-valid CPF - XXX.XXX.XXX-XX (11 numbers)\n")
    validate_cpf()