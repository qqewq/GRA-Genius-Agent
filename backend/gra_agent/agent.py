from typing import List, Dict, Any, Optional
import random
from .gra_core import compute_stability, compute_entropy, compute_interest, gra_filter
from config import S_CRIT, LAMBDA_WEIGHTS, CANDIDATE_POOL_SIZE, USE_DUMMY_CANDIDATES

class GeniusAgent:
    def __init__(self):
        self.s_crit = S_CRIT
        self.lambda_weights = LAMBDA_WEIGHTS
        self.candidate_pool_size = CANDIDATE_POOL_SIZE
        self.history = []  # store past states for context

    def generate_candidates(self, user_input: str) -> List[Dict[str, Any]]:
        """
        Generate a pool of candidate responses (states).
        For demo, use dummy templates; replace with LLM call in production.
        """
        candidates = []
        if USE_DUMMY_CANDIDATES:
            templates = [
                "That's an interesting point. Let me think...",
                "I believe the answer is quite complex.",
                "Could you clarify what you mean?",
                "From my perspective, the key factor is stability.",
                "Let's explore this from different angles.",
                "I see a pattern here.",
                "This reminds me of GRA-Obnulenka's principle."
            ]
            # Generate multiple candidates by sampling templates
            for _ in range(self.candidate_pool_size):
                text = random.choice(templates) + f" (variant {_})"
                state = {
                    "tokens": text.split(),
                    "text": text,
                    "user_input": user_input,
                    "candidate_id": _
                }
                candidates.append(state)
        else:
            # Placeholder for LLM integration
            # Call HuggingFace pipeline or API to generate responses
            pass
        return candidates

    def select_best_response(self, candidates: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        For each candidate, compute S and E, filter, then pick max I.
        """
        best_state = None
        best_interest = -float('inf')
        fallback_state = None
        fallback_stability = -float('inf')

        for state in candidates:
            # Compute S and E (with some synthetic features)
            # In real, you'd extract hierarchical structure from state
            # For demo, we add some randomness to simulate variation
            # but we also incorporate text length as a crude feature.
            tokens = state.get("tokens", [])
            # Add synthetic C_k, V_k based on token count
            # We'll let compute_stability generate synthetic values.
            S = compute_stability(state, self.lambda_weights)
            E = compute_entropy(state)
            state['S'] = S
            state['E'] = E
            state['I'] = compute_interest(S, E)

            if gra_filter(S, self.s_crit):
                if state['I'] > best_interest:
                    best_interest = state['I']
                    best_state = state
            else:
                # Keep track of best fallback (highest S) in case none pass filter
                if S > fallback_stability:
                    fallback_stability = S
                    fallback_state = state

        # If no candidate passed, return the one with highest S
        if best_state is None:
            best_state = fallback_state

        return best_state

    def chat(self, user_input: str) -> str:
        """Main entry point: generate candidates, select best, return text."""
        candidates = self.generate_candidates(user_input)
        selected = self.select_best_response(candidates)
        if selected:
            response_text = selected.get("text", "No response generated.")
            # store in history
            self.history.append({"user": user_input, "agent": response_text})
            return response_text
        else:
            return "I'm sorry, I couldn't find a suitable response."

    def get_history(self):
        return self.history
