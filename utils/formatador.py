def formartarTelefone(telefone: str) -> str:
    tamanho = len(telefone)

    if tamanho == 10:
        return f"({telefone[:2]}){telefone[2:6]}-{telefone[6:]}"
    elif tamanho == 11:
        return f"({telefone[:2]}){telefone[2:7]}-{telefone[7:]}"
    else:
        raise ValueError("Telefone inválido")
