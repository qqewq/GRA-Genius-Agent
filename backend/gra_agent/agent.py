import random
from typing import List, Dict, Any
from .gra_core import compute_stability, compute_entropy, compute_interest, gra_filter
from config import S_CRIT, LAMBDA_WEIGHTS, MAX_CANDIDATES

class GeniusAgent:
    def __init__(self, model=None):
        self.model = model  # опционально LLM
        self.history = []
        self.S_crit = S_CRIT

    def generate_candidates(self, input_text: str) -> List[Dict[str, Any]]:
        """
        Генерирует несколько кандидатов-ответов.
        В демо-версии используем шаблоны или случайные фразы.
        В реальности — вызов LLM с разными параметрами (temperature, top_p).
        """
        # Заглушка: 5 шаблонных ответов
        templates = [
            "Это интересный вопрос. Возможно, ответ кроется в ...",
            "Я думаю, что здесь важна иерархия ...",
            "С точки зрения GRA, стабильность требует ...",
            "Хаос и порядок должны слиться в гармонии.",
            "Позвольте предложить нестандартный взгляд: ..."
        ]
        candidates = []
        for i in range(min(MAX_CANDIDATES, len(templates))):
            text = templates[i] + " " + input_text[:20]
            # Имитация иерархических связей (для S)
            C = random.randint(1, 10)
            V = random.randint(C, C+5)
            hierarchy = {0: (C, V), 1: (C//2, V//2+1)}
            entropy = random.uniform(0.3, 0.9)
            state = {
                'text': text,
                'hierarchy': hierarchy,
                'entropy': entropy,
                'raw_score': 0.0
            }
            state['S'] = compute_stability(state, LAMBDA_WEIGHTS)
            state['E'] = compute_entropy(state)
            state['I'] = compute_interest(state['S'], state['E'])
            candidates.append(state)
        return candidates

    def select_best(self, candidates: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Применяет GRA-фильтр и выбирает кандидата с максимальным I."""
        filtered = [c for c in candidates if c['S'] >= self.S_crit]
        if not filtered:
            # Если ни один не прошёл, выбираем с максимальной S (или возвращаем дефолтный)
            return max(candidates, key=lambda c: c['S'])
        return max(filtered, key=lambda c: c['I'])

    def respond(self, input_text: str) -> str:
        """Основной метод генерации ответа."""
        candidates = self.generate_candidates(input_text)
        best = self.select_best(candidates)
        # Сохраняем в историю
        self.history.append({'input': input_text, 'response': best['text'], 'I': best['I']})
        return best['text']
