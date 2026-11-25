---
trigger: always_on
---

# GitHub 자동 동기화 규칙

이 프로젝트(`exchange_review`)에서 파일을 생성, 수정 또는 삭제한 경우, 어떤 채팅 세션에서 작업하더라도 **작업을 마무리하기 전 마지막 단계에서 반드시 변경사항을 GitHub(`origin main`)에 반영**해야 합니다.

1. `.qmd` 등 소스 파일을 수정했다면 필요한 경우 `quarto render`로 `docs/` 결과물을 최신화합니다.
2. `git status`로 변경사항을 확인한 뒤 `git add -A` 및 의미 있는 커밋 메시지로 `git commit`을 수행합니다.
3. `git push origin main`으로 원격 저장소에 푸시하여 GitHub에 최종 반영되도록 합니다.
