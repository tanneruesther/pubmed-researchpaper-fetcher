
from typing import Callable, Any

def safe_entrez_call(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"❌ Entrez API call failed: {e}")
        return None
