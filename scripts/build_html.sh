#!/bin/bash
# scripts/build_html.sh — Quarto 웹사이트 빌드 및 GitHub Pages 배포 준비
set -e

command -v quarto >/dev/null 2>&1 || {
    echo "❌ Quarto CLI가 설치되어 있지 않습니다."
    echo "   설치: brew install --cask quarto  또는  https://quarto.org/docs/get-started/"
    exit 1
}
echo "✓ Quarto $(quarto --version)"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

echo ""
echo "▶ Step 1: MD → QMD 변환 중... (출력: qmd/)"
python3 scripts/convert_md_to_qmd.py

echo ""
echo "▶ Step 2: _quarto.yml 생성 중..."
python3 scripts/generate_quarto_yml.py

echo ""
echo "▶ Step 3: HTML 빌드 중 (quarto render → docs/)..."
quarto render

touch docs/.nojekyll

HTML_COUNT=$(find docs -name "*.html" | wc -l | tr -d ' ')
echo ""
echo "=================================================="
echo "✅ 빌드 완료!"
echo "   QMD 소스:  qmd/"
echo "   HTML 출력: docs/  (${HTML_COUNT}개 파일)"
echo ""
echo "📌 로컬 미리보기:  quarto preview"
echo "📌 GitHub Pages:   git add docs/ && git commit && git push"
echo "   → Settings → Pages → Branch: main, /docs → Save"
echo "=================================================="
