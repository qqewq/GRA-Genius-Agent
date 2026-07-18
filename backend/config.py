# Stability threshold: states with S < S_CRIT are discarded
S_CRIT = 0.5

# Hierarchical level weights (sum to 1)
LAMBDA_WEIGHTS = [0.3, 0.3, 0.2, 0.1, 0.1]  # for levels 1..5

# For entropy calculation (if using probability distribution)
ENTROPY_BASE = 2  # bits

# Candidate generation settings (dummy or real LLM)
CANDIDATE_POOL_SIZE = 5
USE_DUMMY_CANDIDATES = True  # if True, use template-based responses; else call LLM
# LLM_MODEL_NAME = "gpt2"  # or "microsoft/DialoGPT-medium"
