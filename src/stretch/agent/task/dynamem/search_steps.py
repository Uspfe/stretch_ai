GLOBAL_SEARCH_STEPS: int = 10

def set_global_search_steps(steps: int):
    global GLOBAL_SEARCH_STEPS
    GLOBAL_SEARCH_STEPS = steps

def get_global_search_steps() -> int:
    global GLOBAL_SEARCH_STEPS
    return GLOBAL_SEARCH_STEPS