import os
import sys

import uvicorn

from app.config import settings


def main():
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level=settings.log.level,
    )


if __name__ == "__main__":
    print(f"cwd:{os.getcwd()}")
    print(f"package:{__package__}")
    for i, path in enumerate(sys.path):
        print(f"{i}: {path}")
    main()
