import math
import random
from typing import List, Dict, Any

# Import entropy base from config (will be set at runtime)
ENTROPY_BASE = 2

def compute_stability(state: Dict[str, Any], lambda_weights: List[float]) -> float:
    """
    Compute hierarchical stability S(psi).
    For demo, we simulate C_k and V_k from arbitrary features of the state.
    """
    # In a real implementation, C_k and V_k come from actual structure.
    # Here we generate synthetic values based on token count or embedding diversity.
    tokens = state.get("tokens", [])
    num_tokens = len(tokens)
    if num_tokens == 0:
        return 0.0

    # Simulate hierarchical levels: assume 5 levels
    levels = min(5, len(lambda_weights))
    S = 0.0
    for k in range(levels):
        # Simulate C_k as number of unique bigrams at that level
        # and V_k as total bigrams
        C_k = random.randint(1, max(1, num_tokens // (k+1)))
        V_k = max(C_k, random.randint(C_k, num_tokens * 2))
        if V_k > 0:
            term = lambda_weights[k] * math.log(1 + C_k / V_k)
            S += term
    return S

def compute_entropy(state: Dict[str, Any]) -> float:
    """
    Compute entropy E(psi) as diversity of possible continuations.
    For demo, simulate using distribution over next words.
    """
    # In real scenario, you'd get a probability distribution from LLM.
    # Here we simulate random probabilities over a few candidate continuations.
    probs = [random.random() for _ in range(5)]
    total = sum(probs)
    if total == 0:
        return 0.0
    probs = [p / total for p in probs]
    entropy = -sum(p * math.log(p) / math.log(ENTROPY_BASE) for p in probs if p > 0)
    return entropy

def compute_interest(stability: float, entropy: float) -> float:
    """Interest I = S * E"""
    return stability * entropy

def gra_filter(stability: float, s_crit: float) -> bool:
    """Return True if state is stable enough (S >= S_crit)"""
    return stability >= s_crit
