import os, sys, json, requests
from dotenv import load_dotenv

load_dotenv()

def list_naver_categories(access_token: str) -> None:
    try:
        r = requests.get(
            "https://openapi.naver.com/blog/listCategory.json",
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=20,
        )
        print("[NAVER] status:", r.status_code)
        print("[NAVER] body:", r.text[:800])
    except Exception as e:
        print("[NAVER] request failed:", e)

def main():
    dry_run = (os.getenv("DRY_RUN", "false").lower() == "true")
    print("[RUN] DRY_RUN =", dry_run)

    notion_token = os.getenv("NOTION_TOKEN")
    notion_db    = os.getenv("NOTION_DATABASE_ID")
    naver_access = os.getenv("NAVER_ACCESS_TOKEN")

    # 가볍게 환경 확인
    print("[ENV] NOTION_TOKEN set:", bool(notion_token))
    print("[ENV] NOTION_DATABASE_ID set:", bool(notion_db))
    print("[ENV] NAVER_ACCESS_TOKEN set:", bool(naver_access))

    if dry_run:
        print("[DRY_RUN] Skipping publish.")
        return 0

    # 토큰이 있으면 네이버 카테고리 조회 한번만 호출 (연결 확인용)
    if naver_access:
        list_naver_categories(naver_access)
    else:
        print("[WARN] NAVER_ACCESS_TOKEN is empty. Skipping Naver API call.")

    print("[DONE] Minimal scaffold finished.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
