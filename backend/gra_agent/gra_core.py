import numpy as np
from typing import List, Dict, Any

def compute_stability(state: Dict[str, Any], lambda_weights: List[float]) -> float:
    """
    Вычисляет иерархическую стабильность S(psi).
    state — словарь, содержащий уровни связности: {level: (C_k, V_k)}
    """
    S = 0.0
    for k, (C, V) in enumerate(state.get('hierarchy', {}).items()):
        if V > 0:
            S += lambda_weights[min(k, len(lambda_weights)-1)] * np.log(1 + C / V)
    return S

def compute_entropy(state: Dict[str, Any]) -> float:
    """
    Вычисляет энтропию E(psi) как разнообразие возможных продолжений.
    В простейшем случае — энтропия распределения вероятностей следующих токенов.
    Здесь заглушка: возвращает значение из state или случайное.
    """
    # В реальности это может быть энтропия распределения из LLM
    return state.get('entropy', 0.5)

def compute_interest(S: float, E: float) -> float:
    """Интерес I = S * E"""
    return S * E

def gra_filter(state: Dict[str, Any], S_crit: float) -> bool:
    """Проверяет, проходит ли состояние GRA-фильтр (S >= S_crit)"""
    S = compute_stability(state, [1.0]*5)  # временно
    return S >= S_crit
