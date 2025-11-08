import statistics as st
import numpy as np

empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

empresas = {
    "Empresa 1": empresa1,
    "Empresa 2": empresa2,
    "Empresa 3": empresa3,
    "Empresa 4": empresa4
}

for nome, dados in empresas.items():
    media = st.mean(dados)
    mediana = st.median(dados)
    try:
        moda = st.mode(dados)
    except:
        moda = "Sem moda (valores únicos)"
    desvio = np.std(dados)
    
    print(f"\n{nome}")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda}")
    print(f"Desvio padrão: {desvio:.2f}")